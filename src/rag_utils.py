"""
RAG Utility Module.
Contains helper functions to create embeddings, chunk texts, and perform basic vector retrieval.
"""
import logging
from typing import List, Dict, Any
import google.generativeai as genai

from src.config import GEMINI_API_KEY

logger = logging.getLogger(__name__)

def generate_embeddings(texts: List[str], model: str = 'models/text-embedding-004') -> List[List[float]]:
    """
    Generates embeddings for a list of texts using Google Generative AI embeddings.
    
    Args:
        texts (List[str]): List of documents/strings to embed.
        model (str): The embedding model to use.
        
    Returns:
        List[List[float]]: A list containing embedding vectors for each input text.
    """
    if not GEMINI_API_KEY:
         logger.warning("API Key não encontrada. Não é possível gerar embeddings.")
         return []

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        embeddings = []
        for text in texts:
            response = genai.embed_content(
                model=model,
                content=text,
                task_type="retrieval_document"
            )
            embeddings.append(response['embedding'])
        logger.info(f"Gerados {len(embeddings)} embeddings com sucesso.")
        return embeddings
    except Exception as e:
        logger.error(f"Erro ao gerar embeddings: {e}", exc_info=True)
        return []

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """
    Calculates the cosine similarity between two vectors.
    """
    if not vec1 or not vec2 or len(vec1) != len(vec2):
        return 0.0
    
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm_a = sum(a * a for a in vec1) ** 0.5
    norm_b = sum(b * b for b in vec2) ** 0.5
    
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
        
    return dot_product / (norm_a * norm_b)

def retrieve_top_k(query_embedding: List[float], doc_embeddings: List[List[float]], documents: List[str], k: int = 3) -> List[str]:
    """
    Retrieves the top K most similar documents based on cosine similarity.
    
    Args:
        query_embedding: Vector embedding of the search query.
        doc_embeddings: List of document vectors.
        documents: List of original text documents.
        k: Number of documents to retrieve.
        
    Returns:
        List[str]: The top K matching documents.
    """
    if not query_embedding or not doc_embeddings or not documents:
        return []
        
    similarities = [cosine_similarity(query_embedding, doc_emb) for doc_emb in doc_embeddings]
    
    # Zip similarities with documents, sort descending, and get top K
    scored_docs = sorted(zip(similarities, documents), key=lambda x: x[0], reverse=True)
    return [doc for score, doc in scored_docs[:k]]
