import yaml

yaml_file = open("z:\\06\\learn_yaml.yaml", 'r')
yaml_content = yaml.load(yaml_file, Loader=yaml.FullLoader)

print("Key: Value")
for key, value in yaml_content.items():
    print(f"{key}: {value}")
