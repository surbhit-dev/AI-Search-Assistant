def create_chunks(content):

    chunk_size = 500

    chunks = []

    for i in range(
        0,
        len(content),
        chunk_size
    ):

        chunk = content[
            i:i + chunk_size
        ]

        chunks.append(chunk)

    return chunks