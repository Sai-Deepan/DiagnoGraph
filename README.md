#  DiagnoGraph: Streamlit-Based Patient Health Diagnosis Report

**DiagnoGraph** is a healthcare data analysis and visualization tool designed to help doctors and patients track health trends over time. It provides **interactive Streamlit dashboards** with patient-specific records, BMI calculation, and summary-based health status classification using graphs and values.  

---

##  Features  

-  **Streamlit Dashboard** for interactive visualization  
-  **Patient-specific analysis** – Enter a patient ID to view their data only  
-  **Standardized data plots** for accurate comparisons  
-  **Graphs of 2-week health records** using Matplotlib  
-  **Summary Report** including:  
  -  BMI (shown at the beginning and in the summary)  
    - Values of multiple medical tests  
  -  Final health status (Healthy / At Risk)  
  -  Predicted disease (if detected)  
-  **MySQL integration** for storing and retrieving patient records  

---

##  Project Structure  

-  Main Streamlit application (frontend + visualization)  
-  Backend(Standardization and preprocessing  )
-  Backend( MySQL connectivity and patient data management  )
- Graph generation using Matplotlib  

---

##  Demo  

 *Add demo video link here*  

---

##  Project Images  

 *Add screenshots of:*  
- Streamlit dashboard  
- Patient graphs  
- Summary report with BMI and health status  

---

##  Tech Stack  

###  Frontend (User Interaction)  
-  **Streamlit** — Interactive dashboard framework  
-  **Matplotlib** — Graph plotting within Streamlit  

###  Backend (Core Logic & Database)  
-  **Python 3.10+** — Main programming language  
-  **NumPy & Pandas** — Data handling and standardization  
-  **MySQL** — Database for storing patient health data  
-  **mysql-connector-python** — Database connectivity  

---

##  Getting Started  


###  Prerequisites  
- Python 3.10+  
- MySQL server installed and running  
- Required Python packages (listed in `requirements.txt`)  

---

###  Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Sai-Deepan/DiagnoGraph.git
   cd DiagnoGraph
2.Install required Python packages:
-pip install -r requirements.txt

3.Setup the database:
-python database_setup.py

###  Usage Displays 2-week graphs of different test results

 Generates summary with BMI and test values

 Shows health status (Healthy / At Risk)

 Predicts potential disease if health deviates from normal


1.Start the Streamlit application:

streamlit run app.py

2.Enter a patient ID in the interface.

##  Database Setup Instructions  

DiagnoGraph uses **MySQL** to manage patient health records. Follow these steps to set it up:  

### 1. Install MySQL  
- **Windows/Mac:** Download from [MySQL Downloads](https://dev.mysql.com/downloads/installer/)  
  ```bash
  sudo apt update
  sudo apt install mysql-server

### 2.Create Database
### 3.Create Table for Patient Records
### 4.Create Python Database Connection
### 5.Verify data

##  Why DiagnoGraph?  

Monitoring health over time is critical. **DiagnoGraph** combines **data standardization, visualization, and health summarization** with a simple **Streamlit interface**, making it easier for doctors and patients to:  

-  **Track progress**  
-  **Understand health status**  
- **Make informed decisions**

## Contributors:
## 1)Deepan Sai
## 2)Aadithya V
## 3)Viswasainath Vijayakumar
## 4)Deepak R










