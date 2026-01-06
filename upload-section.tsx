"use client"

import { useState } from "react"
import { FileUploadDropzone } from "@/components/file-upload-dropzone"
import ProcessingStatus from "@/components/processing-status"

export default function UploadSection() {
  const [isProcessing, setIsProcessing] = useState(false)
  const [uploadedFile, setUploadedFile] = useState<File | null>(null)
  const [processingStage, setProcessingStage] = useState<string>("")

  const handleFileUpload = async (file: File) => {
    setUploadedFile(file)
    setIsProcessing(true)
    setProcessingStage("Validating financial statements...")

    try {
      const formData = new FormData()
      formData.append("file", file)

      const response = await fetch("/api/process-financials", {
        method: "POST",
        body: formData,
      })

      if (!response.ok) throw new Error("Upload failed")

      setProcessingStage("Computing KPIs and deltas...")

      // Simulate processing stages
      await new Promise((resolve) => setTimeout(resolve, 1500))
      setProcessingStage("Generating embeddings...")

      await new Promise((resolve) => setTimeout(resolve, 1500))
      setProcessingStage("Creating RAG index...")

      await new Promise((resolve) => setTimeout(resolve, 1500))
      setProcessingStage("Generating MD&A narrative...")

      await new Promise((resolve) => setTimeout(resolve, 2000))
      setProcessingStage("Complete!")

      // Redirect to results after completion
      setTimeout(() => {
        window.location.href = "/results"
      }, 1000)
    } catch (error) {
      console.error("Error processing file:", error)
      setProcessingStage("Error processing file")
      setIsProcessing(false)
    }
  }

  return (
    <section id="upload" className="max-w-5xl mx-auto px-6 py-20">
      <div className="text-center mb-12">
        <h1 className="text-5xl font-bold text-[var(--color-text)] mb-4 text-balance">
          Generate MD&A from SEC Filings
        </h1>
        <p className="text-xl text-[var(--color-text-secondary)] text-balance">
          Upload financial statement extracts and get AI-powered Management Discussion & Analysis narratives with
          citations
        </p>
      </div>

      {!isProcessing ? (
        <FileUploadDropzone onFileSelect={handleFileUpload} />
      ) : (
        <ProcessingStatus stage={processingStage} />
      )}
    </section>
  )
}
