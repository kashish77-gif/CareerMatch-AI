# CareerMatch AI

## Project Overview

CareerMatch AI is an AI-powered resume analysis and job matching platform built with Python and Streamlit.

The application analyzes a candidate's resume and compares it with a job description to evaluate technical skill compatibility, semantic similarity, ATS compatibility, skill gaps, resume quality, and suitable job recommendations.

## Problem Statement

Job seekers often struggle to understand whether their resume matches a particular job description. Manually comparing resumes with job requirements is time-consuming and may cause candidates to overlook important missing skills or resume weaknesses.

CareerMatch AI addresses this problem by automatically analyzing the resume and job description and providing measurable matching results and actionable recommendations.

## Objectives

* Analyze resumes automatically.
* Extract important resume sections and technical skills.
* Analyze skills required by a job description.
* Separate required and preferred job skills.
* Calculate resume-job skill compatibility.
* Measure semantic similarity between the resume and job description.
* Calculate an overall match score.
* Identify missing skills and skill gaps.
* Evaluate ATS compatibility.
* Provide resume improvement suggestions.
* Recommend suitable jobs based on the candidate's skills.

## Key Features

### Resume Analysis

* PDF and DOCX resume upload.
* Automatic resume text extraction.
* Resume section detection.
* Technical skill extraction.

### Job Description Analysis

* Job description processing.
* Job skill extraction.
* Required skill identification.
* Preferred skill identification.

### Resume-Job Matching

* Matching skills detection.
* Missing skills detection.
* Skill match percentage.
* Required skill match score.
* Preferred skill match score.
* Weighted skill scoring.

### Semantic Matching

* Compares the meaning of the resume and job description.
* Generates a semantic similarity score.
* Helps identify compatibility beyond exact skill matches.

### Overall Match Score

The project combines skill compatibility and semantic similarity to calculate an overall resume-job match score.

### Skill Gap Analysis

Identifies skills required by the job that are missing from the resume and provides recommendations for improving the candidate's skill profile.

### Resume Improvement

Provides suggestions based on:

* Resume structure
* Missing sections
* Technical skills
* Required skills
* Preferred skills

### ATS Resume Analysis

Evaluates the resume for ATS-friendly characteristics and generates suggestions for improving ATS compatibility.

### Job Recommendations

Recommends suitable job roles based on:

* Resume skills
* Skill matching
* Semantic similarity

## System Workflow

```text
Resume Upload
      |
      v
Resume Text Extraction
      |
      v
Resume Section Extraction
      |
      v
Resume Skill Extraction
      |
      |
      +----------------------+
      |                      |
      v                      v
Job Description        ATS Analysis
      |
      v
Job Skill Extraction
      |
      v
Required / Preferred Skills
      |
      v
Skill Matching
      |
      +----------------------+
      |                      |
      v                      v
Skill Gap Analysis    Semantic Similarity
      |                      |
      +----------+-----------+
                 |
                 v
          Overall Match Score
                 |
        +--------+--------+
        |        |        |
        v        v        v
 Resume      Job       Recommendations
Improvement  Matching
```

## Technology Stack

### Programming Language

* Python

### Framework

* Streamlit

### Machine Learning / NLP

* Scikit-learn
* NLP techniques
* Semantic similarity

### Data Processing

* Pandas
* NumPy

### Resume Processing

* PDF text extraction
* DOCX text extraction

### Development Tools

* Jupyter Notebook
* Visual Studio Code
* Git
* GitHub

## Project Structure

```text
CareerMatch-AI/
│
├── app.py
├── requirements.txt
├── test_semantic.py
│
├── data/
│   └── jobs.json
│
├── src/
│   ├── __init__.py
│   ├── resume_parser.py
│   ├── section_extractor.py
│   ├── skill_extractor.py
│   ├── matcher.py
│   ├── semantic_matcher.py
│   ├── score_calculator.py
│   ├── score_matcher.py
│   ├── job_analyzer.py
│   ├── skill_gap.py
│   ├── resume_improver.py
│   ├── ats_analyzer.py
│   └── job_recommender.py
│
├── .gitignore
└── uploads/
```

> `uploads/` is used locally for uploaded files and is excluded from the Git repository.

## Module Description

| File                   | Purpose                                           |
| ---------------------- | ------------------------------------------------- |
| `app.py`               | Main Streamlit application                        |
| `resume_parser.py`     | Extracts text from uploaded resumes               |
| `section_extractor.py` | Identifies resume sections                        |
| `skill_extractor.py`   | Extracts technical skills                         |
| `matcher.py`           | Compares resume skills with job skills            |
| `semantic_matcher.py`  | Calculates semantic similarity                    |
| `score_calculator.py`  | Calculates overall match score                    |
| `score_matcher.py`     | Handles score matching functionality              |
| `job_analyzer.py`      | Separates required and preferred job requirements |
| `skill_gap.py`         | Generates skill gap recommendations               |
| `resume_improver.py`   | Generates resume improvement suggestions          |
| `ats_analyzer.py`      | Calculates ATS score and suggestions              |
| `job_recommender.py`   | Recommends suitable jobs                          |
| `jobs.json`            | Stores job recommendation data                    |
| `test_semantic.py`     | Tests semantic matching functionality             |

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kashish77-gif/CareerMatch-AI.git
```

### 2. Navigate to the Project

```bash
cd CareerMatch-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Run:

```bash
streamlit run app.py
```

The application will open in the browser.

## Example Output

The application provides:

* Overall Match Score
* Skill Match Score
* Semantic Similarity Score
* Required Skill Match
* Preferred Skill Match
* Matching Skills
* Missing Skills
* Required Skill Gaps
* Preferred Skill Gaps
* Skill Gap Recommendations
* Resume Improvement Suggestions
* ATS Score
* ATS Improvement Suggestions
* Recommended Jobs

## Security and Privacy

* Virtual environments are excluded from version control.
* Uploaded resumes are excluded from the Git repository.
* Environment files are excluded from version control.
* API keys and secrets should not be stored directly in source code.
* Uploaded documents should be handled carefully because resumes may contain personal information.

## Testing

Semantic matching functionality can be tested using:

```bash
python test_semantic.py
```

## Development Challenges

During development, several practical issues were encountered and resolved, including:

* Setting up the Python virtual environment.
* Running the Streamlit application locally.
* Handling Streamlit loading issues.
* Resolving Python and Streamlit launcher errors.
* Handling PowerShell virtual-environment activation.
* Building the project module by module.
* Integrating multiple analysis components into the main application.
* Preventing uploaded files and virtual-environment files from being committed to Git.
* Setting up Git version control.
* Connecting the local project to GitHub.
* Organizing the project into reusable Python modules.

## Future Improvements

* Advanced NLP-based skill extraction.
* Better resume formatting analysis.
* Resume keyword optimization.
* Personalized learning recommendations for missing skills.
* Integration with live job-search APIs.
* User authentication.
* Resume improvement using generative AI.
* More advanced ATS analysis.
* Cloud deployment.
* Improved document security.
* Database integration.
* Job application tracking.

## Disclaimer

CareerMatch AI is an educational and career-support application. Match scores, ATS scores, recommendations, and suggestions are intended to provide guidance and should not be considered a replacement for professional recruitment decisions.

## Author

**Kashish Vashishtha**

B.Tech Computer Science Engineering

GitHub:
[https://github.com/kashish77-gif](https://github.com/kashish77-gif)

## License

This project is created for educational and portfolio purposes.
