import yaml

from eset_rulegen import Ancestor
from eset_rulegen.parentprocess import ParentProcess
from eset_rulegen.process import Process
from eset_rulegen.operations import Operations
from eset_rulegen.operation import Operation
from eset_rulegen.condition import Condition
from eset_rulegen.description import Description
from eset_rulegen.actions import Actions
from eset_rulegen.definition import Definition
from eset_rulegen.operator import Operator
from eset_rulegen.rule import Rule


class YamlRule:

    def __init__(self, yml_path):

        self.yml_path = yml_path

        with open(self.yml_path, 'r') as f:
            rule_dict = yaml.load(f, Loader=yaml.FullLoader)

        self.rule = self.create_rule(rule_dict['rule'])

    def __repr__(self):

        return self.rule.xml_string()

    def create_description(self, description_dict):

        return Description(**description_dict)

    def create_actions(self, action_dict):

        return Actions(action_dict)

    def create_definition(self, definition_dict):

        args = {}
        for k in definition_dict.keys():
            args[k] = self.create_object_args(definition_dict[k], k)

        return Definition(**args)

    def create_object_args(self, obj, current):

        classes = {
            'ancestor': Ancestor,
            'parentprocess': ParentProcess,
            'process': Process,
            'operations': Operations,
            'operation': Operation,
            'condition': Condition
        }

        args = {}

        for k, v in obj.items():

            if isinstance(v, dict):
                new_obj = self.create_object_args(obj[k], k)
                args['content'] = new_obj

            else:
                args[k] = v

        if current == 'operator':
            return self.create_operator(args)
        elif current:
            return classes[current](**args)

    def create_operator(self, operator_dict):

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
                        self.create_operator(item['operator'])
                    )

            operator = Operator(
                type=operator_dict['type'],
                content=conditions
            )

        return operator

    def create_rule(self, rule_dict):

        description = self.create_description(rule_dict['description'])
        actions = self.create_actions(rule_dict['actions'])
        definition = self.create_definition(rule_dict['definition'])

        rule = Rule(
            definition,
            description,
            actions
        )

        return rule
