# 📄 OCR-Based Document Image Analysis System  

## 🚀 Overview  
The **OCR-Based Document Image Analysis System** automates text extraction from images using **Tesseract OCR** and **OpenCV**. This system efficiently converts scanned documents into editable text, reducing manual efforts and improving accuracy. Extracted text is processed with **Regex and NLP techniques**, stored in **Cassandra**, and presented via a **user-friendly web interface**.

---

## 📌 Features  
✅ **Automated OCR Processing** – Converts images into editable text.  
✅ **Image Preprocessing** – Uses OpenCV for better text clarity (Grayscale, Thresholding, Noise Reduction).  
✅ **Text Cleaning & Validation** – Post-processing with Regex & NLP.  
✅ **User Review & Editing** – Allows users to edit, copy, and export extracted text.  
✅ **Scalable Storage** – Stores extracted text in Cassandra for fast retrieval.  
✅ **Error Handling** – Manages unreadable text, duplicate data, and database failures.  
✅ **Intuitive Web Interface** – Simple UI for uploading and managing documents. 

## 🛠️ Tech Stack  
| Component    | Technology Used |
|-------------|----------------|
| **Frontend** | React.js (or HTML/CSS) |
| **Backend**  | Django / Flask |
| **OCR Engine** | Tesseract OCR, OpenCV |
| **Database** | Cassandra (NoSQL) |
| **Deployment** | Docker / AWS / Firebase (optional) |

---

## 🖥️ System Architecture  
📌 **Image Reference:** [`assets/system_architecture.png`](./assets/system_architecture.png)  

The architecture consists of a **React frontend** for user interaction, a **Flask/Django API** for OCR processing, and **Cassandra** for scalable data storage. The OCR engine (Tesseract + OpenCV) extracts text from images, which is then processed, validated, and stored.

---

## 🔄 System Flow  
📌 **Image Reference:** [`assets/system_flow.png`](./assets/system_flow.png)  

The **OCR processing flow** follows these steps:  
1️⃣ **User Uploads an Image** → JPEG, PNG, or PDF.  
2️⃣ **Image Preprocessing (OpenCV)** → Noise reduction, grayscale conversion, thresholding.  
3️⃣ **OCR Extraction (Tesseract)** → Extracts raw text from the processed image.  
4️⃣ **Text Post-Processing (Regex, NLP)** → Cleans and formats the extracted text.  
5️⃣ **Validation & Error Handling** → Checks for readability, duplicates, and inconsistencies.  
6️⃣ **Storage (Cassandra)** → Saves the final text for retrieval.  
7️⃣ **User Review & Export** → Allows users to edit, copy, or download text.  

---

## 📌 Usage
1️⃣ **Upload an Image** Open the web app and select a document image.

2️⃣ **OCR Processing** The backend processes the image, extracts text, and displays it in an editable format.

3️⃣ **Edit & Save** Users can make corrections and save/export the text in JSON/CSV format.

## 🚀 Key Performance Indicators (KPIs)
📌 **Image Reference:** `assets/kpi_chart.png`

✔️ **OCR Accuracy** – Measures correct text extraction percentage.  
✔️ **Processing Speed** – Average time taken per document.  
✔️ **Error Rate** – Percentage of failed OCR attempts.  
✔️ **User Engagement** – Frequency of text edits & corrections.  

## ⚠️ Exception Handling
📌 **Image Reference:** `assets/error_handling.png`

✅ **Unreadable Text:** If OCR fails, prompts the user to upload a clearer image.  
✅ **Duplicate Data:** Prevents redundant storage of the same extracted text.  
✅ **Database Errors:** Logs failures and retries the operation.  

## 📌 Future Enhancements
🚀 **Multilingual OCR Support** – Process documents in multiple languages.  
🚀 **Handwriting Recognition** – AI-based handwritten text detection.  
🚀 **Cloud Integration** – Save extracted text to Google Drive / AWS S3.  
🚀 **AI-Based Text Correction** – Improve extracted text accuracy using deep learning.  

## 📬 Contact & Support
For any queries, reach out to:  
📧 **Email:** atharvakarle2717@gmail.com  
🐙 **GitHub:** 
