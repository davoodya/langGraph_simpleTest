# AI Business Agent using LangGraph

This project implements a simple AI Agent using the [LangGraph](https://github.com/langchain-ai/langgraph) framework.  
It analyzes daily business data such as sales, costs, and customer counts to generate actionable recommendations.

---

## Features

1. Calculates **profit**, **CAC**, and **daily percentage changes**
2. Warns when **CAC increases** or **profit is negative**
3. Recommends actions such as increasing ads or reducing cost
4. Modular architecture using LangGraph nodes

---

## Agent Workflow
[Input Node] → [Processing Node] → [Recommendation Node]

1. **Input Node**: Accepts a business JSON object
2. **Processing Node**: Computes key metrics:
   1. `profit = revenue - cost`
   2. `CAC = cost / customers`
   3. percentage changes from yesterday
3. **Recommendation Node**: Suggests decisions based on the metrics

---

## LangGraph Studio Usage Guide
### 0. Create a Account on LangSmith and Create a Tracing Project
you should create a project in [LangSmith](https://smith.langchain.com/) and get the project name and api key and other necessary environments variables from the project settings.

### 1. Set LangGraph Environment Variables
then create a `.env` file in the root directory of the project and add the following lines:

```txt   
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="PUT_YOUR_API_KEY_HERE"
LANGSMITH_PROJECT="Your_Project_Name"
```

Notes:
1. `.env` file should be in the root directory of the project
2. get API keys from [LangSmith](https://smith.langchain.com/) 

### 2. Run the LangGraph Studio Agent
```bash
python agent_studio.py
```
----

## Locally Usage Guide

### 1. Install requirements

```bash
pip install -r requirements.txt
```
### 2. Run the Agent Stand-Alone Locally
```bash
python run_agent_locally.py
```

### 3. Running Tests
```sh
#Test Input Node
python test_agent.py

#Test full agent logic and output
python test_full_agent.py
```
### 4. Project Structure
```bash
AI-Business/
│
├── ai_agent.py           # Main LangGraph agent with input, process, and recommendation nodes
├── schema.py             # Shared state structure using TypedDict
├── agent_studio.py          # Sample run with test data (CLI usage)
├── run_agent_locally.py       # Clean agent runner for LangGraph Studio
├── test_agent.py         # Unit test for input node
├── test_full_agent.py    # Full flow test (metrics + recommendations)
├── requirements.txt      # Required Python dependencies
└── README.md             # This file
```

### 6. Sample Output
```json
{
  "input_data": {
    "today": {
      "revenue": 1400,
      "cost": 1100,
      "customers": 50
    },
    "yesterday": {
      "revenue": 1200,
      "cost": 900,
      "customers": 45
    }
  },
  "metrics": {
    "profit": 300,
    "revenue_change_pct": 16.67,
    "cost_change_pct": 22.22,
    "today_cac": 22.0,
    "yesterday_cac": 20.0,
    "cac_change_pct": 10.0
  },
  "recommendations": "Sales have grown.\nConsider increasing advertising budget."
}

```


## Author
- Developed by: [Davood Yahay](https://github.com/davoodya)
- Website: [davoodya.ir](https://davoodya.ir)
- Telegram: [@davoodya](https://t.me/davoodya)
- YouTube: [@DavoodSec](https://www.youtube.com/@DavoodSec)
- LinkedIn: [Davood Yahay](https://www.linkedin.com/in/davoodya)
- Email: davoodyahay@gmail.com
