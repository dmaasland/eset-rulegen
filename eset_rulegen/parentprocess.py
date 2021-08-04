from dataclasses import dataclass

from eset_rulegen.condition import Condition
from eset_rulegen.operator import Operator
from eset_rulegen.exceptions import ParentProcessError


@dataclass
class ParentProcess:

    content: object

    def __post_init__(self):

        supported_objects = [
            Condition,
            Operator
        ]

        for supported_object in supported_objects:
            if isinstance(self.content, supported_object):
                return

        raise ParentProcessError(
            f'Type "{type(self.content).__name__}" not supported for "{type(self).__name__}"'
        )