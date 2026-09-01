import re


SKILL_DATABASE = [
    # Programming Languages
    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "JavaScript",
    "TypeScript",
    "R",
    "Go",
    "PHP",

    # Data Science
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Matplotlib",
    "Seaborn",
    "TensorFlow",
    "PyTorch",

    # Machine Learning / AI
    "Machine Learning",
    "Deep Learning",
    "Natural Language Processing",
    "NLP",
    "Computer Vision",
    "Artificial Intelligence",

    # Databases
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Oracle",

    # Data / BI
    "Power BI",
    "Tableau",
    "Excel",
    "Data Analysis",
    "Data Visualization",

    # Cloud / DevOps
    "AWS",
    "Azure",
    "Google Cloud",
    "Docker",
    "Kubernetes",

    # Web
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "FastAPI",
    "Django",
    "Flask",

    # Tools
    "Git",
    "GitHub",
    "Jupyter Notebook",

    # Concepts
    "Data Structures",
    "Algorithms",
    "Object Oriented Programming"
]


def extract_skills(text):
    """
    Extract skills from text using a predefined skill database.
    """

    found_skills = []

    text_lower = text.lower()

    for skill in SKILL_DATABASE:

        skill_lower = skill.lower()

        pattern = r"\b" + re.escape(skill_lower) + r"\b"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return found_skills