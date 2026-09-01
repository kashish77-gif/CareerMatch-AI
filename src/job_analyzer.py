def extract_job_sections(job_description):
    """
    Extract required and preferred skills
    from a job description.
    """

    text = job_description.lower()

    required_skills = []
    preferred_skills = []

    required_start = text.find("required skills:")
    preferred_start = text.find("preferred skills:")

    if required_start != -1:

        if preferred_start != -1:

            required_text = job_description[
                required_start + len("required skills:"):
                preferred_start
            ]

        else:

            required_text = job_description[
                required_start + len("required skills:"):
            ]

        required_skills = required_text.strip()


    if preferred_start != -1:

        preferred_text = job_description[
            preferred_start + len("preferred skills:"):
        ]

        preferred_skills = preferred_text.strip()


    return required_skills, preferred_skills