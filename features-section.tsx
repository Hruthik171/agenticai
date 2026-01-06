"use client"

const features = [
  {
    icon: "📊",
    title: "Automated KPI Extraction",
    description: "Compute YoY/QoQ deltas and key financial metrics from raw statements automatically",
  },
  {
    icon: "🔍",
    title: "RAG-Powered Analysis",
    description: "Retrieve contextual insights from chunked filings using semantic search and embeddings",
  },
  {
    icon: "📝",
    title: "AI-Generated Narratives",
    description: "Create professional MD&A sections with trends, drivers, and risk factors using LLM",
  },
  {
    icon: "🔗",
    title: "Full Citation Tracking",
    description: "Every narrative point is linked back to source chunks for transparency and verification",
  },
]

export default function FeaturesSection() {
  return (
    <section id="features" className="max-w-7xl mx-auto px-6 py-20 border-t border-[var(--color-border)]">
      <h2 className="text-4xl font-bold text-[var(--color-text)] mb-16 text-center">
        Powerful Financial Analysis Engine
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {features.map((feature, index) => (
          <div
            key={index}
            className="bg-[var(--color-surface)] border border-[var(--color-border)] rounded-lg p-8 hover:border-[var(--color-accent)] transition-all group"
          >
            <div className="text-4xl mb-4 group-hover:scale-110 transition-transform">{feature.icon}</div>
            <h3 className="text-lg font-semibold text-[var(--color-text)] mb-2">{feature.title}</h3>
            <p className="text-[var(--color-text-secondary)]">{feature.description}</p>
          </div>
        ))}
      </div>
    </section>
  )
}
