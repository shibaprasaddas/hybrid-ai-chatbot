# Lightweight scoring engine


def calculate_score(user_input, patterns):
    score = 0

    words = user_input.split()

    for pattern in patterns:
        pattern_words = pattern.lower().split()

        for word in words:
            if word in pattern_words:
                score += 1

    return score
