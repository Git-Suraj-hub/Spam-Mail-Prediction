import numpy as np
import streamlit as st
import pandas as pd
import pickle
import  time
from sklearn.model_selection import train_test_split

pd.set_option('future.no_silent_downcasting', True)

model = pickle.load(open(r'model.sav', 'rb'))
Feautre_Extraction = pickle.load(open(r'Feature_Extraction.sav', 'rb'))

raw_mail_data = pd.read_csv(r'mail_data.csv')

raw_mail_data['Category'] = raw_mail_data['Category'].replace({'spam': 0, 'ham': 1})

X = raw_mail_data['Message']
Y = raw_mail_data['Category']

def SpamDetection(Input_Mail):
    input_data_features = Feautre_Extraction.transform([Input_Mail])


    # making prediction

    prediction = model.predict(input_data_features)
    print(prediction)

    if (prediction[0] == 1):
        return('✅ Real  mail ✅')

    else:
        return ('🤖 Spam mail 🚫 ')

def main():
    st.title("✉️ mail Spam Detection 📧")

    Input_Mail = st.text_input('Enter some text')
    if st.button("Detection"):
        progress_bar = st.progress(0)  # Initialize progress bar

        for i in range(100):  # Simulating loading
            time.sleep(0.03)
            progress_bar.progress(i + 1)  # Update progress

        result = SpamDetection(Input_Mail)
        st.success(result)


if __name__ == '__main__':
    main()

