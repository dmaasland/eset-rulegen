from eset_rulegen.exceptions import DescriptionError

from dataclasses import dataclass
from dataclasses import field

@dataclass
class Description:

    name: str
    category: str
    explanation: str = None
    os: str = None
    mitreattackid: list = field(default_factory=list)
    malicious_causes: str = None
    benign_causes: str = None
    recommended_actions: str = None
    severity: int = None


    def __post_init__(self):

        try:
            assert isinstance(self.mitreattackid, list)
        except AssertionError:
            raise DescriptionError(
                f'Argument "mitreattackid" should be {type(list())}, not {type(self.mitreattackid)}'
            )