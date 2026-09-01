def calculate_skill_match(resume_skills, job_skills):
    """
    Compare resume skills with job-required skills.
    """

    # Normalize resume skills
    resume_skills_lower = {
        skill.strip().lower()
        for skill in resume_skills
        if skill.strip()
    }

    # Normalize job skills
    job_skills_lower = {
        skill.strip().lower()
        for skill in job_skills
        if skill.strip()
    }

    # Find matching skills
    matched_skills = (
        resume_skills_lower &
        job_skills_lower
    )

    # Find missing skills
    missing_skills = (
        job_skills_lower -
        resume_skills_lower
    )

    # Calculate score
    if not job_skills_lower:

        match_score = 0

    else:

        match_score = (
            len(matched_skills)
            / len(job_skills_lower)
        ) * 100

    return (
        matched_skills,
        missing_skills,
        match_score
    )