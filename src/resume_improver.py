def generate_resume_improvement_suggestions(
    sections,
    skills,
    required_missing,
    preferred_missing
):
    """
    Generate job-specific suggestions
    for improving a resume.
    """

    suggestions = []

    section_names = {
        section.lower().strip()
        for section in sections.keys()
    }


    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    summary_text = sections.get(
        "summary",
        ""
    ).strip()

    if "summary" not in section_names:

        suggestions.append(
            "Add a professional summary that clearly "
            "highlights your technical skills, projects, "
            "and career objective."
        )

    elif len(summary_text) < 80:

        suggestions.append(
            "Improve your professional summary by adding "
            "more specific information about your technical "
            "skills, projects, and career interests."
        )


    # --------------------------------------------------
    # Skills
    # --------------------------------------------------

    if "skills" not in section_names or not skills:

        suggestions.append(
            "Add a dedicated technical skills section "
            "containing technologies relevant to the target job."
        )

    elif len(skills) < 5:

        suggestions.append(
            "Expand your technical skills section with "
            "relevant tools, programming languages, frameworks, "
            "and technologies you have actually worked with."
        )


    # --------------------------------------------------
    # Projects
    # --------------------------------------------------

    projects_text = sections.get(
        "projects",
        ""
    ).strip()

    if "projects" not in section_names:

        suggestions.append(
            "Add relevant academic or personal projects. "
            "Mention the problem, technologies used, "
            "and your contribution."
        )

    elif len(projects_text) < 100:

        suggestions.append(
            "Add more details to your projects. "
            "Explain what you built, which technologies "
            "you used, and what results you achieved."
        )


    # --------------------------------------------------
    # Education
    # --------------------------------------------------

    if "education" not in section_names:

        suggestions.append(
            "Add your educational qualifications including "
            "degree, institution, and graduation year."
        )


    # --------------------------------------------------
    # Experience
    # --------------------------------------------------

    experience_text = sections.get(
        "experience",
        ""
    ).strip()

    if "experience" not in section_names:

        suggestions.append(
            "If you have internships, training, freelance "
            "work, or relevant practical experience, include "
            "them in your resume."
        )

    elif len(experience_text) < 100:

        suggestions.append(
            "Strengthen your experience section by describing "
            "your responsibilities, technologies used, "
            "and measurable results."
        )


    # --------------------------------------------------
    # Required Skills
    # --------------------------------------------------

    if required_missing:

        missing_required = ", ".join(
            sorted(required_missing)
        )

        suggestions.append(
            "Prioritize learning or demonstrating these "
            "missing required skills: "
            + missing_required
            + "."
        )


    # --------------------------------------------------
    # Preferred Skills
    # --------------------------------------------------

    if preferred_missing:

        missing_preferred = ", ".join(
            sorted(preferred_missing)
        )

        suggestions.append(
            "Consider developing these preferred skills "
            "to strengthen your profile: "
            + missing_preferred
            + "."
        )


    # --------------------------------------------------
    # Achievement-Oriented Resume
    # --------------------------------------------------

    all_resume_text = " ".join(
        sections.values()
    ).lower()

    achievement_words = [
        "increased",
        "improved",
        "reduced",
        "achieved",
        "developed",
        "implemented",
        "optimized",
        "%",
        "accuracy"
    ]

    has_achievements = any(
        word in all_resume_text
        for word in achievement_words
    )

    if not has_achievements:

        suggestions.append(
            "Add measurable achievements wherever possible. "
            "Use numbers, percentages, accuracy scores, "
            "or other results to show the impact of your work."
        )


    # --------------------------------------------------
    # Action Verbs
    # --------------------------------------------------

    weak_words = [
        "responsible for",
        "worked on",
        "helped with",
        "did"
    ]

    has_weak_phrasing = any(
        phrase in all_resume_text
        for phrase in weak_words
    )

    if has_weak_phrasing:

        suggestions.append(
            "Replace weak phrases such as 'worked on' or "
            "'responsible for' with strong action verbs such "
            "as developed, implemented, analyzed, designed, "
            "or optimized."
        )


    # --------------------------------------------------
    # Final Check
    # --------------------------------------------------

    if not suggestions:

        suggestions.append(
            "Your resume structure and identified skills "
            "are well aligned with the target job. "
            "Continue improving your achievements and "
            "quantifying your project results."
        )


    return suggestions