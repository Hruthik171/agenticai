"use client"

interface MDASectionCardProps {
  section: {
    title: string
    content: string
    sources: string[]
  }
}

export default function MDASectionCard({ section }: MDASectionCardProps) {
  return (
    <div className="bg-[var(--color-surface)] border border-[var(--color-border)] rounded-lg p-8">
      <h2 className="text-2xl font-bold text-[var(--color-text)] mb-6">{section.title}</h2>

      <div className="prose prose-invert max-w-none mb-8">
        <p className="text-[var(--color-text)] leading-relaxed text-lg">{section.content}</p>
      </div>

      {/* Sources */}
      <div className="border-t border-[var(--color-border)] pt-6">
        <h4 className="text-sm font-semibold text-[var(--color-text-secondary)] mb-3">Sources</h4>
        <ul className="space-y-2">
          {section.sources.map((source, index) => (
            <li key={index} className="flex items-start gap-2 text-sm text-[var(--color-text-secondary)]">
              <span className="text-[var(--color-accent)] mt-1">→</span>
              <span>{source}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  )
}
