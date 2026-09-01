def calculate_overall_score(skill_score, semantic_score):
    """
    Calculate the overall resume-job match score.
    """

    overall_score = (
        (skill_score * 0.60) +
        (semantic_score * 0.40)
    )

    return overall_score