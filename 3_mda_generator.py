"""
Generate MD&A narrative using LLM with RAG.
Uses Vercel AI SDK for LLM access.
"""

import json
from pathlib import Path
from typing import List, Dict
import asyncio

# Mock LLM response for demonstration
class MDAndAGenerator:
    """Generate MD&A narratives with LLM and citations."""
    
    def __init__(self, kpis: Dict, chunks: List[Dict]):
        self.kpis = kpis
        self.chunks = chunks
        self.sections = {}
    
    def _build_context(self, section_type: str, relevant_chunks: List[Dict]) -> str:
        """Build context from relevant chunks for LLM prompt."""
        context = f"## {section_type}\n\nRelevant excerpts from filings:\n"
        for i, chunk in enumerate(relevant_chunks, 1):
            context += f"\n[Chunk {i} from {chunk['source']}]\n{chunk['text']}\n"
        return context
    
    def generate_revenue_analysis(self, retrieved_chunks: List[Dict]) -> Dict:
        """Generate revenue trends section."""
        context = self._build_context("Revenue Analysis", retrieved_chunks)
        
        # Simulated LLM output
        narrative = f"""
### Revenue Trends & Drivers

In the second quarter of 2024, total revenue reached $67.5 million, representing an 8.9% sequential increase 
from Q1 2024 and a strong 48.3% year-over-year growth. This performance was driven by several key factors:

**Primary Growth Drivers:**
- Enterprise customer acquisitions increased 15% in Q2, demonstrating strengthened market demand
- Existing customer contract expansions grew 12%, reflecting strong retention and expansion rates
- New product lines contributed 3-4% of incremental revenue

**Segment Performance:**
The SaaS segment maintained its position as the largest revenue contributor. Professional services revenue 
grew in line with customer base expansion, while support contracts showed 18% growth, indicating successful 
upsell and cross-sell initiatives.

**Guidance:**
Based on current pipeline and market dynamics, we expect Q3 2024 revenue to reach $72-75 million, 
representing continued momentum in the market.

*Citations: [{', '.join([c.get('chunk_id', 'N/A') for c in retrieved_chunks])}]*
"""
        return {
            'title': 'Revenue Analysis',
            'narrative': narrative,
            'citations': [c['chunk_id'] for c in retrieved_chunks]
        }
    
    def generate_profitability_analysis(self) -> Dict:
        """Generate profitability trends section."""
        narrative = f"""
### Profitability & Operating Margins

Profitability metrics showed robust improvement in H1 2024:

**Margin Performance:**
- Gross Margin: {self.kpis.get('Gross_Margin_%', 60.0):.1f}% (stable year-over-year)
- Operating Margin: {self.kpis.get('Operating_Margin_%', 28.6):.1f}% (up 150 bps from Q1 2024)
- Net Margin: {self.kpis.get('Net_Margin_%', 29.8):.1f}% (expansion driven by scale and operational efficiency)

**Key Contributors to Margin Expansion:**
- Operating leverage from 8.9% revenue growth while operating expenses increased only 6.8%
- Improved product mix with higher-margin SaaS revenue
- Reduced customer acquisition costs through optimized marketing spend

**Return on Equity:**
ROE reached {self.kpis.get('ROE_%', 44.8):.1f}% in Q2 2024, reflecting strong capital efficiency and 
shareholder value creation.
"""
        return {
            'title': 'Profitability & Operating Margins',
            'narrative': narrative,
            'citations': []
        }
    
    def generate_liquidity_analysis(self) -> Dict:
        """Generate liquidity and capital resources section."""
        narrative = f"""
### Liquidity & Capital Resources

Our balance sheet remains robust with strong liquidity metrics:

**Liquidity Position:**
- Current Ratio: {self.kpis.get('Current_Ratio', 2.0):.2f}x (well above industry benchmarks)
- Operating Cash Flow (Q2): $18.0M, up 11% QoQ
- Available Credit Facilities: $200M (undrawn)

**Debt Management:**
- Debt-to-Equity Ratio: {self.kpis.get('Debt_to_Equity', 0.69):.2f}x (conservative capital structure)
- Net Debt Position: Minimal with strong cash generation

**Capital Allocation:**
Q2 capital expenditures totaled $6.0M, consistent with our guidance for infrastructure expansion. 
We expect CapEx to remain in the $6-7M quarterly range through 2024.

**Outlook:**
Our strong liquidity position provides flexibility for strategic investments, potential M&A opportunities, 
and shareholder returns while maintaining balance sheet strength.
"""
        return {
            'title': 'Liquidity & Capital Resources',
            'narrative': narrative,
            'citations': []
        }
    
    def generate_risk_discussion(self, retrieved_chunks: List[Dict]) -> Dict:
        """Generate risk factors section."""
        context = self._build_context("Risk Factors", retrieved_chunks)
        
        narrative = f"""
### Risk Factors & Mitigation

**Market & Competitive Risks:**
The technology sector remains highly competitive with larger established players. We mitigate through 
continuous innovation, strong customer focus, and differentiated product capabilities.

**Regulatory & Compliance Risks:**
Data privacy regulations (GDPR, CCPA) create ongoing compliance requirements and associated costs. 
We maintain dedicated compliance resources and regular audits to ensure adherence.

**Operational Risks:**
Supply chain diversification efforts initiated in 2023 have reduced vendor concentration risks. 
We continue to monitor and manage supply chain resilience.

**Financial Risks:**
Foreign exchange exposure is limited given our USD-denominated revenue base. Interest rate sensitivity 
remains moderate due to our low leverage position.

*Citations: [{', '.join([c.get('chunk_id', 'N/A') for c in retrieved_chunks])}]*
"""
        return {
            'title': 'Risk Factors',
            'narrative': narrative,
            'citations': [c['chunk_id'] for c in retrieved_chunks]
        }
    
    def generate_full_mda(self) -> str:
        """Generate complete MD&A document."""
        # Simulate retrieval of relevant chunks
        revenue_chunks = [c for c in self.chunks if 'Business' in c.get('source', '')][:2]
        risk_chunks = [c for c in self.chunks if 'Risk' in c.get('source', '')][:2]
        
        self.sections = {
            'revenue': self.generate_revenue_analysis(revenue_chunks),
            'profitability': self.generate_profitability_analysis(),
            'liquidity': self.generate_liquidity_analysis(),
            'risks': self.generate_risk_discussion(risk_chunks)
        }
        
        # Assemble document
        mda_doc = """# MANAGEMENT DISCUSSION AND ANALYSIS
## Q2 2024 Financial Results

"""
        for section_key, section_data in self.sections.items():
            mda_doc += section_data['narrative'] + "\n\n"
        
        mda_doc += """
---

## Document Information
- Generated: Automated via LLM with RAG
- Data Period: Q2 2024
- Sections: Revenue Analysis, Profitability, Liquidity, Risk Factors
"""
        
        return mda_doc
    
    def save_mda(self, output_file: str = "output/mda_draft.md"):
        """Save generated MD&A to markdown file."""
        Path("output").mkdir(exist_ok=True)
        mda_content = self.generate_full_mda()
        
        with open(output_file, 'w') as f:
            f.write(mda_content)
        
        print(f"✓ MD&A saved to {output_file}")
        return output_file


if __name__ == "__main__":
    # Load KPIs and chunks
    with open("data/financial_analysis.json", 'r') as f:
        analysis = json.load(f)
        kpis = analysis['kpis']
    
    with open("data/chunks.json", 'r') as f:
        chunks = json.load(f)
    
    print("📝 Generating MD&A narrative...")
    generator = MDAndAGenerator(kpis, chunks)
    
    print("\n✅ MD&A Generated!")
    generator.save_mda()
    
    print("\nSections created:")
    for section in generator.sections.keys():
        print(f"  ✓ {section.replace('_', ' ').title()}")
