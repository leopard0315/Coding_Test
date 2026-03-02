from collections import Counter

cx, cy = Counter(), Counter()

for _ in range(3):
    x, y = map(int, input().split())
    cx[x] += 1
    cy[y] += 1

x = [k for k, v in cx.items() if v == 1][0]
y = [k for k, v in cy.items() if v == 1][0]

print(x, y)