from eset_rulegen import *


def main():

    ancestor = Ancestor(
        Condition(
            'FileItem',
            'Path',
            'startswith',
            '%SYSTEM%'
        ),
        distance=2,
        unique=True
    )

    parentprocess = ParentProcess(
        Condition(
            'FileItem',
            'Path',
            'startswith',
            '%SYSTEM%'
        )
    )

    process = Process(
        Operator('or', [
            Condition(
                'FileItem',
                'Path',
                'notstartswith',
                '%SYSTEM%'
            ),
            Condition(
                'FileItem',
                'Path',
                'notstartswith',
                '%WINDIR%'
            )
        ])
    )

    operations = Operations(
        Operation(
            "WriteFile",
            Condition(
                'FileItem',
                'Path',
                'ends',
                'update'
            )
        )
    )

    definition = Definition(
        ancestor=ancestor,
        parentprocess=parentprocess,
        process=process,
        operations=operations
    )

    description = Description(
        name='Testrule',
        category='Test category',
        explanation='test explanation',
        os='windows',
        mitreattackid=['1', '2'],
        malicious_causes='test malicious cause',
        benign_causes='test bening cause',
        recommended_actions='test recommended actions',
        severity=80
    )

    actions = Actions(
        actions=[
            'MarkAsScript',
            'DropEvent'
        ]
    )

    rule = Rule(
        definition=definition,
        description=description,
        actions=actions
    )

    print(rule)


if __name__ == '__main__':
    main()
