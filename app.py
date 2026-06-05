import streamlit as st
import joblib

vectorizer = joblib.load('model/vectorizer.pkl')
classifier = joblib.load('model/classifier.pkl')

st.title("📩 Spam Email Classifier")
st.write("Enter a text message or email below to see if the AI flags it as spam.")

user_input = st.text_area("Message to classify:", height=150)

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("Please enter a message to check.")
    else:
        input_dtm = vectorizer.transform([user_input])
        prediction = classifier.predict(input_dtm)

        if prediction[0] == 1:
            st.error("🚨 ALERT: This message is classified as SPAM.")
        else:
            st.success("✅ SAFE: This message is classified as NOT SPAM.")