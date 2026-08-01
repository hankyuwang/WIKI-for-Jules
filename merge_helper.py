import subprocess
import os
import sys

def has_frontmatter(lines):
    return any(line.strip() == "---" for line in lines)

def merge_parts(head_lines, incoming_lines):
    has_fm_head = has_frontmatter(head_lines)
    has_fm_inc = has_frontmatter(incoming_lines)

    if has_fm_head and has_fm_inc:
        if len(head_lines) >= len(incoming_lines):
            return head_lines
        else:
            return incoming_lines
    elif has_fm_head:
        return head_lines
    elif has_fm_inc:
        return incoming_lines
    else:
        merged = list(head_lines)
        head_set = set(l.strip() for l in head_lines if l.strip())

        for line in incoming_lines:
            l_strip = line.strip()
            if not l_strip:
                continue
            if l_strip not in head_set:
                merged.append(line)
                head_set.add(l_strip)

        return merged

def resolve_conflict_file(filepath):
    print(f"Resolving conflicts in {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    resolved_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("<<<<<<<"):
            head_part = []
            incoming_part = []
            i += 1
            # Read head part until =======
            while i < len(lines) and not lines[i].startswith("======="):
                head_part.append(lines[i])
                i += 1
            # Skip =======
            if i < len(lines) and lines[i].startswith("======="):
                i += 1
            # Read incoming part until >>>>>>>
            while i < len(lines) and not lines[i].startswith(">>>>>>>"):
                incoming_part.append(lines[i])
                i += 1
            # Skip >>>>>>>
            if i < len(lines) and lines[i].startswith(">>>>>>>"):
                i += 1

            # Merge the parts
            merged_part = merge_parts(head_part, incoming_part)
            resolved_lines.extend(merged_part)
        else:
            resolved_lines.append(line)
            i += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(resolved_lines) + "\n")

def get_unmerged_branches():
    try:
        out = subprocess.check_output(["git", "branch", "-r", "--no-merged", "main"]).decode("utf-8")
        branches = []
        for line in out.strip().split("\n"):
            line = line.strip()
            if line and "origin/HEAD" not in line and "origin/main" not in line:
                branches.append(line)
        return sorted(branches)
    except Exception as e:
        print(f"Error getting branches: {e}")
        return []

def main():
    status = subprocess.check_output(["git", "status", "--porcelain"]).decode("utf-8").strip()
    status_lines = [l for l in status.split("\n") if l and not l.endswith("merge_helper.py")]
    if status_lines:
        print("Error: working directory not clean.")
        print("\n".join(status_lines))
        sys.exit(1)

    branches = get_unmerged_branches()
    print(f"Found {len(branches)} unmerged branches to process.")

    success_count = 0
    fail_count = 0

    for idx, b in enumerate(branches, 1):
        print(f"\n[{idx}/{len(branches)}] Merging branch {b}...")
        # Try git merge
        res = subprocess.run(["git", "merge", "--no-ff", "--no-commit", b], capture_output=True, text=True)

        if res.returncode == 0:
            print(f"Clean merge for {b}")
            subprocess.run(["git", "commit", "--no-edit"], check=True)
            success_count += 1
        else:
            print(f"Conflict encountered when merging {b}")
            status_lines = subprocess.check_output(["git", "status", "--porcelain"]).decode("utf-8").strip().split("\n")
            conflicted_files = []
            for line in status_lines:
                if not line:
                    continue
                if line[0] in "UDA" and line[1] in "UDA":
                    conflicted_files.append(line[3:].strip())

            print(f"Conflicted files: {conflicted_files}")

            try:
                for f in conflicted_files:
                    if os.path.exists(f):
                        resolve_conflict_file(f)
                        subprocess.run(["git", "add", f], check=True)
                    else:
                        print(f"Warning: File {f} does not exist, skipping manual resolution.")

                subprocess.run(["git", "commit", "-m", f"Merge remote-tracking branch {b} with conflict resolution"], check=True)
                print(f"Successfully resolved conflicts and merged {b}")
                success_count += 1
            except Exception as ex:
                print(f"Failed to resolve conflicts for {b}: {ex}")
                print("Aborting merge...")
                subprocess.run(["git", "merge", "--abort"], check=True)
                fail_count += 1

    print(f"\nMerge session complete!")
    print(f"Successfully merged: {success_count}/{len(branches)}")
    print(f"Failed: {fail_count}")

if __name__ == "__main__":
    main()
