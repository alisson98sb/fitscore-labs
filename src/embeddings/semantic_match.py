
#Comparar:
#   currículo;
#   vaga;
# usando embeddings reais.


#Melhor biblioteca pra começar:
#   sentence-transformers
# pip install sentence-transformers

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer('all-MiniLM-L6-v2')

resume = """
Java backend developer with experience in Spring Boot, Docker,
PostgreSQL and REST APIs.
"""

job = """
Looking for a backend engineer with API development experience,
Docker knowledge and relational databases.
"""

resume_embedding = model.encode([resume])
job_embedding = model.encode([job])

similarity = cosine_similarity(
    resume_embedding,
    job_embedding
)

print(f"Semantic similarity: {similarity[0][0]:.4f}")