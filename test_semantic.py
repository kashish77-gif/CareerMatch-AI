from src.semantic_matcher import calculate_semantic_similarity


resume_text = """
I have experience building predictive models
using Python and Scikit-learn.
"""

job_description = """
We are looking for a candidate with experience
developing machine learning solutions using Python.
"""


score = calculate_semantic_similarity(
    resume_text,
    job_description
)

print(f"Semantic Similarity: {score:.2f}%")