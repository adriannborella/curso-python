from sqlalchemy import create_engine
import yaml

yaml_file = open("z:\\07\\db.yml", 'r')
yaml_content = yaml.load(yaml_file, Loader=yaml.FullLoader)

dbname = yaml_content.get("dbname")
user = yaml_content.get("user")
password = yaml_content.get("pass")
host = yaml_content.get("host")
port = yaml_content.get("port")

db_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
print(db_string)
db = create_engine(db_string)

result_set = db.execute("SELECT * FROM usuarios")
for r in result_set:
    print(r)
