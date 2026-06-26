from ddgs import DDGS


def discover_urls(query, max_results=5):

    urls = []

    with DDGS() as ddgs:

        results = ddgs.text(
            query,
            max_results=max_results
        )

        for result in results:

            if "href" in result:
                urls.append(result["href"])

    return urls


if __name__ == "__main__":

    query = input("Search: ")

    urls = discover_urls(query)

    for url in urls:
        print(url)