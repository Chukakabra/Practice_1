import unittest
import yaml
from config_converter import parse_input, remove_comments, convert_to_yaml

class TestConfigParser(unittest.TestCase):

    def test_simple_config(self):
        with open('tests/sample_configs/config1.txt', 'r') as file:
            expected_output = '''
age: 30
hobbies:
- reading
- coding
- hiking
name: John Doe
'''
        content = parse_input('tests/sample_configs/config1.txt')
        content = remove_comments(content)
        yaml_output = convert_to_yaml(content)
        self.assertEqual(yaml.safe_load(yaml_output), yaml.safe_load(expected_output))

    def test_config_with_table(self):
        with open('tests/sample_configs/config2.txt', 'r') as file:
            expected_output = '''
server:
  host: localhost
  port: 8080
'''
        content = parse_input('tests/sample_configs/config2.txt')
        content = remove_comments(content)
        yaml_output = convert_to_yaml(content)
        self.assertEqual(yaml.safe_load(yaml_output), yaml.safe_load(expected_output))

    def test_config_with_nested_table(self):
        with open('tests/sample_configs/config3.txt', 'r') as file:
            expected_output = '''
settings:
  debug: true
  languages:
  - python
  - javascript
  version: 1.0
'''
        content = parse_input('tests/sample_configs/config3.txt')
        content = remove_comments(content)
        yaml_output = convert_to_yaml(content)
        self.assertEqual(yaml.safe_load(yaml_output), yaml.safe_load(expected_output))

    def test_config_with_invalid_syntax(self):
        with self.assertRaises(ValueError):
            content = parse_input('invalid_config.txt')
            content = remove_comments(content)
            convert_to_yaml(content)

if __name__ == '__main__':
    unittest.main()
