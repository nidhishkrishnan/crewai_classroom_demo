## ✅ **Demo 1:** Story Maker → Writer → Editor (Photosynthesis)    
## ✅ **Demo 2:** Travel Planner (user enters a city → 3 agents create itinerary)
## ✅ **Demo 3:** Recipe Finder (user enters ingredients → agents find and write recipes)


Both examples are explained clearly for classroom use.
You can copy/paste this as your README.md.

---

# CrewAI Classroom Demo 🤖📚

Welcome to the **CrewAI Classroom Demo**!
This project contains **two multi-agent examples** designed to teach students how AI “teamwork” works using **CrewAI + Ollama** (running locally).

---

# 🌟 What Is This Project?

Think of these programs like classroom **group projects**, but the students are AI Agents!
Each agent has a role, goal, and personality. They work together to complete a task.

This demo includes **two real examples**:

---

# 📘 **Demo 1: Story Maker : Research → Write → Edit (Photosynthesis Example)**

Imagine you have to write a short paragraph about **Photosynthesis**.
Instead of doing it all yourself, an AI team works together:

1. **The Researcher** 🕵️‍♂️ — Finds 3 basic facts
2. **The Writer** ✍️ — Turns the facts into a simple paragraph
3. **The Editor** 📝 — Checks grammar and simplifies language

### 🧠 Flow of Demo 1

1. **Start:** The Crew gives the topic **"Photosynthesis"**
2. **Researcher:** Collects 3 simple facts
3. **Writer:** Creates a student-friendly paragraph
4. **Editor:** Fixes grammar and clarity
5. **Final Output:** A clean paragraph printed on screen

This helps students understand how multi-step AI work can flow from one agent to another.

---

# 🌍 **Demo 2: Travel Planner (User Input → Multi-Agent Team)**

This second example is more interactive and fun.
When you run the script, it asks:

```
Enter a city name for travel planning:
```

You type something like **Seattle**, **Tokyo**, or **Paris**, and the AI team works:

### 👥 Agents in Demo 2

1. **Destination Finder** 🧭

   * Suggests 5–7 attractions in the chosen city
   * Finds viewpoints, nature spots, and unique activities

2. **Budget Planner** 💰

   * Calculates approximate costs
   * Food, transport, and attraction fees
   * Gives a simple daily budget

3. **Itinerary Designer** 🗓

   * Creates a 2-day beginner-friendly travel plan
   * Uses the attractions + budget to build a schedule

### 🧠 Flow of Demo 2

1. User types a city name
2. Destination Agent → Finds places to visit
3. Budget Agent → Calculates daily cost
4. Itinerary Agent → Builds a final 2-day plan
5. Program prints a complete travel itinerary

This demo is perfect for showing:

* agent collaboration
* multi-step reasoning
* user-driven workflows

---

# 🍳 **Demo 3: Recipe Finder (Ingredient-Based Meal Planning)**

This example shows how AI agents can work with **real-world constraints** and **web tools**.
When you run the script, it asks:
```
Enter your available ingredients, separated by commas:
```

You type something like **egg, fish, cabbage, carrot, salt, oil**, and the AI team works:

### 👥 Agents in Demo 3

1. **Ingredient Checker** 📋
   * Verifies which ingredients are available
   * Creates a clean list for the next agents

2. **Recipe Finder** 🔍
   * Searches the web for real recipes using the ingredients
   * Uses a web search tool to find 2-3 matching recipes
   * Must only suggest recipes with available ingredients

3. **Meal Writer** 👨‍🍳
   * Selects the best recipe from search results
   * Writes clear, beginner-friendly cooking instructions
   * Creates step-by-step directions using only available ingredients

### 🧠 Flow of Demo 3

1. User enters available ingredients
2. Ingredient Checker → Confirms the ingredient list
3. Recipe Finder → Searches web for matching recipes (uses Recipe Search Tool)
4. Meal Writer → Creates a simple, step-by-step recipe
5. Program prints a complete meal plan

### 🛠️ Special Features in Demo 3

This demo introduces **AI tools**:
* **Recipe Search Tool** — Searches the web for real recipes
* **Calculator Tool** — Can calculate portions or nutritional info

This shows students:
* How AI agents can use external tools
* Web search integration with AI
* Working within real-world constraints (limited ingredients)
* Multi-agent collaboration with tool usage

---

# 🛠️ Setup Instructions for Both Demos

## 1. Install **Ollama** (Local AI Model)

This project uses **Ollama** so everything runs locally and free.

1. Download from: [https://ollama.com](https://ollama.com)
2. Open Terminal
3. Pull the model:

```bash
ollama pull llama3.2:1b
```

(You can upgrade to bigger models later.)

---

## 2. Create and Activate a Python Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate      # Mac/Linux
.\.venv\Scripts\activate.ps1   # Windows PowerShell
```

---

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

Your **requirements.txt** should include:

```
crewai
langchain_openai
langchain_community
langchain_ollama
litellm
google-search-results
langchain_experimental
python-dotenv
```

---

# 🚀 How to Run the Demos

### ▶️ **Demo 1: Research → Write → Edit**

```
python story_maker.py
```

You will see each agent thinking and generating output step-by-step.

---

### ▶️ **Demo 2: Travel Planner (User Input)**

```
python tour_planner.py
```

You will be prompted to enter a city:

```
Enter a city name for travel planning:
```

Try cities like:

* Seattle
* Tokyo
* London
* Singapore

---

# 🧪 Experiment and Learn!

Here are fun classroom activities you can try:

### 🔹 Change the topic (Demo 1)

Inside `story_maker.py`, modify:

```python
topic = "The Solar System"
```

Run again and see what changes!

### 🔹 Try new cities (Demo 2)

Run multiple times with different locations.

### 🔹 Add more agents

Examples:

* Fact Checker
* Map Generator
* Restaurant Planner

I can help you expand these anytime!

---

If you'd like, I can also generate:

✅ a **project folder template**,
✅ **diagrams** explaining the agent flow,
✅ or a **third demo** (math tutor, news summarizer, code generator, etc.).
