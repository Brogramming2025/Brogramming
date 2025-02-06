import re
import random

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
            line = re.sub(r'chop (\w+) = real_talk', r'\1 = True', line)
            line = re.sub(r'chop (\w+) = cap', r'\1 = False', line)
            line = re.sub(r'chop (\w+) = (.+)', r'\1 = \2', line)
        elif line.startswith("big_ting"):
            line = re.sub(r'big_ting (.+)', r'print(\1)', line)
        elif line.startswith("sumting_light"):
            line = re.sub(r'sumting_light (\w+) = (.+) plus (.+)', r'\1 = \2 + \3', line)
        elif line.startswith("minus_dat"):
            line = re.sub(r'minus_dat (\w+) = (.+) minus (.+)', r'\1 = \2 - \3', line)
        elif line.startswith("times_dat"):
            line = re.sub(r'times_dat (\w+) = (.+) times (.+)', r'\1 = \2 * \3', line)
        elif line.startswith("divide_dat"):
            line = re.sub(r'divide_dat (\w+) = (.+) divide (.+)', r'\1 = \2 / \3', line)
        elif line.startswith("write_dat"):
            line = re.sub(r'write_dat "(.+)" into (\w+)', r'with open("\2.txt", "w") as f:\n    f.write("\1")', line)
        elif line.startswith("mandem_list"):
            line = re.sub(r'mandem_list (\w+)', r'\1 = []', line)
        elif line.startswith("add_to_mandem"):
            line = re.sub(r'add_to_mandem (\w+) value (.+)', r'\1.append(\2)', line)
        elif line.startswith("show_mandem"):
            line = re.sub(r'show_mandem (\w+)', r'print(\1)', line)
        elif line.startswith("badman_chance"):
            line = re.sub(r'badman_chance (\w+) = random between (\d+) and (\d+)', r'\1 = random.randint(\2, \3)', line)
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
chop num1 = 20
chop num2 = 5
sumting_light result1 = num1 plus num2
minus_dat result2 = num1 minus num2
times_dat result3 = num1 times num2
divide_dat result4 = num1 divide num2
big_ting "Math Results: " + str(result1) + ", " + str(result2) + ", " + str(result3) + ", " + str(result4)

mandem_list squad
add_to_mandem squad value "Tyrone"
add_to_mandem squad value "Jake"
show_mandem squad

badman_chance lucky_number = random between 1 and 10
big_ting "Your lucky number is: " + str(lucky_number)
"""

python_code = brogramming_to_python(brogramming_code)
print("Translated Python Code:\n")
print(python_code)

# Execute the converted Python code
exec(python_code)
