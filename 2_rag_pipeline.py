"""
RAG pipeline: Chunk financial filings and create embeddings.
Uses ChromaDB for vector storage and retrieval.
"""

import json
from pathlib import Path
from typing import List, Dict
import hashlib

class FilingChunker:
    """Chunk financial filings for RAG."""
    
    def __init__(self, chunk_size: int = 500, overlap: int = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.chunks = []
    
    def create_synthetic_filings(self) -> Dict[str, str]:
        """
        Create synthetic filing text.
        In production, parse actual SEC HTML/text filings.
        """
        filing_text = {
            'Item_1_Business': """
            The Company operates in the technology sector, focusing on cloud infrastructure solutions.
            Our revenue streams include Software-as-a-Service (SaaS), professional services, and 
            support contracts. In Q2 2024, we achieved $67.5M in revenue, representing a 8.9% 
            increase from Q1 2024. This growth was driven primarily by a 15% increase in 
            enterprise customer acquisitions and a 12% expansion of existing customer contracts.
            """,
            'Item_7A_Risk_Factors': """
            Key risk factors include market competition, regulatory compliance, and supply chain 
            disruptions. Our competitive landscape includes larger established players with greater 
            resources. We mitigate through continuous innovation and customer focus. Regulatory 
            requirements around data privacy compliance (GDPR, CCPA) require ongoing investment. 
            Supply chain risks were partially mitigated by diversifying vendor relationships in 2023.
            """,
            'Item_MD&A_Liquidity': """
            Our liquidity position remains strong with a current ratio of 2.0x as of Q2 2024. 
            Operating cash flow totaled $18.0M in Q2, up 11% from the prior quarter. We maintain 
            $200M in available credit facilities. Capital expenditure is projected at $6-7M quarterly 
            for cloud infrastructure expansion. Debt-to-equity ratio stands at 0.69x, providing 
            ample borrowing capacity.
            """
        }
        return filing_text
    
    def chunk_text(self, text: str, source_id: str) -> List[Dict]:
        """Split text into overlapping chunks."""
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), self.chunk_size - self.overlap):
            chunk_words = words[i:i + self.chunk_size]
            chunk_text = ' '.join(chunk_words).strip()
            
            if len(chunk_text) > 50:  # Skip very small chunks
                chunk_id = hashlib.md5(chunk_text.encode()).hexdigest()[:12]
                chunks.append({
                    'id': chunk_id,
                    'text': chunk_text,
                    'source': source_id,
                    'start_pos': i,
                    'word_count': len(chunk_words)
                })
        
        return chunks
    
    def process_filings(self) -> List[Dict]:
        """Process all filing sections into chunks."""
        filings = self.create_synthetic_filings()
        all_chunks = []
        
        for section, text in filings.items():
            chunks = self.chunk_text(text, section)
            all_chunks.extend(chunks)
        
        self.chunks = all_chunks
        return all_chunks
    
    def save_chunks(self, output_file: str = "data/chunks.json"):
        """Save chunks for embedding."""
        Path("data").mkdir(exist_ok=True)
        with open(output_file, 'w') as f:
            json.dump(self.chunks, f, indent=2)
        print(f"✓ {len(self.chunks)} chunks saved to {output_file}")


class ChromaDBVectorStore:
    """Simple in-memory vector store (mock ChromaDB)."""
    
    def __init__(self):
        self.documents = []
        self.embeddings = []
        self.metadata = []
    
    def add_documents(self, chunks: List[Dict], embeddings: List[List[float]]):
        """Add chunks and their embeddings."""
        self.documents.extend([c['text'] for c in chunks])
        self.embeddings.extend(embeddings)
        self.metadata.extend([{'source': c['source'], 'id': c['id']} for c in chunks])
    
    def retrieve_similar(self, query_embedding: List[float], top_k: int = 3) -> List[Dict]:
        """Retrieve top-k similar documents (mock cosine similarity)."""
        if not self.embeddings:
            return []
        
        similarities = []
        for i, emb in enumerate(self.embeddings):
            # Simple dot product as mock similarity
            sim = sum(a * b for a, b in zip(query_embedding, emb)) / (len(query_embedding) + 1e-10)
            similarities.append((i, sim))
        
        # Sort by similarity and return top_k
        top_indices = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]
        results = [
            {
                'text': self.documents[idx],
                'source': self.metadata[idx]['source'],
                'similarity': sim,
                'chunk_id': self.metadata[idx]['id']
            }
            for idx, sim in top_indices
        ]
        return results


if __name__ == "__main__":
    print("🔍 Processing filings into chunks...")
    chunker = FilingChunker(chunk_size=100, overlap=20)
    chunks = chunker.process_filings()
    
    print(f"✓ Created {len(chunks)} chunks")
    for chunk in chunks[:3]:
        print(f"  - {chunk['source']}: {chunk['word_count']} words")
    
    print("\n💾 Saving chunks...")
    chunker.save_chunks()
    
    print("\n✅ RAG pipeline setup complete!")
