def score_result(chat_input, search_results):
    distances, indices = search_results

    # Check if at least one valid index was found
    if indices[0][0] == -1:
        return 0

    # Score is inverse of distance (lower distance = better match)
    # You might want to normalize or cap this
    score = distances[0][0]
    return round(1 / (1 + score), 4)  # Convert L2 distance to a similarity-like score
