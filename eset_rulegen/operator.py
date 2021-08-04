from eset_rulegen.exceptions import OperatorError
from dataclasses import dataclass

@dataclass
class Operator:

    type: str
    content: object

    def __post_init__(self):

        supported_operators = [
            'OR',
            'AND',
            'NOT'
        ]

        try:
            assert self.type.upper() in supported_operators
            self.type = self.type.upper()
        except AssertionError:
            raise OperatorError(f'Unsupported operator "{self.type}"')
