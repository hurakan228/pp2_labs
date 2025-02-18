import re

# 1
def match_a_b(s):
    return bool(re.fullmatch(r'ab*', s))

# 2
def match_a_bbb(s):
    return bool(re.fullmatch(r'ab{2,3}', s))

# 3
def find_underscore_sequences(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

# 4
def find_upper_lower(s):
    return re.findall(r'[A-Z][a-z]+', s)

# 5
def match_a_any_b(s):
    return bool(re.fullmatch(r'a.*b', s))

# 6
def replace_with_colon(s):
    return re.sub(r'[ ,.]', ':', s)

# 7
def snake_to_camel(s):
    return ''.join(word.capitalize() for word in s.split('_'))

# 8
def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

# 9
def insert_spaces(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

# 10
def camel_to_snake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

# пример
if __name__ == "__main__":
    print(match_a_b("abbb"))  # True
    print(match_a_bbb("abb"))  # True
    print(find_underscore_sequences("hello_world test_example abc_def"))  # ['hello_world', 'test_example', 'abc_def']
    print(find_upper_lower("Hello World Test String"))  # ['Hello', 'World', 'Test', 'String']
    print(match_a_any_b("axyzb"))  # True
    print(replace_with_colon("Hello, world. This is a test"))  # 'Hello:world:This:is:a:test'
    print(snake_to_camel("hello_world_example"))  # 'HelloWorldExample'
    print(split_at_uppercase("SplitAtUppercase"))  # ['', 'Split', 'At', 'Uppercase']
    print(insert_spaces("InsertSpacesBetweenWords"))  # 'Insert Spaces Between Words'
    print(camel_to_snake("CamelCaseToSnakeCase"))  # 'camel_case_to_snake_case'
