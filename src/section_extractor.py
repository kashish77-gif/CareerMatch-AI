import re


SECTION_NAMES = {
    "skills": [
        "skills",
        "technical skills",
        "key skills",
        "core skills",
        "technical expertise"
    ],

    "education": [
        "education",
        "academic background",
        "qualifications",
        "educational qualifications"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment"
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "key projects"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "licenses"
    ]
}


def find_section_heading(line):
    """
    Check whether a line is a known resume section heading.
    """

    cleaned_line = line.strip().lower()

    # Remove common characters
    cleaned_line = re.sub(r"[^a-zA-Z\s]", "", cleaned_line)

    for section, names in SECTION_NAMES.items():

        if cleaned_line in names:
            return section

    return None


def extract_sections(text):
    """
    Divide resume text into different sections.
    """

    sections = {
        "skills": "",
        "education": "",
        "experience": "",
        "projects": "",
        "certifications": ""
    }

    current_section = None

    lines = text.splitlines()

    for line in lines:

        section = find_section_heading(line)

        if section:
            current_section = section
            continue

        if current_section:
            sections[current_section] += line + "\n"

    return sections