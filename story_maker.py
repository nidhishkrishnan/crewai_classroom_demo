import os
from crewai import Agent, Task, Crew, Process, LLM

# =============================================================================
# CONFIGURATION
# =============================================================================
# We use Ollama to run local models.
# Make sure you have Ollama installed and have run: `ollama pull llama3.2:1b`
# The base_url points to your local Ollama instance.
ollama_model = LLM(
    model="ollama/llama3.2:1b",
    base_url="http://localhost:11434"
)

# =============================================================================
# AGENTS
# =============================================================================
# Agents are the "workers" in our crew. Each has a role, a goal, and a backstory.

# 1. Research Agent: Finds facts.
researcher = Agent(
    role='Science Researcher',
    goal='Find simple, clear facts about the given topic.',
    backstory='You are a curious scientist who loves explaining things simply to students.',
    verbose=True, # This lets us see what the agent is thinking in the console.
    allow_delegation=False, # We want to keep it simple, no delegating to others.
    llm=ollama_model # We tell the agent to use our local Ollama model.
)

# 2. Writer Agent: Writes the content.
writer = Agent(
    role='Science Writer',
    goal='Write a short, engaging paragraph based on the research.',
    backstory='You are a writer for a children\'s science magazine. You write in a fun way.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_model
)

# 3. Editor Agent: Polishes the content.
editor = Agent(
    role='Editor',
    goal='Ensure the text is grammatically correct and easy to read.',
    backstory='You are a strict editor who makes sure everything is perfect for the students.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_model
)

# =============================================================================
# TASKS
# =============================================================================
# Tasks are the specific jobs assigned to agents.

# The topic we want to explain.
topic = "Photosynthesis"

# Task 1: Research
task_research = Task(
    description=f"Find 3 key facts about {topic}. Keep them simple.",
    agent=researcher,
    expected_output="A list of 3 simple facts about the topic."
)

# Task 2: Write
task_write = Task(
    description=f"Write a short paragraph (3-4 sentences) explaining {topic} using the facts provided.",
    agent=writer,
    expected_output="A short, engaging paragraph explaining the topic."
)

# Task 3: Edit
task_edit = Task(
    description=f"Review the paragraph for clarity and simplicity. Fix any complex words.",
    agent=editor,
    expected_output="A final, polished paragraph ready for students."
)

# =============================================================================
# CREW
# =============================================================================
# The Crew manages the agents and tasks.

classroom_crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[task_research, task_write, task_edit],
    verbose=False, # Show the full progress in the console
    process=Process.sequential # Run tasks one after another (1 -> 2 -> 3)
)

# =============================================================================
# EXECUTION
# =============================================================================
print(f"Starting the Classroom Crew to learn about: {topic}\n")

# Kickoff the crew!
result = classroom_crew.kickoff()

print("\n\n########################")
print("## FINAL RESULT ##")
print("########################\n")
print(result)
