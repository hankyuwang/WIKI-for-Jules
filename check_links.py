import os
import re

content_dir = 'content'
files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
file_basenames = [f[:-3] for f in files]

broken_links = []
for file in files:
    filepath = os.path.join(content_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    links = re.findall(r'\[\[(.*?)\]\]', content)
    for link in links:
        link_target = link.split('|')[0].split('#')[0]
        if link_target and link_target not in file_basenames:
            broken_links.append((file, link_target))

for f, t in broken_links:
    print(f"Broken link in {f}: {t}")
