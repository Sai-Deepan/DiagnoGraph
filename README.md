# 🩺 DiagnoGraph: Streamlit-Based Patient Health Monitoring  

**DiagnoGraph** is a healthcare data analysis and visualization tool designed to help doctors and patients track health trends over time. It provides **interactive Streamlit dashboards** with patient-specific records, BMI calculation, and summary-based health status classification.  

---

## ✨ Features  

- 📊 **Streamlit Dashboard** for interactive visualization  
- 🧑‍⚕️ **Patient-specific analysis** – Enter a patient ID to view their data only  
- 📈 **Standardized data plots** for accurate comparisons  
- 🗓️ **Graphs of 2-week health records** using Matplotlib  
- 📝 **Summary Report** including:  
  - ⚖️ BMI (shown at the beginning and in the summary)  
  - 🧪 Values of multiple medical tests  
  - ✅ Final health status (Healthy / At Risk)  
  - 🩹 Predicted disease (if detected)  
- 🗄️ **MySQL integration** for storing and retrieving patient records  

---

## 📂 Project Structure  

- `app.py` – Main Streamlit application (frontend + visualization)  
- `data_processing.py` – Standardization and preprocessing  
- `database_setup.py` – MySQL connectivity and patient data management  
- `plots.py` – Graph generation using Matplotlib  

---

## 🎥 Demo  

📺 *Add demo video link here*  

---

## 🖼️ Project Images  

📸 *Add screenshots of:*  
- Streamlit dashboard  
- Patient graphs  
- Summary report with BMI and health status  

---

## 🛠️ Tech Stack  

### 🎨 Frontend (User Interaction)  
- ⚡ **Streamlit** — Interactive dashboard framework  
- 📊 **Matplotlib** — Graph plotting within Streamlit  

### 🔧 Backend (Core Logic & Database)  
- 🐍 **Python 3.10+** — Main programming language  
- 🧮 **NumPy & Pandas** — Data handling and standardization  
- 🗄️ **MySQL** — Database for storing patient health data  
- 🔗 **mysql-connector-python** — Database connectivity  

---

## 🚀 Getting Started  


### ✅ Prerequisites  
- Python 3.10+  
- MySQL server installed and running  
- Required Python packages (listed in `requirements.txt`)  

---

### ⚙️ Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Sai-Deepan/DiagnoGraph.git
   cd DiagnoGraph
2.Install required Python packages:
pip install -r requirements.txt

3.Setup the database:
python database_setup.py

### ▶️ Usage



