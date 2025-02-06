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
            line = re.sub(r'chop (\w+) = ask_mandem "(.+)"', r'\1 = input("\2")', line)
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
            line = re.sub(r'spin_da_block (\w+) in (.+):', r'for \1 in \2:', line)
            python_code.append("    " * indent_level + line)
            indent_level += 1
            continue
        elif line.startswith("safe_mode"):
            python_code.append("try:")
            indent_level += 1
            continue
        elif line.startswith("catch_case"):
            python_code.append("except Exception as e:")
            indent_level += 1
            continue
        elif line == "":
            indent_level = max(0, indent_level - 1)
            continue

        python_code.append("    " * indent_level + line)
    
    return '\n'.join(python_code)

# Example test
brogramming_code = """
chop x = ask_mandem "Wagwan, what’s your name?"
big_ting "Safe, " + x

chop mandem = ["Jake", "Tyrone", "Kieran"]
spin_da_block name in mandem:
    big_ting "Wagwan, " + name

safe_mode:
    chop y = "5" + 2
catch_case:
    big_ting "Bruh, error: " + str(e)
"""

python_code = brogramming_to_python(brogramming_code)
print("Translated Python Code:\n")
print(python_code)

# Execute the converted Python code
exec(python_code)
