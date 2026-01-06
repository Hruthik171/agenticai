"use client"

import type React from "react"

import { useState } from "react"

interface FileUploadDropzoneProps {
  onFileSelect: (file: File) => void
}

export function FileUploadDropzone({ onFileSelect }: FileUploadDropzoneProps) {
  const [isDragging, setIsDragging] = useState(false)

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(true)
  }

  const handleDragLeave = () => {
    setIsDragging(false)
  }

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault()
    setIsDragging(false)

    const file = e.dataTransfer.files[0]
    if (
      file &&
      (file.type === "text/csv" || file.type === "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    ) {
      onFileSelect(file)
    }
  }

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      onFileSelect(file)
    }
  }

  return (
    <div
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
      className={`border-2 border-dashed rounded-lg p-12 text-center transition-all ${
        isDragging
          ? "border-[var(--color-accent)] bg-[var(--color-surface)]"
          : "border-[var(--color-border)] bg-[var(--color-surface-secondary)] hover:border-[var(--color-text-secondary)]"
      }`}
    >
      <div className="mb-6">
        <svg
          className="w-16 h-16 mx-auto text-[var(--color-accent)]"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
          />
        </svg>
      </div>

      <h3 className="text-xl font-semibold text-[var(--color-text)] mb-2">Drop your financial statements here</h3>
      <p className="text-[var(--color-text-secondary)] mb-6">Supports CSV and Excel files (.xlsx)</p>

      <label>
        <input type="file" accept=".csv,.xlsx" onChange={handleFileInput} className="hidden" />
        <button
          onClick={(e) => {
            e.preventDefault()
            ;(e.currentTarget as HTMLElement).previousElementSibling?.querySelector("input")?.click()
          }}
          className="inline-block px-6 py-2 bg-[var(--color-accent)] text-[var(--color-background)] font-semibold rounded-lg hover:bg-[var(--color-accent-hover)] transition"
        >
          Browse Files
        </button>
      </label>
    </div>
  )
}
