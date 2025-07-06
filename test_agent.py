from turtledemo.penrose import start

from schema import BusinessState
from ai_agent import input_node, processing_node

input_data = {
    "today": {
        "revenue": 1200,
        "cost": 800,
        "customers": 40
    },
    "yesterday": {
        "revenue": 1000,
        "cost1": 700,
        "customers": 35
    },
    "metrics": {},
    "recommendation": ""
}

def test_input_node():
    state: BusinessState = {
        "input_data": {
            "today": {"revenue": 1200, "cost": 800, "customers": 40},
            "yesterday": {"revenue": 1000, "cost": 700, "customers": 35}
        },
        "metric": {},
        "recommendation": ""
    }

    result = input_node(state)
    assert result["input_data"]["today"]["revenue"] == 1200
    print("Input Node(1) Test passed!")

def test_processing_node():
    state: BusinessState = {
        "input_data": {
            "today": {"revenue": 1200, "cost": 800, "customers": 40},
            "yesterday": {"revenue": 1000, "cost": 700, "customers": 35}
        },
        "metric": {},
        "recommendation": ""
    }


if __name__ == "__main__":
    test_input_node()