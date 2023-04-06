import yaml

def new_func():
    data = yaml.safe_load(opem('nlu\\train.yml', 'r', encoding='utf-8').read())
    return data

data = new_func()

for command in data['commands']:
    print(command)