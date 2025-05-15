# def score_result(search_results):
#     """
#     Takes ChromaDB query results and returns a similarity score for the top match.
#     """
#     distances = search_results.get("distances", [[]])
    
#     if not distances[0]:
#         return 0.0

#     top_distance = distances[0][0]
#     # Convert distance to similarity score (0 to 1 range; higher is better)
#     score = 1 / (1 + top_distance)
#     return round(score, 4)



def score_result(search_results):
    distances = search_results.get("distances", [[]])
    
    if not distances[0]:
        return 0.0

    top_distance = distances[0][0]

    # Convert L2 distance to cosine similarity (for unit-normalized vectors)
    cosine_score = 1 - 0.5 * (top_distance ** 2)
    return round(cosine_score, 4)
