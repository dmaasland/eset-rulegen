from dataclasses import dataclass

from eset_rulegen.exceptions import OperationError


@dataclass
class Operation:

    type: str
    content: object

    def __post_init__(self):

        supported_operations = [
            'CodeInjection',
            'CreateNamedPipe',
            'CreateProcess',
            'CreateRemoteThread',
            'DeleteFile',
            'DnsRequest',
            'HttpRequest',
            'LoadDLL',
            'ModuleDrop',
            'OpenProcess',
            'ReadFile',
            'RegDeleteKey',
            'RegDeleteValue',
            'RegRenameKey',
            'RegSetValue',
            'RenameFile',
            'Scripts',
            'TcpIpAccept',
            'TcpIpConnect',
            'TcpIpProtocolIdentified',
            'UserActivate',
            'UserAddToGroup',
            'UserCreate',
            'UserDisable',
            'UserLogin',
            'UserLogout',
            'UserRemove',
            'UserRemoveFromGroup',
            'WmiExecution',
            'WmiPersistence',
            'WmiQuery',
            'WriteFile'
        ]

        try:
            assert self.type in supported_operations
        except AssertionError:
            raise OperationError(f'Type "{self.type}" not supported')
