# 🌺 Kaua’i RAG Tourism — Travel Assistant

Final project for the **Full Stack AI Engineering** course.  
This app is a **tourism assistant for Kaua’i (Hawaii)**, combining structured knowledge (JSON) and tourist guides (PDF) with **Retrieval Augmented Generation (RAG)**.

Users can ask questions about Kaua’i and filter results by category (Beach, Nature, Waterfall, etc.).  
The assistant streams answers in real time and provides reliable information from both structured and unstructured sources.

---

## ✅ Project Requirements

### Mandatory (all satisfied)
- ✔️ Written in Python.  
- ✔️ Uses at least one LLM (OpenAI GPT-3.5-turbo).  
- ✔️ Deployed as a Gradio app (ready for Hugging Face Space).  
- ✔️ Public repo with README.  
- ✔️ User provides their own API Key (secure handling).  
- ✔️ Contains scripts for data collection/curation (JSON + PDF loaders).  
- ✔️ README includes cost estimation (below $0.50 per test run).  

---

### Optional Functionalities Implemented (minimum 5, **we have 6**)
- ✔️ **Streaming responses** (real-time generation in Gradio).  
- ✔️ **Domain-specific assistant** (Tourism, not AI tutor).  
- ✔️ **Multiple data sources** (structured JSON + PDF tourist guide).  
- ✔️ **PDF ingestion** as part of the knowledge base.  
- ✔️ **Metadata filtering** (filter answers by category: Beach, Nature, Waterfall, etc.).  
- ✔️ **Validation examples** included in README (below).  

---

## 🧪 Validation Guide

The evaluator can validate that all requirements are satisfied by trying the examples below.

### 🌊 Beach
- **Question:** `Which beaches are the most famous in Kaua’i?`  
- **Category Filter:** `Beach`  
- **Expected Result:** Mentions **Poipu Beach** and **Hanalei Bay**.  

### 🏞 Nature
- **Question:** `What is Waimea Canyon?`  
- **Category Filter:** `Nature`  
- **Expected Result:** Description of Waimea Canyon as the "Grand Canyon of the Pacific".  

### 💧 Waterfall
- **Question:** `Tell me about Wailua Falls`  
- **Category Filter:** `Waterfall`  
- **Expected Result:** Description of Wailua Falls, tips for visiting, etc.  

### 🌿 Botanical Garden
- **Question:** `What is Allerton Garden?`  
- **Category Filter:** `Botanical Garden`  
- **Expected Result:** Description of the garden, its highlights, and recommended duration.  

---

⚠️ **Validation Tip**:  
If the user selects a category that does not match the question (e.g., *"What is Waimea Canyon?"* with filter *Beach*), the app will return:

```
⚠️ No results found for category Beach. Try another one.
```

This proves that **Metadata Filtering** is enforced and not just cosmetic.

---

## 💰 Cost Estimation

Typical usage with OpenAI `gpt-3.5-turbo` and a few questions costs **under $0.50**.  
All functionalities can be tested within this limit.

---

## 🖥️ Screenshots (Simulation)

- **App main interface**  
  <img width="1900" height="808" alt="image" src="https://github.com/user-attachments/assets/4d1b1f66-3d18-4aae-afbf-f8b53ed0aacd" />

- **Loading feedback (user experience improvement)**
  <img width="1886" height="184" alt="image" src="https://github.com/user-attachments/assets/bc34e781-4ffd-4d30-86d2-36bef100d158" /> 

This proves that **Metadata Filtering** is enforced and not just cosmetic.

---

## 💰 Cost Estimation

Typical usage with OpenAI `gpt-3.5-turbo` and a few questions costs **under $0.50**.  
All functionalities can be tested within this limit.

---

## 🖥️ Screenshots (Simulation)

- **App main interface**   
  <img width="1871" height="795" alt="image" src="https://github.com/user-attachments/assets/3e79dfdb-463c-4975-a505-19bab7195dc1" />

- **Loading feedback (user experience improvement)**  
  ```
  ⏳ Processing your question, please wait...
  ```
  
- **Metadata filtering example**
  ```
  ⚠️ No results found for category Beach. Try another one.
  ```
  
---

## 🚀 How to Run Locally

```bash
# 1. Clone repo
git clone https://github.com/<your-username>/kauai-rag-tourism
cd kauai-rag-tourism

# 2. Create virtual env
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate  # on Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Rebuild database
python scripts/index_data.py

# 5. Run app
python app.py
```

Then open [http://127.0.0.1:7860](http://127.0.0.1:7860) in your browser.

---

## 🌐 Deployment on Hugging Face

1. Push repo to Hugging Face Space.  
2. Ensure `app.py`, `requirements.txt`, `README.md`, and `data/` folder are included.  
3. Space will auto-install dependencies from `requirements.txt`.  

- Recommended Python version: **3.10+**  
- Make sure Space is set to **public**.  
- Evaluator can run everything directly without extra setup.  

---

## 📂 Repo Structure

```bash
kauai-rag-tourism/
├── app.py                # Main Gradio app
├── requirements.txt      # Dependencies
├── README.md             # Documentation
├── data/
│   ├── kauai.json        # Structured attractions data
│   └── kauai-maps.pdf    # Tourist guide PDF
├── scripts/
│   ├── index_data.py     # Indexer for JSON + PDF
│   ├── debug_metadata.py # Debug tool for categories
│   └── debug_beach.py    # Debug tool for beaches
└── db/                   # Vector database (auto-generated)
```

📌 Notes

- User must provide their **own OpenAI API Key** (`sk-...`) to use the app.  
- API Key is never exposed in code (security best practice).  
- This project was built with certification requirements in mind, but also serves as a **portfolio piece** for LLM + RAG applications.
