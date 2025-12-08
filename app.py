import streamlit as st
from model_app import predict_single_email

st.set_page_config(page_title="Mail Spam/Ham Classifier", page_icon="📧")

st.title("Mail Spam or Ham Classifier")
st.write(
   "Enter the content of an email below, and the model will classify it as Spam or Ham (Not Spam)."

#    "example ham=Yar i wanted 2 scold u yest but late already... I where got zhong se qing you? If u ask me b4 he ask me then i'll go out w u all lor. N u still can act so real."
# "example spam=0=Dear 0776xxxxxxx U've been invited to XCHAT. This is our final attempt to contact u! Txt CHAT to 86688 150p/MsgrcvdHG/Suite342/2Lands/Row/W1J6HL LDN 18yrs"

)

email_text = st.text_area("Paste the email text here:", height=200)

if st.button("Classify"):
    if not email_text.strip():
        st.warning("Please enter an email first.")
    else:
        label = predict_single_email(email_text)

        if label == 1:
            st.success("Prediction: Ham (Not Spam) ✅")
        else:
            st.error("Prediction: Spam ❌")


st.markdown("---")
st.caption("The email classifier powered by Streamlit \nDeveloped by Piyush Patel")
