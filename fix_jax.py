with open('content/JAX.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
found_first_practices = False
for line in lines:
    if line.strip() == '## 與硬體加速器的適配最佳實踐':
        if not found_first_practices:
            found_first_practices = True
            new_lines.append(line)
        else:
            # Skip the duplicated part
            break
    else:
        new_lines.append(line)

with open('content/JAX.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
