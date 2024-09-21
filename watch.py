import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)\"",s):
    #url = re.search(r"(?:.+) src=\"https?://(?:www\.)?youtube\.com/embed/(.+)\"(?:.+)",s) it takes until the last one [a-zA-Z0-9_-]+

        return f"https://youtu.be/{url.group(1)}"


if __name__ == "__main__":
    main()
