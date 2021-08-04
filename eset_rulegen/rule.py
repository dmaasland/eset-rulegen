from eset_rulegen.operator import Operator
from eset_rulegen.definition import Definition
from eset_rulegen.ancestor import Ancestor
from eset_rulegen.parentprocess import ParentProcess
from eset_rulegen.process import Process
from eset_rulegen.condition import Condition
from eset_rulegen.operations import Operations
from eset_rulegen.operations import Operation
import xml.etree.cElementTree as ET

from dataclasses import dataclass

from .actions import Actions
from .description import Description
from .exceptions import DescriptionError

@dataclass
class Rule:
    """Class that describes an ESET EDR rule"""
    definition: Definition
    description: Description
    actions: Actions = None

    def __post_init__(self):
        """Create an empty rule xml object"""
        self.rule = ET.Element('rule')


    def _xml(self):
        """Create an XML object from the Rule class"""

        # Add definition
        self._definition()

        # Add description
        self._description()

        # Add actions
        self._actions()

        return self.rule

    def _definition(self):

        definition = ET.SubElement(self.rule, 'definition')
        parent_fields = [
            self.definition.ancestor,
            self.definition.parentprocess,
            self.definition.process,
            self.definition.operations
        ]

        for parent_field in parent_fields:
            if parent_field is not None:
                self._build_definition(definition, parent_field)        

    def _build_definition(self, definition, item):

        # Recurse lists
        if isinstance(item, list):
            for nested_item in item:
                self._build_definition(definition, nested_item)
            return

        # Description parents
        elif isinstance(item, Ancestor):
            definition = ET.SubElement(
                definition,
                'ancestor', 
                distance=str(item.distance),
                unique=str(item.unique)
            )

        elif isinstance(item, ParentProcess):
            definition = ET.SubElement(definition, 'parentprocess')

        elif isinstance(item, Process):
            definition = ET.SubElement(definition, 'process')

        elif isinstance(item, Operations):
            definition = ET.SubElement(definition, 'operations')

        # Description children
        elif isinstance(item, Operator):
            definition = ET.SubElement(
                definition,
                'operator',
                type=item.type
            )

        elif isinstance(item, Condition):
            definition = ET.SubElement(
                definition,
                'condition', 
                component=item.component,
                property=item.property,
                condition=item.condition,
                value=item.value,
            )
            return

        elif isinstance(item, Operation):
            definition = ET.SubElement(
                definition,
                'operation', 
                type=item.type
            )
            return

        else:
            raise DescriptionError(f'Description item "{item}" not supported!')

        self._build_definition(definition, item.content)


    def _description(self):

        description = ET.SubElement(self.rule, 'description')

        name = self.description.name
        category = self.description.category
        explanation = self.description.explanation
        os = self.description.os
        mitreattackid = self.description.mitreattackid
        malicious_causes = self.description.malicious_causes
        benign_causes = self.description.benign_causes
        recommended_actions = self.description.recommended_actions
        severity = self.description.severity

        ET.SubElement(description, 'name').text = name
        ET.SubElement(description, 'category').text = category

        if explanation is not None:
            ET.SubElement(description, 'explanation').text = explanation

        if os is not None:
            ET.SubElement(description, 'os').text = os

        if mitreattackid:
            ET.SubElement(description, 'mitreattackid').text = ','.join(mitreattackid)

        if malicious_causes is not None:
            ET.SubElement(description, 'malicious_causes').text = malicious_causes

        if benign_causes is not None:
            ET.SubElement(description, 'benign_causes').text = benign_causes

        if recommended_actions is not None:
            ET.SubElement(description, 'recommended_actions').text = recommended_actions

        if severity is not None:
            ET.SubElement(description, 'severity').text = str(severity)


    def _actions(self):

        if self.actions is not None:
            actions = ET.SubElement(self.rule, 'actions')

            for action in self.actions.actions:
                ET.SubElement(actions, 'action', name=action)


    def xml_string(self):
        """Convert an XML object to a string"""
        rule = self._xml()
        ET.indent(rule)
        xml_string = ET.tostring(
            rule,
            encoding='unicode',
            method='xml',
            xml_declaration=True
        )

        return xml_string


    def __repr__(self):
        """Just print the formatted XML"""
        return self.xml_string()

