from dataclasses import dataclass


@dataclass
class Condition:

    component: str
    property: str
    condition: str
    value: str
