import argparse
import re
import sys
import yaml

def parse_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def remove_comments(content):
    content = re.sub(r'\|\|.*', '', content)
    content = re.sub(r'\{\{!.*?\}\}', '', content, flags=re.DOTALL)
    return content

def parse_array(array_str):
    array_str = array_str.strip('[]')
    items = array_str.split(',')
    return [parse_value(item.strip()) for item in items]

def parse_dict(dict_str):
    dict_str = dict_str.strip('table(')
    items = dict_str.split(',')
    result = {}
    for item in items:
        if '=>' in item:
            key, value = item.split('=>', 1)  # Используем 1, чтобы разделить только на 2 части
            result[key.strip()] = parse_value(value.strip())
        else:
            raise ValueError(f"Invalid dictionary item: {item}")
    return result

def parse_value(value):
    print(f"Parsing value: {value}")
    value = value.strip()
    if value.startswith('[') and value.endswith(']'):
        return parse_array(value)
    elif value.startswith('table(') and value.endswith(')'):
        return parse_dict(value)
    elif value.isdigit():
        return int(value)
    elif re.match(r'^\$[_a-z]+', value):
        return value[1:]
    elif value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    else:
        return value


def convert_to_yaml(content):
    lines = content.splitlines()
    result = {}
    for line in lines:
        line = line.strip()
        if line.startswith('var'):
            _, name, value = line.split(maxsplit=2)
            result[name] = parse_value(value)
    return yaml.dump(result)

def main():
    parser = argparse.ArgumentParser(description='Convert custom config language to YAML.')
    parser.add_argument('file', type=str, help='Path to the input configuration file')
    args = parser.parse_args()

    try:
        content = parse_input(args.file)
        content = remove_comments(content)
        yaml_output = convert_to_yaml(content)
        print(yaml_output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()