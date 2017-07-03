
"""
Using raw_input()
"""

lines = []
while True:
    try:
        lines.append(raw_input())
    except EOFError:
        lines.reverse()
        print lines
        break

"""
Using stdin
"""
from sys import stdin
lines = []
for line in stdin:
    lines.append(line.strip())

lines.reverse()
print(lines)
