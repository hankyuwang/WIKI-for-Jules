import os
import re

def analyze_wiki():
    content_dir = 'content/'
    index_file = os.path.join(content_dir, 'INDEX.md')

    with open(index_file, 'r', encoding='utf-8') as f:
        index_content = f.read()

    # Find all [[WikiLinks]] in INDEX.md
    wiki_links_in_index = set(re.findall(r'\[\[(.*?)\]\]', index_content))

    all_files = os.listdir(content_dir)
    md_files = [f for f in all_files if f.endswith('.md') and f != 'INDEX.md']
    md_filenames = set([f[:-3] for f in md_files])

    orphaned = md_filenames - wiki_links_in_index
    dead_links = wiki_links_in_index - md_filenames

    # Check for short content (e.g., less than 500 characters) indicating it might need expansion
    short_files = []
    missing_prerequisites = []
    missing_frontmatter = []

    for f in md_files:
        filepath = os.path.join(content_dir, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

            if len(content) < 1500:
                short_files.append(f)

            if "## Prerequisites" not in content and "## 先備知識" not in content:
                missing_prerequisites.append(f)

            if not content.startswith("---"):
                missing_frontmatter.append(f)

    report = []
    report.append("# 知識庫巡檢報告\n")

    if orphaned:
        report.append("## 孤立的節點 (在 content/ 但未被 INDEX.md 連結)")
        for o in orphaned:
            report.append(f"- [ ] `{o}.md`")
        report.append("")

    if dead_links:
        report.append("## 失效的連結 (在 INDEX.md 中，但不存在於 content/ 中)")
        for d in dead_links:
            report.append(f"- [ ] `[[{d}]]`")
        report.append("")

    if short_files:
        report.append("## 內容過少需要補充的節點 (字數 < 1500 字)")
        for sf in short_files[:10]: # Just list top 10 to keep it manageable
            report.append(f"- [ ] `{sf}`")
        if len(short_files) > 10:
            report.append(f"- (還有 {len(short_files) - 10} 個檔案...)")
        report.append("")

    if missing_prerequisites:
        report.append("## 缺少 '先備知識' (Prerequisites) 區塊的節點")
        for mp in missing_prerequisites[:10]:
            report.append(f"- [ ] `{mp}`")
        if len(missing_prerequisites) > 10:
            report.append(f"- (還有 {len(missing_prerequisites) - 10} 個檔案...)")
        report.append("")

    if missing_frontmatter:
        report.append("## 缺少 YAML Frontmatter 的節點")
        for mf in missing_frontmatter[:10]:
            report.append(f"- [ ] `{mf}`")
        if len(missing_frontmatter) > 10:
            report.append(f"- (還有 {len(missing_frontmatter) - 10} 個檔案...)")
        report.append("")

    return "\n".join(report), short_files[:2] # Return up to 2 short files to expand dynamically

report_text, targets = analyze_wiki()

os.makedirs('outputs', exist_ok=True)
with open('outputs/inspection_report.md', 'w', encoding='utf-8') as f:
    f.write(report_text)

print(report_text)
print("\n--- Targets for virtual team expansion ---")
for t in targets:
    print(t)
