"use client"

import Link from "next/link"

export default function Header() {
  return (
    <header className="border-b border-[var(--color-border)] sticky top-0 z-50 bg-[var(--color-surface)] backdrop-blur-sm">
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2">
          <div className="w-10 h-10 rounded-lg bg-[var(--color-accent)] flex items-center justify-center">
            <span className="text-[var(--color-background)] font-bold text-lg">MD</span>
          </div>
          <span className="text-xl font-bold text-[var(--color-text)]">Automated MD&A</span>
        </Link>

        <nav className="flex items-center gap-8">
          <Link
            href="#features"
            className="text-[var(--color-text-secondary)] hover:text-[var(--color-text)] transition"
          >
            Features
          </Link>
          <Link href="#upload" className="text-[var(--color-text-secondary)] hover:text-[var(--color-text)] transition">
            Get Started
          </Link>
        </nav>
      </div>
    </header>
  )
}
