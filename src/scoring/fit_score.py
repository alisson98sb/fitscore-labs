from pathlib import Path

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


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


def find_skills(text: str, skills: list[str]) -> list[str]:
    return [skill for skill in skills if skill in text]


def calculate_keyword_score(resume_skills: list[str], job_skills: list[str]) -> float:
    if not job_skills:
        return 0.0

    matched_skills = set(resume_skills).intersection(job_skills)

    return round((len(matched_skills) / len(job_skills)) * 100, 2)


def calculate_semantic_score(resume_text: str, job_text: str) -> float:
    model = SentenceTransformer("all-MiniLM-L6-v2")

    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_text])

    similarity = cosine_similarity(resume_embedding, job_embedding)[0][0]

    return round(similarity * 100, 2)


def calculate_final_score(keyword_score: float, semantic_score: float) -> float:
    final_score = (float(keyword_score) * 0.4) + (float(semantic_score) * 0.6)
    return round(final_score, 2)


def main() -> None:
    resume_text = read_text_file(RESUME_PATH)
    job_text = read_text_file(JOB_PATH)

    resume_skills = find_skills(resume_text, SKILLS)
    job_skills = find_skills(job_text, SKILLS)

    keyword_score = calculate_keyword_score(resume_skills, job_skills)
    semantic_score = calculate_semantic_score(resume_text, job_text)
    final_score = calculate_final_score(keyword_score, semantic_score)

    print("=== FitScore ===")
    print(f"Keyword Score: {keyword_score}%")
    print(f"Semantic Score: {semantic_score}%")
    print(f"Final FitScore: {final_score}%")

    print("\nResume Skills:")
    print(resume_skills)

    print("\nJob Required Skills:")
    print(job_skills)


if __name__ == "__main__":
    main()