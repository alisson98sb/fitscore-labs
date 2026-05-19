# src/preprocessing/resume_parser.py

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

RESUME_PATH = BASE_DIR / "data" / "resumes" / "sample_resume.txt"
JOB_PATH = BASE_DIR / "data" / "jobs" / "sample_job.txt"

SKILLS = [
    "python",
    "java",
    "spring",
    "docker",
    "aws",
    "react",
    "postgresql",
    "machine learning",
    "artificial intelligence",
    "api",
]


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8").lower()


def count_words(text: str) -> int:
    return len(text.split())


def find_skills(text: str, skills: list[str]) -> list[str]:
    return [skill for skill in skills if skill in text]


def calculate_keyword_match(resume_skills: list[str], job_skills: list[str]) -> float:
    if not job_skills:
        return 0.0

    matched_skills = set(resume_skills).intersection(job_skills)
    return round((len(matched_skills) / len(job_skills)) * 100, 2)


def main() -> None:
    resume_text = read_text_file(RESUME_PATH)
    job_text = read_text_file(JOB_PATH)

    resume_skills = find_skills(resume_text, SKILLS)
    job_skills = find_skills(job_text, SKILLS)

    match_score = calculate_keyword_match(resume_skills, job_skills)

    print("=== FitScore Resume Parser ===")
    print(f"Resume words: {count_words(resume_text)}")
    print(f"Job description words: {count_words(job_text)}")

    print("\nSkills found in resume:")
    print(resume_skills)

    print("\nSkills required in job:")
    print(job_skills)

    print(f"\nKeyword match score: {match_score}%")


if __name__ == "__main__":
    main()