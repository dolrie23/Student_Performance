import pandas as pd
from PIL import Image
import streamlit as st
from prediction import prediction, preprocessor, preprocessing
from options_mapping import (
    application_mode_options, course_options, previous_qualification_options, mother_qualification_options,
    father_qualification_options, mother_occupation_options, father_occupation_options, nacionality_options
)

st.set_page_config(page_title="👩‍🎓 Student Performance Predictor 👨‍🎓", layout="wide")

image_file = 'Logo.png'
desired_width = 300
desired_height = 300
df = {}


col1, col2 = st.columns([2, 10])

with col1:
    # for idx, image_file in enumerate(image_files):
    img = Image.open(image_file)
    resized_img = img.resize((desired_width, desired_height))
    st.image(resized_img)

with col2:
    st.title("Prediksi Status Mahasiswa")
    st.markdown("""
        🏫 **Jaya Jaya Institute** is a higher education institution dedicated to improving academic quality and student well-being. With the increasing number of students facing dropouts or delays in graduation, there is a growing need for a system that can monitor and predict student risks early on.
    
        📊 This dashboard is designed to support academic and management teams in:
        - Predicting graduation or dropout likelihood based on student data  
    """)

st.markdown("""
    Please use the input panel to enter student information and view prediction results.
""")

st.sidebar.write("""
 Welcome to the **Student Status Prediction Dashboard** of **Jaya Jaya Institute**.
                 """)
add_selectitem = st.sidebar.selectbox("Pick your need!", "Student's Academic Performance")

st.markdown("### 🧑 Faktor Internal")
st.markdown("#### Curricular Activity")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    Curricular_units_1st_sem_credited = st.number_input("1st Sem Credited Units", min_value=0, max_value=50, value=0)
with col2:
    Curricular_units_1st_sem_approved = st.number_input("1st Sem Approved Units", min_value=0, max_value=50, value=0)
with col3:
    Curricular_units_1st_sem_enrolled = st.number_input("1st Sem Enrolled Units", min_value=0, max_value=50, value=0)
with col4:
    Curricular_units_1st_sem_evaluations = st.number_input("1st Sem Evaluations", min_value=0, max_value=50, value=0)
with col5:
    Curricular_units_1st_sem_without_evaluations = st.number_input("1st Sem Without Evaluations", min_value=0, max_value=50, value=0)


col6, col7, col8, col9, col10 = st.columns(5)
with col6:
    Curricular_units_2nd_sem_credited = st.number_input("2nd Sem Credited Units", min_value=0, max_value=50, value=0)
with col7:
    Curricular_units_2nd_sem_approved = st.number_input("2nd Sem Approved Units", min_value=0, max_value=50, value=0)
with col8:
    Curricular_units_2nd_sem_enrolled = st.number_input("2nd Sem Enrolled Units", min_value=0, max_value=50, value=0)
with col9:
    Curricular_units_2nd_sem_evaluations = st.number_input("2nd Sem Evaluations", min_value=0, max_value=50, value=0)
with col10:
    Curricular_units_2nd_sem_without_evaluations = st.number_input("2nd Sem Without Evaluations",
                                                                   min_value=0, max_value=50, value=0)

col6a, col6b = st.columns(2)
with col6a:
    Curricular_units_1st_sem_grade = st.slider("1st Sem Grade", min_value=0.0, max_value=20.0, value=10.0)
with col6b:
    Curricular_units_2nd_sem_grade = st.slider("2nd Sem Grade", min_value=0.0, max_value=20.0, value=10.0)

st.markdown("#### Biodata")
col11, col12, col13, col14, col15 = st.columns(5)
with col11:
    Scholarship_holder = st.selectbox("Scholarship Holder", options=["Yes (1)", "No (0)"], index=1)
with col12:
    Educational_special_needs = st.selectbox("Special Needs", options=["Yes (1)", "No (0)"], index=1)
with col13:
    Age_at_enrollment = st.number_input("Umur", min_value=17, max_value=70, step=1)
with col14:
    Gender = st.selectbox(label="Gender", options=["Male(1)", "Female(0)"], index=0)
with col15:
    Marital_status = st.selectbox(label="Marital Status",
                                  options=["1 – single", "2 – married", "3 – widower",
                                           "4 – divorced", "5 – facto union", "6 – legally separated"],
                                  index=0)

Admission_grade = st.slider(label='Admission Grade', min_value=95, max_value=190, value=100)

st.markdown("### 🤸🏻‍♂️ External Factors")
st.markdown("#### Family")
col1, col2, col3, col4 = st.columns(4)
with col1:
    Mothers_qualification_label = st.selectbox("Mother's Qualification", list(mother_qualification_options.keys()))
    Mothers_qualification_val = mother_qualification_options[Mothers_qualification_label]
with col2:
    Fathers_qualification_label = st.selectbox("Father's Qualification", list(father_qualification_options.keys()))
    Fathers_qualification_val = father_qualification_options[Fathers_qualification_label]
