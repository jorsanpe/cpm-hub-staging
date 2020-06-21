import random
import string


def __random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_c_function():
    function_name = __random_string()
    return f'''
int {function_name}(int a, int b) {{
    return a + b;
}}
'''
