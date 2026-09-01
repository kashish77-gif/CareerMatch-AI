import json

from src.skill_extractor import extract_skills
from src.semantic_matcher import calculate_semantic_similarity


def load_jobs():

    with open(
        "data/jobs.json",
        "r",
        encoding="utf-8"
    ) as file:

        jobs = json.load(file)

    return jobs


def recommend_jobs(resume_text, resume_skills):

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

        # --------------------------------------------------
        # Skill Matching
        # --------------------------------------------------

        matched_skills = (
            resume_skills_lower &
            job_skills
        )

        if job_skills:

            skill_score = (
                len(matched_skills)
                / len(job_skills)
            ) * 100

        else:

            skill_score = 0


        # --------------------------------------------------
        # Semantic Matching
        # --------------------------------------------------

        job_text = (
            job["title"]
            + " "
            + job["description"]
            + " "
            + " ".join(job["skills"])
        )

        semantic_score = calculate_semantic_similarity(
            resume_text,
            job_text
        )


        # --------------------------------------------------
        # Recommendation Score
        # --------------------------------------------------

        recommendation_score = (
            (skill_score * 0.6)
            +
            (semantic_score * 0.4)
        )


        recommendations.append(
            {
                "title": job["title"],

                "description": job["description"],

                "score": recommendation_score,

                "skill_score": skill_score,

                "semantic_score": semantic_score,

                "matched_skills": sorted(
                    matched_skills
                )
            }
        )


    # --------------------------------------------------
    # Sort Jobs By Recommendation Score
    # --------------------------------------------------

    recommendations.sort(
        key=lambda job: job["score"],
        reverse=True
    )

    return recommendations