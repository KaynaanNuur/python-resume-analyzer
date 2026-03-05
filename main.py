import sys
from analyzer import analyze_resume

if len(sys.argv) != 3:
    print("Usage: python main.py <resume_file> <job_description_file>")
    sys.exit(1)

resume_file = sys.argv[1]
job_file = sys.argv[2]

result = analyze_resume(resume_file, job_file)

print(result)

with open("analysis_report.txt", "w") as report:
    report.write(result)

print("\nReport saved to analysis_report.txt")