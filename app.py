import streamlit as st

from src.resume_parser import extract_resume_text
from src.section_extractor import extract_sections
from src.skill_extractor import extract_skills
from src.matcher import calculate_skill_match
from src.semantic_matcher import calculate_semantic_similarity
from src.score_calculator import calculate_overall_score
from src.job_analyzer import extract_job_sections
from src.skill_gap import generate_skill_gap_report
from src.resume_improver import generate_resume_improvement_suggestions
from src.job_recommender import recommend_jobs
from src.ats_analyzer import calculate_ats_score
from src.report_generator import generate_report


st.set_page_config(
    page_title="CareerMatch AI",
    page_icon="💼",
    layout="wide"
)


# --------------------------------------------------
# Custom Styling
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 18px;
        color: #777;
        margin-bottom: 25px;
    }

    .score-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        text-align: center;
        margin-bottom: 15px;
    }

    .score-number {
        font-size: 32px;
        font-weight: 700;
    }

    .section-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">CareerMatch AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered resume analysis and job matching platform</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# Input Section
# --------------------------------------------------

input_col1, input_col2 = st.columns(2)


with input_col1:

    st.subheader("Resume")

    resume = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx"],
        help="Maximum file size: 5 MB"
    )

    MAX_FILE_SIZE = 5 * 1024 * 1024

    if resume is not None and resume.size > MAX_FILE_SIZE:
        st.error(
            "Resume file is too large. Please upload a file smaller than 5 MB."
        )
        resume = None

with input_col2:

    st.subheader("Job Description")

    job_description = st.text_area(
        "Paste the job description here",
        height=220,
        placeholder="Paste the complete job description..."
    )


st.write("")


# --------------------------------------------------
# Analyze Button
# --------------------------------------------------

analyze = st.button(
    "Analyze Match",
    use_container_width=True
)


