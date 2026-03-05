from text_processing import process_text
from collections import Counter

def analyze_resume(resume_path, job_path):

    with open(resume_path, "r") as file:
        resume_text = file.read()

    with open(job_path, "r") as file:
        job_text = file.read()

    resume_words = process_text(resume_text)
    job_words = process_text(job_text)

    resume_set = set(resume_words)
    job_set = set(job_words)

    matching_skills = resume_set.intersection(job_set)
    missing_skills = job_set.difference(resume_set)

    score = (len(matching_skills) / len(job_set)) * 100

    # count resume word frequency
    word_counts = Counter(resume_words)
    top_skills = word_counts.most_common(5)

    top_skills_output = "\n".join([f"{skill} ({count})" for skill, count in top_skills])

    result = f"""
Resume Match Score: {score:.2f}%

Matching Skills:
{', '.join(sorted(matching_skills))}

Missing Skills:
{', '.join(sorted(missing_skills))}

Top Resume Skills
-----------------
{top_skills_output}
"""

    return result