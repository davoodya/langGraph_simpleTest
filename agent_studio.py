from dotenv import load_dotenv
load_dotenv()

from ai_agent import build_agent
from schema import BusinessState
import json

import os
print("LangSmith Project:", os.getenv("LANGSMITH_PROJECT"))
print("LangSmith Tracing:", os.getenv("LANGSMITH_TRACING"))

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