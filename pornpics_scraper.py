import os
import argparse
import urllib.request

from helpers import get_html, get_dir_name
from progress import print_double_progress, print_single_progress

global_data = {
    "line_number": 0,
    "total_lines": 0,
    "total_steps": 0
}


def print_progress(progress):
    if global_data['line_number'] == 0:
        print_single_progress(
            progress=progress,
            total=global_data['total_steps'],
            prefix="IMAGES "
        )
    else:
        print_double_progress(
            progress1=global_data['line_number'],
            total1=global_data['total_lines'],
            prefix1="URLS ",
            progress2=progress,
            total2=global_data['total_steps'],
            prefix2="IMAGES ",
        )


def download_links_from_page(dir_name, items):
    i = 1

    os.makedirs(dir_name, exist_ok=True)
    global_data['total_steps'] = len(items)
    for item in items:
        href = item.find("a")['href']
        urllib.request.urlretrieve(href, dir_name + "/" + str(i).zfill(4) + ".jpg")

        print_progress(progress=i)

        i = i + 1


def process_page(url):
    html = get_html(url)

    image_list = html.find("ul", {"id": "tiles"})
    list_items = image_list.find_all("li")

    dirname = get_dir_name(url, html)

    download_links_from_page(dirname, list_items)

def process_file_with_urls(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]
        global_data['total_lines'] = len(lines)
        global_data['line_number'] = 1
        for line in lines:
            process_page(line)
            global_data['line_number'] = global_data['line_number'] + 1


def main():
    parser = argparse.ArgumentParser(description="PornPics scraper")
    parser.add_argument("url", nargs="?", help="PornPics gallery URL")
    parser.add_argument("--file", help="Path to file with URLs")

    args = parser.parse_args()

    if args.file:
        if not os.path.isfile(args.file):
            print("File does not exist.")
            return

        process_file_with_urls(args.file)
    elif args.url:
        process_page(args.url)
    else:
        print("Error: You need to specify URL or file path.")

if __name__ == "__main__":
    main()
