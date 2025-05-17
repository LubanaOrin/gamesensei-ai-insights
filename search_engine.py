from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

def get_similar_posts(query, corpus_path="data/sample_reddit_dump.json"):
    with open(corpus_path, "r") as f:
        data = json.load(f)
    texts = [item['body'] for item in data]
    vectorizer = TfidfVectorizer().fit_transform(texts + [query])
    sim_matrix = cosine_similarity(vectorizer[-1], vectorizer[:-1])
    top_indexes = sim_matrix[0].argsort()[-5:][::-1]
    return "\n\n".join([texts[i] for i in top_indexes])
