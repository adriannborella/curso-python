import yaml

yaml_file = open("z:\\06\\db.yml", 'r')
yaml_content = yaml.load(yaml_file, Loader=yaml.FullLoader)

print(f"tipo: {yaml_content.get('tipo')}")
print(f"host: {yaml_content.get('host')}")
print(f"port: {yaml_content.get('port')}")
print(f"user: {yaml_content.get('user')}")
print(f"pass: {yaml_content.get('pass')}")
