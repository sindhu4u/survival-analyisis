import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('my_model.h5')

# Define the function to make predictions
def predict_survival(creatinine, ejection_fraction):
    input_data = np.array([[creatinine, ejection_fraction]])
    prediction = model.predict(input_data)
    return "Survives" if prediction[0][0] < 0.5 else "Does not survive"

# Set up the Streamlit page configuration
st.set_page_config(page_title="Towards Healthier Hearts: A Survival Predictor ", layout="wide")

# Display the main title
st.title("Towards Healthier Hearts: Survival Predictor 🩺")
st.markdown(
    """
    **Cardiovascular diseases (CVDs) are the leading cause of death globally.** 
    According to the World Health Organization (WHO), an estimated 17.9 million people died 
    from CVDs in 2019, representing 32% of all global deaths. 
    CVDs are a group of disorders of the heart and blood vessels, 
    including coronary heart disease, cerebrovascular disease, rheumatic heart disease, 
    and other conditions.

    **Learn more about CVDs from the World Health Organization : 💓** [Cardiovascular diseases](https://www.who.int/health-topics/cardiovascular-diseases)
    """
)
# Sidebar content with image and description
logo_url = "./logo.jpeg"  
st.sidebar.image(logo_url, width=150)

st.sidebar.write("""
This innovative tool empowers physicians with an efficient way to predict heart failure survival. By focusing on two vital clinical indicators—**serum creatinine** and **ejection fraction**—this tool provides valuable insights that enhance decision-making and patient care. Embracing this kind of technology represents a significant leap toward personalized medicine, paving the way for improved health outcomes and more accurate predictions. With these kinds of tools, we're not just advancing medical technology—we're transforming the future of patient care for the better.
""")
st.sidebar.write("### Resources")
st.sidebar.markdown(
    """
    - 🔗 **[Heart Failure Dataset](https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records)**: Access the dataset used for this prediction tool.
    - 📄 **[Research Paper](https://doi.org/10.1186/s12911-020-1023-5)**: Read the research paper that discusses the methodology and findings used to create this tool.
    """
)
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://th.bing.com/th/id/OIP.-LmXKFgB1Xho4Z1pDzxAjQHaEK?rs=1&pid=ImgDetMain");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Layout for sliders
col1, col2 = st.columns(2)

with col1:
    creatinine = st.slider("Serum Creatinine (mg/dL)", min_value=0.5, max_value=9.40, step=0.1, format="%.1f", key="creatinine", help="Adjust the serum creatinine level")

with col2:
    ejection_fraction = st.slider("Ejection Fraction (%)", min_value=14, max_value=80, step=1, format="%d", key="ejection_fraction", help="Adjust the ejection fraction percentage")


# Handle button click and prediction
button_clicked = st.button("Predict")

if button_clicked:
    result = predict_survival(creatinine, ejection_fraction)
    if result == "Survives":
        st.success("Encouraging results! The tool predicts that the patient has a good chance of survival. Continue your excellent care and monitoring.")

        st.subheader("Believe in your body's ability to heal. You're on the road to recovery, and we wish that it is filled with hope, healing, and happiness!")
        st.write("""
            - **Early Detection of Complications:** Regular check-ups can help identify any signs of worsening conditions or new health issues early on. This allows for prompt intervention, potentially preventing complications and improving long-term outcomes.
            - **Monitor Treatment Effectiveness:** Check-ups can assess how well your current treatment plan is working in managing your heart health. This allows healthcare professionals to make any necessary adjustments to optimize your care.
            - **Improved Peace of Mind:** Knowing that you are being closely monitored and proactive steps are being taken towards maintaining your health can offer reassurance and reduce anxiety.
        """)

        st.subheader("Here are a few resources for you !")
        st.write("""
            - 🔗 **Healthy Lifestyle Resources:**
                - [Healthy Diet Tips](https://health.gov/myhealthfinder/health-conditions/heart-health/heart-healthy-foods-shopping-list)
                - [Exercise Guidelines](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7344739/)
                - [Stress Reduction Techniques](https://www.health.harvard.edu/heart-health/5-ways-to-de-stress-and-help-your-heart)
            - 🔗 **Patient Support Organizations:**
                - [Heart Foundation of India](https://www.heartfoundationindia.org.in/)
                - [National Health Mission](https://nhm.gov.in/)
        """)
    else:
        st.error("The patient may face difficulty. Consider additional diagnostic tests and consult with healthcare professionals for more insights.")

        st.subheader("Even in the most challenging times, your strength and resilience can make a difference. Regular monitoring is a powerful tool to support your journey towards better health!")
        st.write("""
            - **Early Intervention:** Regular monitoring can help identify potential problems earlier, allowing healthcare professionals to intervene and potentially improve outcomes.
            - **Informed Decision-Making:** Monitoring data can help guide treatment decisions and ensure you receive the most appropriate care.
            - **Proactive Care Planning:** Knowing a patient faces challenges allows for early discussions about care options and planning for the future.
        """)

        # Resources for negative prediction
        st.subheader("Here are a few resources for you !")
        st.write("""
            - 🔗 **Palliative Care Information:** 
                - [Palliative Care](https://www.palliativecare.in/palliative-care-for-cardiovascular-disease/)
            - 🔗 **Support Groups:**
                - [List of Support Groups](https://hearthealthindia.org/)
            - 🔗 **Counseling Services:**
                - [Counseling Resources](https://stanfordhealthcare.org/medical-treatments/c/cardiac-behavioral-counseling.html)
            - 🔗 **Clinical Trials:**
                - [Clinical Trials Registry - India (CTRI)](https://www.ctri.nic.in/)
        """)