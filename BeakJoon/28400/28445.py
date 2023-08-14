import sys

dad_body, dad_tail = sys.stdin.readline().split()
mom_body, mom_tail = sys.stdin.readline().split()

colors = [dad_body, dad_tail, mom_body, mom_tail]
combinations = [(a, b) for a in colors for b in colors]

unique_combinations = sorted(set(combinations))

for body, tail in unique_combinations:
    print(body, tail)
