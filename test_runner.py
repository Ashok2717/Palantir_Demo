from webhook_ingest import ingest_stories_to_local_db
from chat_vector_search import search_chat_input
from score_checker import score_result
# from ai_agent import ask_agent

# Sample stories to embed and ingest
stories = [
    {
        "namespace": "story-greenlake",
        "text": "When I was younger, my mom and I used to spend summer days biking around Green Lake near Seattle...",
    },
    {
        "namespace": "story-attic-adventure",
        "text": "Lina loved adventures. Every weekend, she would explore her grandmother’s big old house...",
    }
]

# Step 1: Ingest stories
ingest_stories_to_local_db(stories)

# # Step 2: Provide chat input to test
# # chat_input = "I love biking around lakes with my family during summers."
chat_input =  "Tell me about Lina's adventures."
# chat_input = "When I was younger, my mom and I used to spend summer days biking around Green Lake near Seattle..."

# Step 3: Search similar story
search_results = search_chat_input(chat_input)
print("search_results:",search_results)

# Step 4: Score the match
score = score_result(chat_input, search_results)

print("score::",score)

# # Step 5: AI generates explanation
# ai_response = ask_agent(chat_input, search_results)

# # Step 6: Print results
# print("\n=== Final Output ===")
# print(f"User Input: {chat_input}")
# print(f"Top Match: {search_results[0]['metadata']['text'] if search_results else 'No match'}")
# print(f"Similarity Score: {score}")
# print(f"AI Agent Says: {ai_response}")
