"use client"

interface ProcessingStatusProps {
  stage: string
}

const stages = [
  "Validating financial statements...",
  "Computing KPIs and deltas...",
  "Generating embeddings...",
  "Creating RAG index...",
  "Generating MD&A narrative...",
  "Complete!",
]

export default function ProcessingStatus({ stage }: ProcessingStatusProps) {
  const currentStageIndex = stages.indexOf(stage)

  return (
    <div className="space-y-8">
      <div className="bg-[var(--color-surface)] border border-[var(--color-border)] rounded-lg p-8">
        <div className="mb-8">
          <h3 className="text-lg font-semibold text-[var(--color-text)] mb-6">Processing Progress</h3>

          <div className="space-y-4">
            {stages.map((s, index) => (
              <div key={s} className="flex items-center gap-4">
                <div
                  className={`w-10 h-10 rounded-full flex items-center justify-center font-semibold text-sm transition-all ${
                    index < currentStageIndex
                      ? "bg-[var(--color-success)] text-[var(--color-background)]"
                      : index === currentStageIndex
                        ? "bg-[var(--color-accent)] text-[var(--color-background)]"
                        : "bg-[var(--color-border)] text-[var(--color-text-secondary)]"
                  }`}
                >
                  {index < currentStageIndex ? "✓" : index + 1}
                </div>
                <span
                  className={`${
                    index <= currentStageIndex ? "text-[var(--color-text)]" : "text-[var(--color-text-secondary)]"
                  }`}
                >
                  {s}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="h-1 bg-[var(--color-border)] rounded-full overflow-hidden">
          <div
            className="h-full bg-gradient-to-r from-[var(--color-accent)] to-[var(--color-success)] transition-all duration-500"
            style={{ width: `${((currentStageIndex + 1) / stages.length) * 100}%` }}
          />
        </div>
      </div>

      <div className="text-center">
        <div className="inline-flex items-center gap-2">
          <div className="w-2 h-2 bg-[var(--color-accent)] rounded-full animate-pulse"></div>
          <span className="text-[var(--color-text-secondary)]">Processing your file...</span>
        </div>
      </div>
    </div>
  )
}
