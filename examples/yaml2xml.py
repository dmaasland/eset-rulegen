import yaml

from eset_rulegen import Ancestor, rule
from eset_rulegen import ParentProcess
from eset_rulegen import Process
from eset_rulegen import Operations
from eset_rulegen import Condition
from eset_rulegen import Description
from eset_rulegen import Actions
from eset_rulegen import Definition
from eset_rulegen import Operator
from eset_rulegen import Rule


def create_description(description_dict):

    return Description(**description_dict)


def create_actions(action_dict):

    return Actions(action_dict)


def create_definition(definition_dict):

    args = create_object_args(definition_dict)
    return Definition(**args)


def create_object_args(obj_dict, current=None):

    classes = {
        'ancestor': Ancestor,
        'parentprocess': ParentProcess,
        'process': Process,
        'operations': Operations,
        'condition': Condition
    }

    if not current:
        args = {}

    for k, v in obj_dict.items():

        if k == 'operator':
            obj = create_operator(obj_dict[k])

        elif isinstance(v, dict):
            obj = create_object_args(v, k)

            if not current:
                obj = classes[k](obj)
                args.update({
                    k: obj
                })

    if not current:
        return args

    return obj


def create_operator(operator_dict):

    operator_content = operator_dict['content']
    conditions = []

    if isinstance(operator_content, list):

        for item in operator_content:
            item_type = list(item.keys())[0]

            if item_type == 'condition':
                conditions.append(
                    Condition(**item[item_type])
                )

            elif item_type == 'operator':
                conditions.append(
                    create_operator(item['operator'])
                )

        operator = Operator(
            type=operator_dict['type'],
            content=conditions
        )

    return operator


def create_rule(rule_dict):

    description = create_description(rule_dict['description'])
    actions = create_actions(rule_dict['actions'])
    definition = create_definition(rule_dict['definition'])

    rule = Rule(
        definition,
        description,
        actions
    )

    return rule


def main():

    with open('rule.yml', 'r') as f:
        rule_dict = yaml.load(f, Loader=yaml.FullLoader)

    rule = create_rule(rule_dict['rule'])

    print(rule)


if __name__ == '__main__':
    main()
