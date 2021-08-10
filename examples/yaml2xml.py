from eset_rulegen import YamlRule


def main():

    rule = YamlRule('rule.yml')
    print(rule)


if __name__ == '__main__':
    main()
