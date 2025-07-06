from schema import BusinessState
from langgraph.graph import StateGraph


def input_node(state: BusinessState) -> BusinessState:
    #state["input_data"] = input_data
    return state

def processing_node(state: BusinessState) -> BusinessState:
    # Define Datas
    data = state["input_data"]

    today = data["today"]
    yesterday = data["yesterday"]

    # Calculate metric
    profit = today["revenue"] - today["cost"]

    revenue_change_pct = ((today["revenue"] - yesterday["revenue"]) / yesterday["revenue"]) * 100
    cost_change_pct = ((today["cost"] - yesterday["cost"]) / yesterday["cost"]) * 100
