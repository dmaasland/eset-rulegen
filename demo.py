from eset_rulegen.operator import Operator
from eset_rulegen import Description
from eset_rulegen import Definition
from eset_rulegen import Condition
from eset_rulegen import Process
from eset_rulegen import Rule


def main():

    description = Description(
        name='Simple rule to check for execution of powershell.exe',
        category='Demo rules'
    )

    condition1 = Condition(
        component='Module',
        property='OriginalFilename',
        condition='is',
        value='POWERSHELL.EXE'
    )

    condition2 = Condition(
        component='Module',
        property='OriginalFilename',
        condition='is',
        value='WSCRIPT.EXE'
    )

    condition3 = Condition(
        component='Module',
        property='OriginalFilename',
        condition='is',
        value='CSCRIPT.EXE'
    )

    operator = Operator(
        "OR",
        [condition1, condition2, condition3]
    )

    process = Process(
        operator
    )

    definition = Definition(
        process=process
    )

    rule = Rule(
        definition,
        description
    )

    print(rule)


if __name__ == '__main__':
    main()