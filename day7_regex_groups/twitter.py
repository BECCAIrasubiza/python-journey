
import re


def main():
    url = input("URL: ").strip()
    print("re.sub way:   ", username_sub(url))
    print("re.search way:", username_search(url))


def username_sub(url):
    return re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)


def username_search(url):
    if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
        return matches.group(1)
    return None


if __name__ == "__main__":
    main()
