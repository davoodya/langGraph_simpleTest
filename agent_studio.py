from dotenv import load_dotenv
load_dotenv()

from ai_agent import build_agent
from schema import BusinessState
import json
import os

# Validation for LangSmith Configuration
langGraphProject = os.getenv("LANGSMITH_PROJECT")
langGraphAPI = os.getenv("LANGSMITH_API_KEY")
langGraphTracing = os.getenv("LANGSMITH_TRACING")

if not langGraphProject or not langGraphAPI:
    print("You don't have a '.env' file.\n"
          "Please read README.md file, define API and other env variables and try again!")
else:
    print("LangGraph Project: ", langGraphProject)
    print(f"LangGraph Submit: ", bool(langGraphAPI))
    print("LangSmith Tracing: ", langGraphTracing)


# Create the agent
agent = build_agent()

# Test Data
state: BusinessState = {
    "input_data": {
        "today": {"revenue": 1400, "cost": 1100, "customers": 50},
        "yesterday": {"revenue": 1200, "cost": 900, "customers": 45}
    },
    "metrics": {},
    "recommendations": ""
}

# Run the agent
final_state = agent.invoke(state)

# Print the final state
print("Final State: \n");    print(json.dumps(final_state, indent=2))