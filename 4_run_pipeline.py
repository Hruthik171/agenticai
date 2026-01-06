"""
Main execution script: Run the complete MD&A generation pipeline.
"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

from scripts.setup_data import FinancialDataProcessor
from scripts.rag_pipeline import FilingChunker, ChromaDBVectorStore
from scripts.mda_generator import MDAndAGenerator

def main():
    print("=" * 60)
    print("AUTOMATED MD&A GENERATION PIPELINE")
    print("=" * 60)
    
    # Step 1: Process financial data
    print("\n[1/4] Processing financial statements...")
    processor = FinancialDataProcessor()
    processor.load_sample_data()
    kpis = processor.compute_kpis()
    processor.compute_yoy_qoq_deltas()
    processor.export_analysis()
    
    print("\n     KPIs computed:")
    for k, v in list(kpis.items())[:5]:
        print(f"     • {k}: {v:.2f}")
    
    # Step 2: Create RAG chunks
    print("\n[2/4] Creating filing chunks for RAG...")
    chunker = FilingChunker(chunk_size=100, overlap=20)
    chunks = chunker.process_filings()
    chunker.save_chunks()
    print(f"     {len(chunks)} chunks created and indexed")
    
    # Step 3: Generate MD&A
    print("\n[3/4] Generating MD&A narrative...")
    generator = MDAndAGenerator(kpis, chunks)
    mda_file = generator.save_mda()
    
    print(f"     ✓ Sections generated: Revenue, Profitability, Liquidity, Risks")
    print(f"     ✓ Output: {mda_file}")
    
    # Step 4: Summary
    print("\n[4/4] Pipeline complete!")
    print("\n" + "=" * 60)
    print("DELIVERABLES")
    print("=" * 60)
    print("✓ output/mda_draft.md - Full MD&A narrative with citations")
    print("✓ data/financial_analysis.json - KPIs and deltas")
    print("✓ data/chunks.json - Filing chunks for retrieval")
    print("\nNext steps:")
    print("  1. Review output/mda_draft.md for accuracy")
    print("  2. Integrate real SEC filing data via EDGAR API")
    print("  3. Replace mock LLM with real API calls")
    print("  4. Add ChromaDB vector store for production RAG")
    print("=" * 60)


if __name__ == "__main__":
    main()
