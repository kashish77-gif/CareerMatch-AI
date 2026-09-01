def generate_skill_gap_report(
    required_missing,
    preferred_missing
):
    """
    Generate recommendations based on
    missing required and preferred skills.
    """

    recommendations = []

    if required_missing:

        for skill in sorted(required_missing):

            recommendations.append(
                f"Learn or strengthen {skill} because it is "
                f"a required skill for this job."
            )

    if preferred_missing:

        for skill in sorted(preferred_missing):

            recommendations.append(
                f"Consider learning {skill} to improve "
                f"your competitiveness for this role."
            )

    if not recommendations:

        recommendations.append(
            "Your resume covers the identified job skills well."
        )

    return recommendations