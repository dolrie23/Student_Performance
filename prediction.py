import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

model = joblib.load('model/Best_model.pkl')
preprocessor = joblib.load('model/preprocessor.pkl')


def preprocessing(df):
    df['Curricular_units_approved'] = df['Curricular_units_1st_sem_approved'] + df['Curricular_units_2nd_sem_approved']
    df['Curricular_units_grade'] = df['Curricular_units_1st_sem_grade'] + df['Curricular_units_2nd_sem_grade']
    df['Curricular_units_evaluations'] = (df['Curricular_units_1st_sem_evaluations'] +
                                          df['Curricular_units_2nd_sem_evaluations'])
    df['Curricular_units_credited'] = df['Curricular_units_1st_sem_credited'] + df['Curricular_units_2nd_sem_credited']
    df['Curricular_units_enrolled'] = df['Curricular_units_1st_sem_enrolled'] + df['Curricular_units_2nd_sem_enrolled']
    df['Curricular_units_without_evaluations'] = (df['Curricular_units_1st_sem_without_evaluations'] +
                                                  df['Curricular_units_2nd_sem_without_evaluations'])

    df.drop(columns=['Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_approved',
                     'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_credited',
                     'Curricular_units_1st_sem_enrolled',
                     'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_approved',
                     'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_credited',
                     'Curricular_units_2nd_sem_enrolled',
                     'Curricular_units_2nd_sem_without_evaluations', 'Curricular_units_1st_sem_without_evaluations'],
            inplace=True)
    df['Status'] = df['Status'].map({'Graduate': 0, 'Dropout': 1})
    preprocessed_data = preprocessor.transform(df)
    # print(preprocessed_data.shape)
    selected_df = df[['Curricular_units_approved', 'Curricular_units_grade',
                      'Tuition_fees_up_to_date','Curricular_units_evaluations',
                      'Scholarship_holder', 'Age_at_enrollment',
                      'Curricular_units_enrolled', 'Admission_grade',
                      'Course', 'Previous_qualification_grade',
                      'Application_mode', 'Fathers_occupation',
                      'Mothers_occupation', 'Fathers_qualification', 'Unemployment_rate']]
    return selected_df


def prediction(df):
    preprocessed_data = preprocessing(df)
    predictions = model.predict(preprocessed_data)
    categorical_predictions = ['Graduate' if pred == 0 else 'Dropout' for pred in predictions]

    return categorical_predictions


def prediction_dataset(df):
    preprocessed_data = preprocessing(df)
    predictions = model.predict(preprocessed_data)
    probability = model.predict_proba(preprocessed_data)
    df['Probability'] = probability[:, 1]
    df['Status'] = predictions
    df.to_csv('Prediction_Data_Result.csv', index=False)
    return df


if __name__ == '__main__':
    pil = input('Ingin prediksi dataset(Y) atau seuntaian data(N)?\nType your Answer: ')
    if pil == 'Y' or pil == 'y':
        sample = {
            'Marital_status': 1,
            'Application_mode': 1,
            'Application_order': 5,
            'Course': 9254,
            'Daytime_evening_attendance': 1,
            'Previous_qualification': 1,
            'Previous_qualification_grade': 101.0,
            'Nacionality': 1,
            'Mothers_qualification': 3,
            'Fathers_qualification': 19,
            'Mothers_occupation': 3,
            'Fathers_occupation': 9,
            'Admission_grade': 98.9,
            'Displaced': 1,
            'Educational_special_needs': 0,
            'Debtor': 0,
            'Tuition_fees_up_to_date': 1,
            'Gender': 1,
            'Scholarship_holder': 0,
            'Age_at_enrollment': 20,
            'International': 0,
            'Curricular_units_1st_sem_credited': 0,
            'Curricular_units_1st_sem_enrolled': 6,
            'Curricular_units_1st_sem_evaluations': 10,
            'Curricular_units_1st_sem_approved': 4,
            'Curricular_units_1st_sem_grade': 13.0,
            'Curricular_units_1st_sem_without_evaluations': 0,
            'Curricular_units_2nd_sem_credited': 0,
            'Curricular_units_2nd_sem_enrolled': 6,
            'Curricular_units_2nd_sem_evaluations': 6,
            'Curricular_units_2nd_sem_approved': 6,
            'Curricular_units_2nd_sem_grade': 13.0,
            'Curricular_units_2nd_sem_without_evaluations': 0,
            'Unemployment_rate': 12.4,
            'Inflation_rate': 0.5,
            'GDP': 1.79,
            'Status': None,
        }
        data = pd.DataFrame(sample, index=[0])
        result = prediction(data)
        print(f"Prediction result: {result}")
    else:
        data = pd.read_csv('Prediction_Data.csv')
        # print("Kolom dalam file CSV:", data.columns.tolist())
        result = prediction_dataset(data)
