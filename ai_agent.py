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

    # Calculate metrics
    profit = today["revenue"] - today["cost"]

    revenue_change_pct = ((today["revenue"] - yesterday["revenue"]) / yesterday["revenue"]) * 100
    cost_change_pct = ((today["cost"] - yesterday["cost"]) / yesterday["cost"]) * 100

    today_cac = today["cost"] / today["customers"] if today["customers"] else 0
    yesterday_cac = yesterday["cost"] / yesterday["customers"] if yesterday["customers"] else 0
    cac_change_pct = ((today_cac - yesterday_cac) / yesterday_cac) * 100 if yesterday_cac else 0

    # Save in State
    state["metrics"] = {
        "profit": profit,
        "revenue_change_pct": revenue_change_pct,
        "cost_change_pct": cost_change_pct,
        "today_cac": today_cac,
        "yesterday_cac": yesterday_cac,
        "cac_change_pct": cac_change_pct
    }

    return state
