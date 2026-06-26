import requests
from bs4 import BeautifulSoup


def extract_content(url):

    try:

        response = requests.get(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/137.0.0.0 Safari/537.36"
                )
            },
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = (
            soup.title.text
            if soup.title
            else "No Title"
        )

        content = ""

        for h in soup.find_all(
            ["h1", "h2"]
        )[:5]:

            content += (
                h.get_text(
                    " ",
                    strip=True
                ) + "\n"
            )

        for p in soup.find_all(
            "p"
        )[:10]:

            content += (
                p.get_text(
                    " ",
                    strip=True
                ) + "\n"
            )

        return {
            "url": url,
            "title": title,
            "content": content
        }

    except Exception as e:

        print(
            f"Failed to extract: {url}"
        )

        print(
            f"Reason: {e}"
        )

        return None