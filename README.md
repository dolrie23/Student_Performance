# 🎓 Student Graduation Prediction and Analysis

A Streamlit application that predicts a student's graduation status
based on academic, economic, administrative, and external factors.

## 📌 Project Background
Jaya Jaya Institute is a higher education institution established in 2000
with a strong track record of producing high-quality graduates. 
However, in recent years, the institution has faced a rising number of student dropouts.

A high dropout rate poses a serious challenge, as it may indicate issues in academic support or student engagement.
To address this, the institution aims to identify at-risk students as early as possible to provide targeted guidance
or intervention.

## 📌 Project Objectives
This project output is to analyze data and build web based prediction using streamlit to assist educational institutions
in identifying students at risk of Student Performance.

## 📌 Features
- User-friendly interface predictions manual input of 38 features
- Real-time prediction using trained model
- Lightweight deployment with Streamlit

## ⚙️ Tech Stack
- Python
- Streamlit
- Scikit-learn
- Pandas
- Seaborn
- Joblib
- Metabase

## 📊 Dataset
- Number of records: 4000++
- Number of features: 38 features
- Target variable: `Status` (1 = Graduated, 0 = Dropout)

## 🤖 Machine Learning
- Model used: Random Forest Classifier
- Feature importance visualized in metabase to identify key predictive factors
- Top 15 Importance Features are:
  - Curricular_units_approved
  - Curricular_units_grade
  - Tuition_fees_up_to_date
  - Curricular_units_evaluations
  - Scholarship_holder
  - Age_at_enrollment
  - Curricular_units_enrolled
  - Admission_grade
  - Course
  - Previous_qualification_grade
  - Application_mode
  - Fathers_occupation
  - Mothers_occupation
  - Fathers_qualification
  - Unemployment_rate


## 🚀 How to Run this project

1. **Clone repository:**
    ```bash
    git clone https://github.com/dolrie23/Student_Performance.git
    mkdir "Student_Performance"
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
   
3. **IF need to Run Notebook:**
   
     Need data.csv dan notebook environment
   
     ```
     $ conda create --n venv "python=<version>"
     $ conda activate venv
     ```
   
4. **Run Streamlit:**
     
    Make sure all these python are all fine:
     - prediction.py
     - options_mapping.py
     - streamlit_pred.py
   
     Execute this in your fav terminal:
      ```
      cd <your_local_venv>
   
      .\.venv\Scripts\activate
   
      streamlit run streamlit_pred.py
      ```
   
    or run streamlit from my streamlit community link here:
    ```
     https://student-performance-prediction-analysis.streamlit.app
    ```

5. **Open notebook for analysis:**
    
     Open `notebook.ipynb` using Jupyter Notebook to see full analysis.

6. **Dashboard Metabase:**
      
   - Email Metabase: danielsimanjuntak2305@gmail.com dan password: root123
   - Use filename `metabase.db.mv.db` to see the Visualization Dashboard in your local Metabase.
   - Dashboard contains importance factor that affected student performance.

## 🤸🏻‍♂️ Recomendation Actions

Based on our analysis, there are several actions would save the student from Dropout:

-  Provide tuition fee relief and installment options for financially disadvantaged students. Additionally, improve access to scholarships to support their academic journey.
- Limit or structure credit load (SKS) packages for first-year students to minimize the risk of academic failure in early semesters. 
- Offer evening or weekend classes (employee-class system) for older students to accommodate their unique circumstances and reduce the likelihood of low performance. 
- Actively monitor student performance using the dashboard and leverage the predictive model to identify students at risk of dropping out early, enabling timely intervention and support.

## ✅ Conclusion

By combining data analysis, visualization, and predictive modeling, this project enables Jaya Jaya Institut to 
proactively identify students at risk of dropping out. The actionable insights provided empower the institution 
to create data driven decisions and implement targeted strategies that support student success and reduce dropout rates.