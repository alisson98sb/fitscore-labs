## 2026-05-19

Started the first deep work session for FitScore.

Created:
- project structure
- README
- first resume parsing script

Learned:
- basic text preprocessing
- skill keyword matching
- project organization

Result:
- 83.33% keyword match score


## 2026-05-20

Implemented the first semantic similarity test for FitScore using embeddings.

Learned:
- sentence-transformers
- embeddings
- cosine similarity
- semantic matching

Created:
- semantic_match.py

Result:
- Semantic similarity score: 0.6334

Insights:
- semantic matching can identify similarity even without exact keyword matches
- embeddings are significantly more powerful than lexical matching alone


## 2026-05-21

Implemented the first FitScore scoring pipeline.

Created:
- keyword score
- semantic score
- weighted final score

Result:
- Keyword Score: 83.33%
- Semantic Score: 74.75%
- Final FitScore: 78.18%

Insight:
- combining lexical and semantic scoring gives a more balanced compatibility analysis between resume and job description.