if analyze:

    if resume is None:

        st.warning("Please upload your resume.")

    elif not job_description.strip():

        st.warning("Please enter the job description.")

    else:

        # --------------------------------------------------
        # Extract Resume Text
        # --------------------------------------------------

        with st.spinner("Analyzing your resume..."):

            resume_text = extract_resume_text(resume)


        if not resume_text.strip():

            st.error(
                "Could not extract text from the resume."
            )

        else:

            # --------------------------------------------------
            # Extract Resume Sections
            # --------------------------------------------------

            sections = extract_sections(resume_text)


            # --------------------------------------------------
            # Extract Resume Skills
            # --------------------------------------------------

            skills = extract_skills(
                sections["skills"]
            )


            # --------------------------------------------------
            # ATS Analysis
            # --------------------------------------------------

            ats_score, ats_suggestions = calculate_ats_score(
                resume_text,
                sections,
                skills
            )


            # --------------------------------------------------
            # Extract Job Skills
            # --------------------------------------------------

            job_skills = extract_skills(
                job_description
            )


            # --------------------------------------------------
            # Extract Required and Preferred Skills
            # --------------------------------------------------

            required_text, preferred_text = (
                extract_job_sections(
                    job_description
                )
            )


            required_skills = extract_skills(
                required_text
            )

            preferred_skills = extract_skills(
                preferred_text
            )


            # --------------------------------------------------
            # Overall Skill Matching
            # --------------------------------------------------

            matched_skills, missing_skills, skill_score = (
                calculate_skill_match(
                    skills,
                    job_skills
                )
            )


            # --------------------------------------------------
            # Required Skill Matching
            # --------------------------------------------------

            required_matched, required_missing, required_score = (
                calculate_skill_match(
                    skills,
                    required_skills
                )
            )


            # --------------------------------------------------
            # Preferred Skill Matching
            # --------------------------------------------------

            preferred_matched, preferred_missing, preferred_score = (
                calculate_skill_match(
                    skills,
                    preferred_skills
                )
            )


            # --------------------------------------------------
            # Semantic Matching
            # --------------------------------------------------

            with st.spinner("Calculating semantic similarity..."):

                semantic_score = calculate_semantic_similarity(
                    resume_text,
                    job_description
                )


            # --------------------------------------------------
            # Weighted Skill Score
            # --------------------------------------------------

            if required_skills and preferred_skills:

                weighted_skill_score = (
                    (required_score * 0.75)
                    +
                    (preferred_score * 0.25)
                )

            elif required_skills:

                weighted_skill_score = required_score

            elif preferred_skills:

                weighted_skill_score = preferred_score

            else:

                weighted_skill_score = 0


            # --------------------------------------------------
            # Overall Score
            # --------------------------------------------------

            overall_score = calculate_overall_score(
                weighted_skill_score,
                semantic_score
            )


            # --------------------------------------------------
            # Skill Gap Analysis
            # --------------------------------------------------

            recommendations = generate_skill_gap_report(
                required_missing,
                preferred_missing
            )


            # --------------------------------------------------
            # Resume Improvement
            # --------------------------------------------------

            resume_suggestions = (
                generate_resume_improvement_suggestions(
                    sections,
                    skills,
                    required_missing,
                    preferred_missing
                )
            )


            # --------------------------------------------------
            # Job Recommendations
            # --------------------------------------------------

            with st.spinner("Finding suitable jobs..."):

                job_recommendations = recommend_jobs(
                    resume_text,
                    skills
                )


            st.success(
                "Resume analysis completed successfully."
            )


            # ==================================================
            # DASHBOARD OVERVIEW
            # ==================================================

            st.divider()

            st.header("Match Overview")


            overview_col1, overview_col2, overview_col3, overview_col4 = (
                st.columns(4)
            )


            with overview_col1:

                st.metric(
                    "Overall Match",
                    f"{overall_score:.1f}%"
                )


            with overview_col2:

                st.metric(
                    "Skill Match",
                    f"{skill_score:.1f}%"
                )


            with overview_col3:

                st.metric(
                    "Semantic Match",
                    f"{semantic_score:.1f}%"
                )


            with overview_col4:

                st.metric(
                    "ATS Score",
                    f"{ats_score:.1f}%"
                )


            # ==================================================
            # SCORE BREAKDOWN
            # ==================================================

            st.divider()

            st.header("Score Breakdown")


            score_col1, score_col2 = st.columns(2)


            with score_col1:

                st.write("Skill Match")

                st.progress(
                    min(max(int(skill_score), 0), 100)
                )

                st.write(
                    f"{skill_score:.1f}%"
                )


                st.write("Semantic Similarity")

                st.progress(
                    min(max(int(semantic_score), 0), 100)
                )

                st.write(
                    f"{semantic_score:.1f}%"
                )


            with score_col2:

                st.write("ATS Compatibility")

                st.progress(
                    min(max(int(ats_score), 0), 100)
                )

                st.write(
                    f"{ats_score:.1f}%"
                )


                st.write("Required Skill Match")

                st.progress(
                    min(max(int(required_score), 0), 100)
                )

                st.write(
                    f"{required_score:.1f}%"
                )


            # ==================================================
            # RESUME INFORMATION
            # ==================================================

            st.divider()

            st.header("Resume Analysis")


            resume_tab1, resume_tab2 = st.tabs(
                [
                    "Resume Sections",
                    "Detected Skills"
                ]
            )


            with resume_tab1:

                for section_name, section_text in sections.items():

                    if section_text.strip():

                        with st.expander(
                            section_name.title()
                        ):

                            st.write(section_text)


            with resume_tab2:

                if skills:

                    st.write(
                        f"{len(skills)} skills detected in your resume."
                    )

                    st.write(
                        sorted(skills)
                    )

                else:

                    st.warning(
                        "No skills detected in your resume."
                    )


            # ==================================================
            # JOB ANALYSIS
            # ==================================================

            st.divider()

            st.header("Job Analysis")


            job_tab1, job_tab2 = st.tabs(
                [
                    "Job Skills",
                    "Required vs Preferred"
                ]
            )


            with job_tab1:

                if job_skills:

                    st.write(
                        f"{len(job_skills)} skills detected in the job description."
                    )

                    st.write(
                        sorted(job_skills)
                    )

                else:

                    st.warning(
                        "No skills detected in the job description."
                    )


            with job_tab2:

                requirement_col1, requirement_col2 = (
                    st.columns(2)
                )


                with requirement_col1:

                    st.subheader("Required Skills")

                    if required_skills:

                        for skill in sorted(required_skills):

                            st.write(
                                f"- {skill}"
                            )

                        st.metric(
                            "Required Skill Match",
                            f"{required_score:.1f}%"
                        )

                    else:

                        st.write(
                            "No required skills detected."
                        )


                with requirement_col2:

                    st.subheader("Preferred Skills")

                    if preferred_skills:

                        for skill in sorted(preferred_skills):

                            st.write(
                                f"- {skill}"
                            )

                        st.metric(
                            "Preferred Skill Match",
                            f"{preferred_score:.1f}%"
                        )

                    else:

                        st.write(
                            "No preferred skills detected."
                        )


            # ==================================================
            # SKILL MATCHING
            # ==================================================

            st.divider()

            st.header("Skill Matching")


            match_col1, match_col2 = st.columns(2)


            with match_col1:

                st.subheader("Matching Skills")

                if matched_skills:

                    for skill in sorted(matched_skills):

                        st.write(
                            f"- {skill}"
                        )

                else:

                    st.write(
                        "No matching skills found."
                    )


            with match_col2:

                st.subheader("Missing Skills")

                if missing_skills:

                    for skill in sorted(missing_skills):

                        st.write(
                            f"- {skill}"
                        )

                else:

                    st.write(
                        "No major missing skills detected."
                    )


            # ==================================================
            # SKILL GAP ANALYSIS
            # ==================================================

            st.divider()

            st.header("Skill Gap Analysis")


            gap_col1, gap_col2 = st.columns(2)


            with gap_col1:

                st.subheader("Required Skill Gaps")

                if required_missing:

                    for skill in sorted(required_missing):

                        st.write(
                            f"- {skill}"
                        )

                else:

                    st.write(
                        "No required skill gaps detected."
                    )


            with gap_col2:

                st.subheader("Preferred Skill Gaps")

                if preferred_missing:

                    for skill in sorted(preferred_missing):

                        st.write(
                            f"- {skill}"
                        )

                else:

                    st.write(
                        "No preferred skill gaps detected."
                    )


            if recommendations:

                st.subheader("Recommendations")

                for recommendation in recommendations:

                    st.write(
                        f"- {recommendation}"
                    )


            # ==================================================
            # RESUME IMPROVEMENTS
            # ==================================================

            st.divider()

            st.header("Resume Improvement Suggestions")


            if resume_suggestions:

                for suggestion in resume_suggestions:

                    st.write(
                        f"- {suggestion}"
                    )

            else:

                st.write(
                    "No improvement suggestions available."
                )


            # ==================================================
            # ATS ANALYSIS
            # ==================================================

            st.divider()

            st.header("ATS Resume Analysis")


            if ats_score >= 80:

                st.success(
                    "Your resume has a strong ATS-friendly structure."
                )

            elif ats_score >= 60:

                st.warning(
                    "Your resume is moderately ATS-friendly."
                )

            else:

                st.error(
                    "Your resume needs improvement for better ATS compatibility."
                )


            if ats_suggestions:

                st.subheader(
                    "ATS Improvement Suggestions"
                )

                for suggestion in ats_suggestions:

                    st.write(
                        f"- {suggestion}"
                    )


            # ==================================================
            # JOB RECOMMENDATIONS
            # ==================================================

            st.divider()

            st.header("Recommended Jobs")


            if job_recommendations:

                st.write(
                    "Jobs are ranked using skill matching and semantic similarity."
                )


                for index, job in enumerate(
                    job_recommendations[:5],
                    start=1
                ):

                    with st.expander(
                        f"{index}. {job['title']}"
                    ):

                        recommendation_col1, recommendation_col2, recommendation_col3 = (
                            st.columns(3)
                        )


                        with recommendation_col1:

                            st.metric(
                                "Recommendation Score",
                                f"{job['score']:.1f}%"
                            )


                        with recommendation_col2:

                            st.metric(
                                "Skill Match",
                                f"{job['skill_score']:.1f}%"
                            )


                        with recommendation_col3:

                            st.metric(
                                "Semantic Similarity",
                                f"{job['semantic_score']:.1f}%"
                            )


                        st.write(
                            job["description"]
                        )


                        if job["matched_skills"]:

                            st.write(
                                "Matching Skills"
                            )

                            st.write(
                                ", ".join(
                                    job["matched_skills"]
                                )
                            )

                        else:

                            st.write(
                                "No matching skills found."
                            )


            else:

                st.warning(
                    "No suitable job recommendations found."
                )


            # ==================================================
            # FINAL SUMMARY
            # ==================================================

            st.divider()

            st.header("Final Summary")


            summary_col1, summary_col2, summary_col3, summary_col4 = (
                st.columns(4)
            )


            with summary_col1:

                st.metric(
                    "Job Skills",
                    len(job_skills)
                )


            with summary_col2:

                st.metric(
                    "Matched Skills",
                    len(matched_skills)
                )


            with summary_col3:

                st.metric(
                    "Missing Skills",
                    len(missing_skills)
                )


            with summary_col4:

                st.metric(
                    "ATS Score",
                    f"{ats_score:.1f}%"
                )


            # ==================================================
            # DOWNLOAD ANALYSIS REPORT
            # ==================================================

            st.divider()

            st.header("Download Analysis Report")


            report = generate_report(
                overall_score=overall_score,
                ats_score=ats_score,
                skill_score=skill_score,
                semantic_score=semantic_score,
                matched_skills=matched_skills,
                missing_skills=missing_skills,
                required_missing=required_missing,
                preferred_missing=preferred_missing,
                recommendations=recommendations,
                resume_suggestions=resume_suggestions,
                ats_suggestions=ats_suggestions
            )


            st.download_button(
                label="Download Analysis Report",
                data=report,
                file_name="CareerMatch_AI_Report.txt",
                mime="text/plain",
                use_container_width=True
            )