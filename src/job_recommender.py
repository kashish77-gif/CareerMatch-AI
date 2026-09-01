import json


def load_jobs():

    with open(
        "data/jobs.json",
        "r",
        encoding="utf-8"
    ) as file:

        jobs = json.load(file)

    return jobs


def recommend_jobs(resume_skills):

    jobs = load_jobs()

    resume_skills_lower = {
        skill.lower()
        for skill in resume_skills
    }

    recommendations = []

    for job in jobs:

        job_skills = {
            skill.lower()
            for skill in job["skills"]
        }

        matched_skills = (
            resume_skills_lower &
            job_skills
        )

        if job_skills:

            match_score = (
                len(matched_skills)
                / len(job_skills)
            ) * 100

        else:

            match_score = 0

        recommendations.append(
            {
                "title": job["title"],
                "description": job["description"],
                "score": match_score,
                "matched_skills": sorted(
                    matched_skills
                )
            }
        )

    recommendations.sort(
        key=lambda job: job["score"],
        reverse=True
    )

    return recommendations