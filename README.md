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

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/jriya-31/Image-Analysis.git
cd OCR-Document-Analysis
