"use client"

interface KPICardProps {
  label: string
  value: string
  change: "up" | "down"
  color: "success" | "warning" | "error"
}

export default function KPICard({ label, value, change, color }: KPICardProps) {
  const colorMap = {
    success: "text-[var(--color-success)]",
    warning: "text-[var(--color-warning)]",
    error: "text-[var(--color-error)]",
  }

  return (
    <div className="bg-[var(--color-surface)] border border-[var(--color-border)] rounded-lg p-6">
      <p className="text-[var(--color-text-secondary)] text-sm mb-3">{label}</p>
      <div className="flex items-end justify-between">
        <span className={`text-3xl font-bold ${colorMap[color]}`}>{value}</span>
        <span className={`text-lg ${colorMap[color]}`}>{change === "up" ? "↑" : "↓"}</span>
      </div>
    </div>
  )
}
