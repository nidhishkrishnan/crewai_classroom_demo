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
    goal="Find recipes online using available ingredients.",
    backstory="You find accurate, tasty recipes from the web.",
    llm=ollama_model,
    tools=tools,
    verbose=True
)

meal_writer = Agent(
    role="Meal Writer",
    goal="Write a simple step-by-step recipe based on the chosen dish.",
    backstory="You are a friendly cooking teacher writing instructions for beginners.",
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
    description="Find 2–3 recipes online using these ingredients. Use the Recipe Search tool.",
    agent=recipe_finder,
    expected_output="List of real recipes."
)

meal_task = Task(
    description="Choose one recipe and write a beginner-friendly step-by-step recipe.",
    agent=meal_writer,
    expected_output="A clear, simple recipe."
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
