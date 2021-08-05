class RuleError(Exception):
    """Base class for rule exceptions"""
    pass


class ActionsError(RuleError):
    """Something went wrong when setting the rule actions"""
    pass


class DescriptionError(RuleError):
    """Something went wrong when setting the rule description"""
    pass


class OperatorError(RuleError):
    """Something went wrong with a rule operator"""
    pass


class AncestorError(RuleError):
    """Something went wrong with the ancestor object"""
    pass


class ParentProcessError(RuleError):
    """Something went wrong with the parent process object"""
    pass


class ProcessError(RuleError):
    """Something went wrong with the process object"""
    pass


class OperationError(RuleError):
    """Something went wrong with an operation"""
    pass
