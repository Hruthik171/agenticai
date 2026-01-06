
# Automated MD&A Draft Generator

## Problem Statement

Writing the *MD&A (Management Discussion & Analysis)* section of financial reports takes a lot of time and manual effort.
Analysts need to study financial statements, calculate growth, and then write explanations in text form.

We tried to *automate the first draft of MD&A* using *financial data and AI*, so analysts can save time and focus more on review and decision-making.

---

## What Our Project Does

Our project reads *SEC financial statement data, analyzes the numbers, and **automatically generates an MD&A draft* in simple professional language.

The system:

* Reads financial data from SEC filings
* Calculates *Year-over-Year (YoY)* changes
* Converts numbers into meaningful financial sentences
* Uses AI to generate a *well-structured MD&A section*
* Saves the output as a readable report file

This is meant to be a *first draft*, not a final report.

---

## How the System Works (Simple Flow)

1. Load financial data from SEC dataset
2. Calculate growth metrics (YoY)
3. Convert financial results into text statements
4. Store statements in a vector database
5. Use AI to generate an MD&A narrative
6. Save the output as a Markdown file

---

## Technologies Used

* Python
* Pandas
* LangChain
* OpenAI API
* FAISS (Vector Database)

---

## Project Structure

<img width="478" height="155" alt="image" src="https://github.com/user-attachments/assets/a04d1035-83bf-4b11-a66c-b2150c3a144d" />


---

## How to Run the Project (VS Code)

1. Open the project folder in *VS Code*
2. Install required libraries:

   bash
   pip install -r requirements.txt
   
3. Add your OpenAI API key inside main.py
4. Run the project:

   bash
   python main.py
   
5. After execution, open output_mdna.md

   * Press *Ctrl + Shift + V* to view Markdown preview

---

## Output

The output is a *generated MD&A draft* that explains:

* Revenue trends
* Growth patterns
* Financial performance overview

The output file can be:

* Reviewed by humans
* Edited further
* Exported to reports

---

## Why This Project is Useful

* Reduces manual effort in report writing
* Improves consistency in financial explanations
* Scales easily for multiple companies
* Helps analysts focus on insights instead of writing

---

## Limitations

* This generates only a *first draft*
* Requires human validation
* Depends on quality of financial data

---

## Conclusion

This project shows how *financial analytics and AI* can be combined to *automate report drafting*.
It is a small step toward smarter and faster financial reporting.

---

### One-Line Summary

> This project automatically converts SEC financial data into an AI-generated MD&A draft to reduce manual reporting effort.
