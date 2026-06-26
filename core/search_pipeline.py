from core.url_discovery import discover_urls
from core.content_extractor import extract_content
from core.ranker import score_content
from core.response_generator import generate_response
from core.chunker import create_chunks


def run_search(query):

    urls = discover_urls(query)

    all_chunks = []

    for url in urls:

        data = extract_content(url)

        if data is None:
            continue

        chunks = create_chunks(
            data["content"]
        )

        for chunk in chunks:

            score = score_content(
                query,
                chunk
            )

            all_chunks.append({

                "chunk": chunk,
                "score": score,
                "url": data["url"],
                "title": data["title"]

            })

    all_chunks.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    answer = generate_response(
        query,
        all_chunks
    )

    return {
        "answer": answer,
        "sources": all_chunks[:5]
    }