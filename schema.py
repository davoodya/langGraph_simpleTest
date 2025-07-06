from typing import TypedDict,Dict, Any

# Status of the Business Agent
class BusinessState(TypedDict):
    input_data: Dict[str, Any] # Input Data
    metrics: Dict[str, Any] # Output Data
    recommendations: str # recommendations output

