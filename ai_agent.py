from schema import BusinessState
from langgraph.graph import StateGraph, END


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

def recommendation_node(state: BusinessState) -> BusinessState:
    metrics = state["metrics"]
    messages = []

    # 1. Profit Checking
    if metrics["profit"] < 0:
        messages.append("Profit is negative.\n "
                        "Consider reducing operational costs.")

    # 2. CAC growing checking
    if metrics["cac_change_pct"] > 20:
        messages.append("CAC has increased significantly.\n "
                        "Invest in customer acquisition strategies or Review marketing campaigns .")
    # 3. Sales Growing checking
    if metrics["revenue_change_pct"] > 0:
        messages.append("Sales have grown.\n "
                        "Consider increasing advertising budget.")

    # 4. if Not messages means all metrics is OK
    if not messages:
        messages.append("All metrics are within acceptable range. No action needed for this time.")

    # Save in the State
    state["recommendations"] = "\n".join(messages)
    return state


# Define the build graph agent
def build_agent():
    builder = StateGraph(BusinessState)

    builder.add_node("input", input_node)
    builder.add_node("processing", processing_node)
    builder.add_node("recommendation", recommendation_node)

    # define the data passageway
    builder.set_entry_point("input")
    builder.add_edge("input", "processing")
    builder.add_edge("processing", "recommendation")
    builder.add_edge("recommendation", END)

    # build the agent
    return builder.compile()



