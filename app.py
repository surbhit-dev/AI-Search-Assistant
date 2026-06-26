from core.search_pipeline import run_search

query = input("Ask something: ")

result = run_search(query)

print(result["answer"])