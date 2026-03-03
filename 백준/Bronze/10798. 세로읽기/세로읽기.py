lines = [input() for _ in range(5)]
max_len = max(len(line) for line in lines)

result = []
for col in range(max_len):
    for row in range(5):
        if col < len(lines[row]):
            result.append(lines[row][col])

print(''.join(result))