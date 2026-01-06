"use client"

import { useState } from "react"
import KPICard from "@/components/kpi-card"
import MDASectionCard from "@/components/mda-section-card"

const mockResults = {
  fileName: "AAPL_2023_10K.xlsx",
  company: "Apple Inc.",
  period: "Q4 2023",
  kpis: [
    { label: "Revenue Growth (YoY)", value: "+12.4%", change: "up", color: "success" },
    { label: "Gross Margin", value: "48.2%", change: "up", color: "success" },
    { label: "Operating Margin", value: "31.5%", change: "down", color: "warning" },
    { label: "ROE", value: "156.8%", change: "up", color: "success" },
  ],
  mdaSections: [
    {
      title: "Revenue Overview",
      content:
        "Total net sales increased 12.4% year-over-year to $383.3 billion, driven primarily by strong iPhone sales and services growth. The iPhone segment contributed $192.5 billion (+8.2% YoY), while Services reached $85.2 billion (+16.5% YoY), demonstrating the company's successful transition toward recurring revenue streams.",
      sources: ["SEC Filing - Segment Revenue", "Management Discussion p. 23-24"],
    },
    {
      title: "Cost of Goods & Gross Margin",
      content:
        "Gross margin improved to 48.2% from 46.8% in the prior year, reflecting improved supply chain efficiency and favorable product mix. The company maintained strong pricing power while managing component costs effectively. International revenue, which carries higher margins, represented 47% of net sales.",
      sources: ["SEC Filing - Cost Analysis", "Notes to Financial Statements p. 15"],
    },
    {
      title: "Risk Factors & Challenges",
      content:
        "Key risks include continued geopolitical tensions impacting supply chains, competitive pressure in emerging markets, and foreign exchange headwinds. The company faces regulatory scrutiny in the EU and China, which could impact App Store economics. Supply chain disruptions, while improving, remain a concern for future growth.",
      sources: ["Risk Factors Section p. 8-12", "Forward-Looking Statements"],
    },
    {
      title: "Liquidity & Capital Allocation",
      content:
        "The company maintains a strong balance sheet with $47.8 billion in cash and cash equivalents. Operating cash flow reached $110.2 billion (+6.3% YoY), funding capital expenditures of $12.5 billion and shareholder returns of $98.2 billion through dividends and buybacks. Debt-to-equity ratio remains conservative at 1.84x.",
      sources: ["Cash Flow Statement", "Capital Allocation Policy p. 31-33"],
    },
  ],
}

export default function ResultsDisplay() {
  const [selectedSection, setSelectedSection] = useState(0)

  return (
    <div className="max-w-7xl mx-auto px-6 py-12">
      {/* Header */}
      <div className="mb-12">
        <div className="mb-4">
          <p className="text-[var(--color-text-secondary)] mb-2">Processing Complete</p>
          <h1 className="text-4xl font-bold text-[var(--color-text)] mb-2">{mockResults.company}</h1>
          <p className="text-[var(--color-text-secondary)]">
            {mockResults.period} • {mockResults.fileName}
          </p>
        </div>
      </div>

      {/* KPIs Grid */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-12">
        {mockResults.kpis.map((kpi, index) => (
          <KPICard key={index} {...kpi} />
        ))}
      </div>

      {/* MD&A Sections */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Section List */}
        <div className="lg:col-span-1">
          <div className="sticky top-24">
            <h3 className="text-lg font-semibold text-[var(--color-text)] mb-4">Sections</h3>
            <div className="space-y-2">
              {mockResults.mdaSections.map((section, index) => (
                <button
                  key={index}
                  onClick={() => setSelectedSection(index)}
                  className={`w-full text-left px-4 py-3 rounded-lg transition-all ${
                    selectedSection === index
                      ? "bg-[var(--color-accent)] text-[var(--color-background)] font-semibold"
                      : "bg-[var(--color-surface)] text-[var(--color-text)] hover:bg-[var(--color-surface-secondary)]"
                  }`}
                >
                  {section.title}
                </button>
              ))}
            </div>

            <button className="w-full mt-6 px-4 py-3 bg-[var(--color-surface)] text-[var(--color-accent)] rounded-lg hover:bg-[var(--color-surface-secondary)] transition font-semibold">
              Download as Markdown
            </button>
          </div>
        </div>

        {/* Section Content */}
        <div className="lg:col-span-2">
          <MDASectionCard section={mockResults.mdaSections[selectedSection]} />
        </div>
      </div>
    </div>
  )
}
