# ESET Detection & Response rule generator

Please refer to the rule guide for a full reference of all available options. The rule guide can be found [here](https://help.eset.com/tools/eei/eei_rules_guide_1.6.pdf).

## Installing
Install directly from the git repository using the following command:

```shell
pip install git+https://github.com/dmaasland/eset-rulegen.git
```

## Simple example
Before you start make sure the **`eset_rulegen`** library is imported:

```python
from eset_rulegen import *
```

Or if you don't want to use wildcard imports try this (for this example):

```python
from eset_rulegen import Description
from eset_rulegen import Definition
from eset_rulegen import Condition
from eset_rulegen import Process
from eset_rulegen import Rule
```

When creating rules a description with at least a name and a category is required. So start by creating a **`Description`** object:

```python
description = Description(
    name='Simple rule to check for execution of powershell.exe',
    category='Demo rules'
)
```

This object will represent the description of our rule. Now create the condition for the rule. In this example we want to create a rule that triggers when **`powershell.exe`** is executed. So we create a new **`Condition`** object:

```python
condition = Condition(
    component='Module',
    property='OriginalFileName',
    condition='is',
    value='POWERSHELL.EXE'
)
```

We want this condition to apply to a process. So we wrap it into a **`Process`** object:

```python
process = Process(
    condition
)
```

This object needs to be inserted into a **`Definition`**. So let's do that:

```python
definition = Definition(
    process=process
)
```

And finally we can combine it all into one **`Rule`** object:

```python
rule = Rule(
    definition,
    description
)
```

The final script should now look something like this:

```python
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

    condition = Condition(
        component='Module',
        property='OriginalFilename',
        condition='is',
        value='POWERSHELL.EXE'
    )

    process = Process(
        condition
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
```

Note the added **`print(rule)`** at the end. When we execute this script a new rule is printed:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<rule>
  <definition>
    <process>
      <condition component="Module" property="OriginalFilename" condition="is" value="POWERSHELL.EXE" />
    </process>
  </definition>
  <description>
    <name>Simple rule to check for execution of powershell.exe</name>
    <category>Demo rules</category>
  </description>
</rule>
```

## Medium example
Let's say we want to add other script interpreters to our rule as well. We can do that by creating multiple conditions:
```python
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
```

We also need an extra import for that:

```python
from eset_rulegen import Operator
```

We then need to wrap them all up into an **`Operator`** object:

```python
operator = Operator(
    "OR",
    [condition1, condition2, condition3]
)
```

Then we simply pass that to the **`Process`** object instead of our single condition:

```python
process = Process(
    operator
)
```

Complete script:

```python
from eset_rulegen import Operator
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
```

Output:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<rule>
  <definition>
    <process>
      <operator type="OR">
        <condition component="Module" property="OriginalFilename" condition="is" value="POWERSHELL.EXE" />
        <condition component="Module" property="OriginalFilename" condition="is" value="WSCRIPT.EXE" />
        <condition component="Module" property="OriginalFilename" condition="is" value="CSCRIPT.EXE" />
      </operator>
    </process>
  </definition>
  <description>
    <name>Simple rule to check for execution of powershell.exe</name>
    <category>Demo rules</category>
  </description>
</rule>
```