#!/usr/bin/env python3

from pathlib import Path
import re

docs = {
    "0-add.py": "Return the sum of two floats.",
    "1-concat.py": "Concatenate two strings.",
    "2-floor.py": "Return the floor of a float.",
    "3-to_str.py": "Return the string representation of a float.",
    "5-sum_list.py": "Return the sum of a list of floats.",
    "6-sum_mixed_list.py": "Return the sum of a list of integers and floats.",
    "7-to_kv.py": "Return a tuple containing a string and the square of a number.",
    "8-make_multiplier.py": "Return a function that multiplies a float by a multiplier.",
    "9-element_length.py": "Return a list containing each element and its length.",
}

for filename, docstring in docs.items():
    path = Path(filename)

    if not path.exists():
        print(f"Skipping {filename}: file not found")
        continue

    content = path.read_text()

    pattern = r'(^def\s+\w+\([^)]*\)(?:\s*->\s*[^:]+)?\s*:\s*\n)(?!\s+""")'

    new_content, count = re.subn(
        pattern,
        lambda match: match.group(1) + f'    """{docstring}"""\n',
        content,
        count=1,
        flags=re.MULTILINE,
    )

    if count:
        path.write_text(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No change needed: {filename}")

# 4-define_variables.py
print("Done.")
