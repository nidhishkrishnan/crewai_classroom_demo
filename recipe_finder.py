from crewai import Agent, Task, Crew, LLM
from crewai.tools import BaseTool
from langchain_community.utilities import SerpAPIWrapper
from langchain_experimental.tools import PythonREPLTool

# ---------------------------------------
# 1. Setup Ollama Model
# ---------------------------------------
ollama_model = LLM(
    model="ollama/llama3.2:1b",
    base_url="http://localhost:11434"
)

# ---------------------------------------
# 2. Setup Real Tools
# ---------------------------------------

class RecipeSearchTool(BaseTool):
    name: str = "Recipe Search"
    description: str = "Search the web for recipes using given ingredients."

    def _run(self, query: str) -> str:
        search = SerpAPIWrapper()
        return search.run(query)

class CalculatorTool(BaseTool):
    name: str = "Python Calculator"
    description: str = "Perform calculations for portions or nutrition."

    def _run(self, query: str) -> str:
        python_repl = PythonREPLTool()
        return python_repl.run(query)

recipe_search_tool = RecipeSearchTool()
calculator_tool = CalculatorTool()

tools = [recipe_search_tool, calculator_tool]

# ---------------------------------------
# 3. Define Agents
# ---------------------------------------

ingredient_checker = Agent(
    role="Ingredient Checker",
    goal="Check which ingredients the user has available.",
    backstory="You verify ingredients carefully.",
    llm=ollama_model,
    verbose=True
)

recipe_finder = Agent(
    role="Recipe Finder",
    goal="Find recipes online using ONLY the available ingredients provided.",
    backstory="""You are a strict recipe searcher who NEVER suggests ingredients 
    that aren't available. You only find recipes using the exact ingredients given.""",
    llm=ollama_model,
    tools=tools,
    verbose=True
)

meal_writer = Agent(
    role="Meal Writer",
    goal="Write recipes using ONLY the ingredients confirmed as available.",
    backstory="""You are a cooking teacher who never adds extra ingredients. 
    You work strictly within the constraints of what's available.""",
    llm=ollama_model,
    verbose=True
)

# ---------------------------------------
# 4. User Input
# ---------------------------------------
user_input = input("Enter your available ingredients, separated by commas: ")
ingredients_list = [item.strip() for item in user_input.split(",")]

# ---------------------------------------
# 5. Define Tasks
# ---------------------------------------
ingredient_task = Task(
    description=f"Check which of these ingredients are available: {ingredients_list}.",
    agent=ingredient_checker,
    expected_output="List of available ingredients."
)

recipe_task = Task(
    description=f"""Find 2-3 recipes online that use ONLY these ingredients: {ingredients_list}.
    You MUST NOT suggest recipes with ingredients outside this list.
    Use the Recipe Search tool to find real recipes.""",
    agent=recipe_finder,
    expected_output="List of 2-3 real recipes using only the provided ingredients.",
    context=[ingredient_task]  # Explicitly pass context
)

meal_task = Task(
    description=f"""Choose ONE recipe from the previous search results.
    Write a step-by-step recipe using ONLY these ingredients: {ingredients_list}.
    DO NOT add any ingredients not in this list.""",
    agent=meal_writer,
    expected_output="A clear recipe using only the available ingredients.",
    context=[ingredient_task, recipe_task]  # Pass both previous tasks
)

# ---------------------------------------
# 6. Crew Execution
# ---------------------------------------
crew = Crew(
    agents=[ingredient_checker, recipe_finder, meal_writer],
    tasks=[ingredient_task, recipe_task, meal_task],
    verbose=True
)

result = crew.kickoff()

# ---------------------------------------
# 7. Display Result
# ---------------------------------------
print("\n=== Final Meal Plan ===\n")
print(result)
