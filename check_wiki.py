import os
import re

content_dir = 'content'
index_path = os.path.join(content_dir, 'INDEX.md')

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract all links from INDEX.md
wiki_links_in_index = set(re.findall(r'\[\[(.*?)\]\]', index_content))
wiki_links_in_index = {link.split('|')[0] for link in wiki_links_in_index}

# Get all .md files in content/
md_files = {f[:-3] for f in os.listdir(content_dir) if f.endswith('.md') and f != 'INDEX.md'}

# Find orphaned files (in content/ but not in INDEX.md)
orphaned_files = md_files - wiki_links_in_index

# Find dead links (in INDEX.md but not in content/)
dead_links = wiki_links_in_index - md_files

print(f"Orphaned files ({len(orphaned_files)}):")
for f in sorted(orphaned_files):
    print(f" - {f}")

print(f"\nDead links ({len(dead_links)}):")
for l in sorted(dead_links):
    print(f" - {l}")
