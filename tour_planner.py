from crewai import Agent, Task, Crew, LLM

# -----------------------------------
# 1. Get user input
# -----------------------------------
city = input("Enter a city name for travel planning: ")

# 2. Setup Ollama Model
ollama_model = LLM(
    model="ollama/llama3.2:1b",
    base_url="http://localhost:11434"
)

# -----------------------------------
# 3. Agents
# -----------------------------------

destination_agent = Agent(
    role="Destination Finder",
    goal="Suggest the best attractions in a city.",
    backstory=(
        "You are an expert on world travel destinations and know what tourists enjoy."
    ),
    llm=ollama_model,
    verbose=True
)

budget_agent = Agent(
    role="Budget Planner",
    goal="Provide simple, beginner-friendly travel cost estimates.",
    backstory=(
        "You are practical with money and specialize in giving clear cost breakdowns."
    ),
    llm=ollama_model,
    verbose=True
)

itinerary_agent = Agent(
    role="Itinerary Designer",
    goal="Create an easy-to-follow itinerary for the trip.",
    backstory=(
        "You organize travel activities into a clear day-by-day schedule."
    ),
    llm=ollama_model,
    verbose=True
)

# -----------------------------------
# 4. Tasks (using user input city)
# -----------------------------------

destination_task = Task(
    description=(
        f"List 5–7 must-see attractions in {city}. Include a mix of viewpoints, "
        f"nature, city sights, and unique experiences."
    ),
    expected_output="A bullet list of attractions with 1-line descriptions.",
    agent=destination_agent
)

budget_task = Task(
    description=(
        "Using the attractions from the destination finder, estimate a simple "
        f"daily budget for visiting {city}. Include food, local transport, and "
        "attraction fees."
    ),
    expected_output="A cost breakdown with approximate daily total.",
    agent=budget_agent
)

itinerary_task = Task(
    description=(
        f"Using the destinations and budget, create a clear 2-day itinerary for {city}. "
        "Make it beginner-friendly."
    ),
    expected_output="A formatted 2-day itinerary.",
    agent=itinerary_agent
)

# -----------------------------------
# 5. Crew Execution
# -----------------------------------

crew = Crew(
    agents=[destination_agent, budget_agent, itinerary_agent],
    tasks=[destination_task, budget_task, itinerary_task],
    verbose=False
)

result = crew.kickoff()

print("\n=== Final Travel Plan ===\n")
print(result)
