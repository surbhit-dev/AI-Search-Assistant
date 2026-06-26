STOP_WORDS = {
    "what",
    "is",
    "the",
    "a",
    "an",
    "of",
    "in",
    "on",
    "now"
}


def score_content(query, content):

    query_words = query.lower().split()
    filtered_words = []

    content = content.lower()

    score = 0

    for word in query_words:
        if word not in STOP_WORDS:
            filtered_words.append(word)

    for word in filtered_words:
        if word in content:
            score += content.count(word)

    return score