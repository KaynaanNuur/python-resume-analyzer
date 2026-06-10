# Python Resume Analyzer

A Python application that analyzes a resume against a job description to determine how well a candidate matches a position. The program extracts keywords, calculates a match score, identifies missing skills, and generates a detailed analysis report.

## Features

* Compare resumes with job descriptions
* Calculate a resume match percentage
* Identify matching keywords and skills
* Highlight missing skills from the resume
* Generate an analysis report
* Display the most common skills found in the resume
* Simple command-line interface

## Technologies Used

* Python 3
* Collections (Counter)
* File Handling
* Text Processing
* Set Operations

## Project Structure

```text
python-resume-analyzer/
│
├── main.py
├── analyzer.py
├── text_processing.py
├── sample_data/
│   ├── resume.txt
│   └── job_description.txt
└── analysis_report.txt
```

## How It Works

1. The user provides a resume file and a job description file.
2. The application reads and processes the text.
3. Common words are removed using stopword filtering.
4. Skills and keywords are extracted.
5. A match score is calculated based on overlapping keywords.
6. Missing skills are identified.
7. Results are displayed and saved to a report file.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/python-resume-analyzer.git
cd python-resume-analyzer
```

## Usage

Run the application from the terminal:

```bash
python main.py sample_data/resume.txt sample_data/job_description.txt
```

Or:

```bash
python3 main.py sample_data/resume.txt sample_data/job_description.txt
```

## Example Output

```text
Resume Match Score: 75.00%

Matching Skills:
python, sql, react

Missing Skills:
aws, docker

Top Resume Skills
-----------------
python (5)
sql (3)
react (2)
```

## Future Improvements

* PDF resume support
* Graphical user interface (GUI)
* Skill categorization
* Resume recommendations
* Data visualization charts
* NLP-based keyword matching
* Machine learning scoring models

## Learning Outcomes

This project demonstrates:

* Python programming fundamentals
* Data structures and algorithms
* Text processing techniques
* File input/output operations
* Modular application design
* Basic data analysis concepts

## Author

Kaynaan Nuur

Computer Programming and Analysis Student at Humber College
