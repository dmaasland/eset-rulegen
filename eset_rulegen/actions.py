from eset_rulegen.exceptions import ActionsError
from dataclasses import dataclass, field


@dataclass
class Actions:

    actions: list[str] = field(default_factory=list)

    def __post_init__(self):

        allowed_actions = [
            'TriggerDetection',
            'MarkAsScript',
            'MarkAsCompromised',
            'HideCommandLine',
            'BlockProcessExecutable',
            'CleanAndBlockProcessExecutable',
            'BlockParentProcessExecutable',
            'CleanAndBlockParentProcessExecutable',
            'IsolateFromNetwork',
            'DropEvent'
        ]

        try:
            for action in self.actions:
                assert action in allowed_actions

        except AssertionError:
            raise ActionsError(f'Action "{action}" not allowed!')
