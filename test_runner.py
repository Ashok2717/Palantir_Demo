from webhook_ingest import ingest_stories_to_local_db
from chat_vector_search import search_chat_input
from score_checker import score_result
from ai_agent import semantic_authentication_agent
prior_auth_score = 0.0

# Sample stories to embed and ingest
# stories = [
#     {
#         "namespace": "story-greenlake",
#         "text": "When I was younger, my mom and I used to spend summer days biking around Green Lake near Seattle...",
#     },
#     {
#         "namespace": "story-attic-adventure",
#         "text": "Lina loved adventures. Every weekend, she would explore her grandmother’s big old house...",
#     }
# ]

stories = [
    {
        "namespace": "story-greenlake-2",
        "text": "A nostalgic reflection where the narrator reminisces about summer days spent biking with their mother around Green Lake, a scenic spot near Seattle. It’s a peaceful and heartfelt memory evoking a sense of warmth, nature, and bonding between parent and child.",
    },
    {
        "namespace": "story-attic-adventure-2",
        "text": "Lina, a curious and adventurous child, loves exploring. Every weekend she visits her grandmother’s large, old house and discovers new mysteries. The story sets up a tone of childhood excitement and exploration, focusing on imagination and weekend adventures.",
    }
]

# # Step 1: Ingest stories
# ingest_stories_to_local_db(stories)

# # Step 2: Provide chat input to test
# chat_input = "I love biking around lakes with my family during summers."
# chat_input =  "Lina loved adventures. Every weekend, she would explore her grandmother’s big old house."
# chat_input = "When I was younger, my mom and I used to spend summer days biking "
# chat_input = "A nostalgic reflection where the narrator reminisces about summer days spent biking with their mother around Green Lake, a scenic spot near Seattle. It’s a peaceful and heartfelt memory evoking a sense of warmth, nature, and bonding between parent and child."


chat_input = input("\nEnter your chat input: ")


# # Step 3: Search similar story
search_results = search_chat_input(chat_input)
# print("search_results:",search_results)

# # Step 4: Score the match
score = score_result(search_results)

# print("score::",score)

# Step 5: AI Agent Decision
decision, prior_auth_score = semantic_authentication_agent(score, prior_auth_score)


# Step 6: Print results
print("\n=============== Final Output ==============")

