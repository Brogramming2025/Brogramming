
#Brogramming 2025

import re

def brogramming_to_python(code):
    """
    Translates Brogramming language code to Python code while maintaining proper indentation.
    """
    lines = code.split('\n')
    python_code = []
    indent_level = 0

    for i, line in enumerate(lines):
        line = line.strip()
        
        if line.startswith("chop"):
            line = re.sub(r'chop (\w+) = (.+)', r'\1 = \2', line)
        elif line.startswith("big_ting"):
            line = re.sub(r'big_ting (.+)', r'print(\1)', line)
        elif line.startswith("mandem_linkup"):
            line = re.sub(r'mandem_linkup (\w+)\(\):', r'def \1():', line)
            python_code.append("    " * indent_level + line)
            indent_level += 1
            continue
        elif line.startswith("if_vibes"):
            line = re.sub(r'if_vibes (.+):', r'if \1:', line)
            python_code.append("    " * indent_level + line)
            indent_level += 1
            continue
        elif line.startswith("spin_da_block"):
            line = re.sub(r'spin_da_block (.+):', r'while \1:', line)
            python_code.append("    " * indent_level + line)
            indent_level += 1
            continue
        elif line == "":
            indent_level = max(0, indent_level - 1)
            continue

        python_code.append("    " * indent_level + line)
    
    return '\n'.join(python_code)

# Example test
brogramming_code = """
chop x = 5
if_vibes x > 3:
    big_ting "X is big!"
mandem_linkup greet():
    big_ting "Wagwan!"
"""

python_code = brogramming_to_python(brogramming_code)
print("Translated Python Code:\n")
print(python_code)

# Execute the converted Python code
exec(python_code)
>>>>>>> 3d44531 (Added user input feature (ask_mandem))
