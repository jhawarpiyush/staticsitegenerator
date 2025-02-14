import os
import pathlib

from block_markdown_split import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 heading found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown_content = f.read()

    with open(template_path, "r") as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    full_html = template_content.replace(
        '{{ Title }}', title).replace('{{ Content }}', html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise OSError('Content directory not found')
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    print(f"Generating pages from {dir_path_content} with {template_path} in {dest_dir_path}")
    dir_paths = os.listdir(dir_path_content)
    for path in dir_paths:
        src_item = os.path.join(dir_path_content, path)
        dest_item = os.path.join(dest_dir_path, path)

        if os.path.isfile(src_item):
            dest_item = dest_item.replace(".md", ".html")
            generate_page(src_item, template_path, dest_item)
        elif os.path.isdir(src_item):
            os.makedirs(dest_item, exist_ok=True)
            generate_pages_recursive(src_item, template_path, dest_item)
    
