# Automated Expense Extraction from Receipts using Computer Vision & OCR  
Jagadeesh kumar Sellappan – University of San Diego, Fall 2025  

## Project Overview  
This project builds an end-to-end computer vision pipeline that automatically extracts key financial information (Vendor, Date, Total Amount, Address) from real-world receipt photos/scans using:  
- Classic OpenCV preprocessing (deskewing, denoising, contrast enhancement)  
- State-of-the-art OCR & document understanding models (TrOCR / Donut / LayoutLMv3)  
- Structured post-processing and entity extraction  

The extracted data is automatically added to a personal expense tracker web app built with **Streamlit**.

## Why This Project?  
Manual expense entry is slow and error-prone. This system enables instant, accurate expense logging from a simple phone photo — useful for personal finance, corporate reimbursement, bookkeeping, and accounting automation.

## Dataset  
**ICDAR 2019 SROIE (Scanned Receipts OCR and Information Extraction)**  
- 626 whole receipt images (training)  
- 347 whole receipt images (testing)  
- Real-world variations: skew, blur, shadows, fading, different layouts, phone vs scanner  
- Official competition dataset → entity-level annotations and public leaderboard scoring script  

Link: https://rrc.cvc.uab.es/?ch=13

## Current Progress (as of November 2025)
| Task                            | Status      | Notes                              |
|---------------------------------|-------------|------------------------------------|
| Repository & project setup      | Completed   |                                    |
| SROIE dataset downloaded        | Completed   | Train + test + annotations         |
| Exploratory Data Analysis       | In Progress | Visualizing difficult cases        |
| Baseline OCR (EasyOCR/TrOCR)    | In Progress |                                    |
| Preprocessing pipeline          | Planned     | Deskew, denoise, thresholding      |
| Full extraction + evaluation    | Planned     | Official SROIE F1 scoring          |
| Streamlit expense tracker app   | Planned     | With live receipt upload           |
| Technical report & presentation | Not Started |                                    |

## Repository Structure (will grow)
