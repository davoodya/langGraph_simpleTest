from ai_agent import build_agent
from schema import BusinessState

# test input data to be used in LangGraph studio
test_input: BusinessState = {
    "input_data": {
        "today": {"revenue": 1400, "cost": 1100, "customers": 50},
        "yesterday": {"revenue": 1200, "cost": 900, "customers": 45}
    },
    "metrics": {},
    "recommendations": ""
}

# Build the LangGraph agent
agent = build_agent()

# Run the agent
if __name__ == "__main__":
    final_state = agent.invoke(test_input)

    print("\nFinal State:\n");    print(final_state)