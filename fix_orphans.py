import os
import re

content_files = [f for f in os.listdir("content") if f.endswith(".md") and f != "INDEX.md"]

with open("content/INDEX.md", "r", encoding="utf-8") as f:
    index_content = f.read()

link_pattern = re.compile(r'\[\[(.*?)\]\]')
links_in_index = []
for match in link_pattern.finditer(index_content):
    link = match.group(1).split('|')[0]
    links_in_index.append(link)

orphaned_files = [f for f in content_files if f[:-3] not in links_in_index]

print("\n--- Orphaned Files ---")
for file in orphaned_files:
    print(file)
