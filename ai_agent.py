from schema import BusinessState
from langgraph.graph import StateGraph


def input_node(state: BusinessState) -> BusinessState:
    #state["input_data"] = input_data
    return state