with col3:
    Mothers_occupation_label = st.selectbox("Mother's Occupation", list(mother_occupation_options.keys()))
    Mothers_occupation_val = mother_occupation_options[Mothers_occupation_label]
with col4:
    Fathers_occupation_label = st.selectbox("Father's Occupation", list(father_occupation_options.keys()))
    Fathers_occupation_val = father_occupation_options[Fathers_occupation_label]

st.markdown("#### Nation")
col5, col6, col7 = st.columns(3)
with col5:
    Nacionality_label = st.selectbox("Nationality", list(nacionality_options.keys()))
    Nacionality_val = nacionality_options[Nacionality_label]
with col6:
    Displaced = st.selectbox(label="Displaced", options=["Yes (1)", "No (0)"], index=1)
with col7:
    International = st.selectbox(label="International Student", options=["Yes (1)", "No (0)"], index=1)

st.markdown("### 🗃️ Administrative Factors")
st.markdown("####  Applications")
col1, col2, col3, col4 = st.columns(4)
with col1:
    Application_mode_label = st.selectbox("Application Mode", list(application_mode_options.keys()))
    Application_mode_val = application_mode_options[Application_mode_label]
with col2:
    Application_order = st.slider("Application Order", 0, 9, 1)
with col3:
    Course_label = st.selectbox("Course", list(course_options.keys()))
    Course_mode_val = course_options[Course_label]
with col4:
    Daytime_evening_attendance = st.selectbox(label="Attendance Regime", options=["Daytime (1)", "Evening (0)"], index=0)

st.markdown("#### Past Background")
col5, col6 = st.columns(2)
with col5:
    Previous_qualification_label = st.selectbox("Previous Qualification", list(previous_qualification_options.keys()))
    Previous_qualification_val = previous_qualification_options[Previous_qualification_label]
with col6:
    Previous_qualification_grade = st.slider("Previous Qualification Grade", 0.0, 200.0, 100.0)

st.markdown("### 💰 Economic Factors")
col1, col2 = st.columns(2)
with col1:
    Debtor = st.selectbox("Debtor", ["Yes (1)", "No (0)"], index=1)
with col2:
    Tuition_fees_up_to_date = st.selectbox(label="Tuition Fees Up-to-Date", options=["Yes (1)", "No (0)"], index=0)

col4, col5, col6 = st.columns(3)
with col4:
    Unemployment_rate = st.slider("Unemployment Rate (%)", 0.0, 100.0, 10.0)
with col5:
    Inflation_rate = st.slider("Inflation Rate (%)", -5.0, 20.0, 2.0)
with col6:
    GDP = st.slider("GDP Growth (%)", -10.0, 10.0, 1.5)

if st.button("Predict Student Status"):
    Gender = 1 if "Male" in Gender else 0
    Marital_status = int(Marital_status.split("–")[0].strip())
    Displaced = int(Displaced.split()[1][1])
    International = int(International.split()[1][1])
    Scholarship_holder = int(Scholarship_holder.split()[1][1])
    Debtor = int(Debtor.split()[1][1])
    Daytime_evening_attendance = int(Daytime_evening_attendance.split()[1][1])
    Tuition_fees_up_to_date = int(Tuition_fees_up_to_date.split()[1][1])

    data_dict = {
        'Marital_status': Marital_status,
        'Application_mode': Application_mode_val,
        'Application_order': Application_order,
        'Course': Course_mode_val,
        'Daytime_evening_attendance': Daytime_evening_attendance,
        'Previous_qualification': Previous_qualification_val,
        'Previous_qualification_grade': Previous_qualification_grade,
        'Nacionality': Nacionality_val,
        'Mothers_qualification': Mothers_qualification_val,
        'Fathers_qualification': Fathers_qualification_val,
        'Mothers_occupation': Mothers_occupation_val,
        'Fathers_occupation': Fathers_occupation_val,
        'Admission_grade': Admission_grade,
        'Displaced': Displaced,
        'Educational_special_needs': Educational_special_needs,
        'Debtor': Debtor,
        'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
        'Gender': Gender,
        'Scholarship_holder': Scholarship_holder,
        'Age_at_enrollment': Age_at_enrollment,
        'International': International,
        'Curricular_units_1st_sem_credited': Curricular_units_1st_sem_credited,
        'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_evaluations': Curricular_units_1st_sem_evaluations,
        'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
        'Curricular_units_1st_sem_without_evaluations': Curricular_units_1st_sem_without_evaluations,
        'Curricular_units_2nd_sem_credited': Curricular_units_2nd_sem_credited,
        'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_evaluations': Curricular_units_2nd_sem_evaluations,
        'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
        'Curricular_units_2nd_sem_without_evaluations': Curricular_units_2nd_sem_without_evaluations,
        'Unemployment_rate': Unemployment_rate,
        'Inflation_rate': Inflation_rate,
        'GDP': GDP,
        'Status': None
    }

    df = pd.DataFrame(data_dict, index=[0])
    prediction_result = prediction(df)
    result = "Graduate" if prediction == 1 else "Dropout"
    st.success(f"🎯 Prediction Student: **{result}**")


