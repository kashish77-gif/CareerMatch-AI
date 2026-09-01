def calculate_ats_score(
    resume_text,
    sections,
    skills
):
    """
    Calculate a basic ATS-friendly resume score.
    """

    score = 0
    suggestions = []

    resume_text_lower = resume_text.lower()


    # --------------------------------------------------
    # Resume Length
    # --------------------------------------------------

    word_count = len(
        resume_text.split()
    )

    if 300 <= word_count <= 1000:

        score += 20

    elif word_count < 300:

        score += 10

        suggestions.append(
            "Your resume appears too short. "
            "Add relevant projects, skills, education, "
            "or experience details."
        )

    else:

        score += 10

        suggestions.append(
            "Your resume may contain too much information. "
            "Remove unnecessary content and keep the resume concise."
        )


    # --------------------------------------------------
    # Important Sections
    # --------------------------------------------------

    section_names = {
        section.lower().strip()
        for section in sections.keys()
    }


    important_sections = [
        "summary",
        "skills",
        "education",
        "projects"
    ]


    section_score = 0

    for section in important_sections:

        if section in section_names:

            section_score += 10

        else:

            suggestions.append(
                f"Consider adding a {section} section "
                "to improve resume structure."
            )


    score += section_score


    # --------------------------------------------------
    # Technical Skills
    # --------------------------------------------------

    if len(skills) >= 5:

        score += 15

    elif len(skills) > 0:

        score += 8

        suggestions.append(
            "Add more relevant technical skills "
            "that you have actually used."
        )

    else:

        suggestions.append(
            "Add a clear technical skills section."
        )


    # --------------------------------------------------
    # Contact Information
    # --------------------------------------------------

    contact_keywords = [
        "email",
        "@",
        "phone",
        "linkedin",
        "github"
    ]


    contact_count = sum(
        keyword in resume_text_lower
        for keyword in contact_keywords
    )


    if contact_count >= 3:

        score += 10

    elif contact_count >= 1:

        score += 5

        suggestions.append(
            "Make sure your resume contains "
            "professional contact information such as "
            "email, phone, LinkedIn, and GitHub."
        )

    else:

        suggestions.append(
            "Add professional contact information "
            "including email, phone, LinkedIn, and GitHub."
        )


    # --------------------------------------------------
    # Final Score
    # --------------------------------------------------

    score = min(
        score,
        100
    )


    return score, suggestions