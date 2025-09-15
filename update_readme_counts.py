import os
import re

README_PATH = 'README.md'
DATA_DIR = 'data'

PREFIXES = ['Q', 'DA', 'SA', 'WA']


def count_files_by_prefix(data_dir, prefixes):
    counts = {prefix: 0 for prefix in prefixes}
    pattern = re.compile(r'^(Q|DA|SA|WA).*\\.txt$', re.IGNORECASE)
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.lower().endswith('.txt'):
                for prefix in prefixes:
                    if file.upper().startswith(prefix):
                        counts[prefix] += 1
                        break
    return counts


def update_readme(readme_path, counts):
    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find or create the section marker
    start_marker = '<!-- FILE_COUNTS_START -->\n'
    end_marker = '<!-- FILE_COUNTS_END -->\n'
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if line == start_marker:
            start_idx = i
        if line == end_marker:
            end_idx = i

    counts_md = [start_marker]
    counts_md.append('## File Counts in data/\n')
    for prefix in PREFIXES:
        if prefix == 'Q':
            counts_md.append(f'- {prefix}*.txt (Questions): {counts[prefix]}\n')
        elif prefix == 'DA':
            counts_md.append(f'- {prefix}*.txt (Dumb Answers): {counts[prefix]}\n')
        elif prefix == 'SA':
            counts_md.append(f'- {prefix}*.txt (Smart Answers): {counts[prefix]}\n')
        elif prefix == 'WA':
            counts_md.append(f'- {prefix}*.txt (Wrong Answers): {counts[prefix]}\n')
    counts_md.append(end_marker)

    if start_idx is not None and end_idx is not None:
        # Replace old section
        new_lines = lines[:start_idx] + counts_md + lines[end_idx+1:]
    else:
        # Append section at the end
        if not lines[-1].endswith('\n'):
            lines[-1] += '\n'
        new_lines = lines + ['\n'] + counts_md

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)


def main():
    counts = count_files_by_prefix(DATA_DIR, PREFIXES)
    update_readme(README_PATH, counts)
    print('README.md updated with file counts.')


if __name__ == '__main__':
    main()
