import json
from jinja2 import Template, FileSystemLoader, Environment

def generate_index(env, data):

    template = env.get_template('index_template.html')
    
    with open('index.html', 'w') as file:
        file.write(template.render(recipes=data['recipes']))

def generate_recipes(env, data):

    with open('recipes.json') as f:
      data = json.load(f)

    template = env.get_template('recipes_template.html')

    for recipe in data['recipes']:
        with open(f'{recipe["src"]}.html', 'w') as file:
            file.write(template.render(recipe))

if __name__ == '__main__':
    loader = FileSystemLoader('common/')
    env = Environment(loader=loader)

    with open('recipes.json') as f:
      data = json.load(f)

    generate_index(env, data)
    generate_recipes(env, data)
