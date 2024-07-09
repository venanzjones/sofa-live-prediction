import streamlit as st
import numpy as np

# Preloaded model that always outputs 1 (for demonstration)
def predict_sofa_score():
    # Sample function, replace with your model prediction logic
    return 1

# Page title
st.set_page_config(page_title='Sofa Score Prediction', page_icon='🛋️')
st.title('🛋️ Sofa Score Prediction')

with st.expander('About this app'):
    st.markdown('**What can this app do?**')
    st.info('This app predicts the Sofa Score for the following day based on user input for weight, height, and current Sofa Score.')

    st.markdown('**How to use the app?**')
    st.warning('To use the app, enter your weight, height, and current Sofa Score in the sidebar, and the predicted Sofa Score for the following day will be displayed.')

# Sidebar for accepting input parameters
with st.sidebar:
    st.header('Input Parameters')
    weight = st.number_input('Weight (kg)', min_value=0.0, max_value=300.0, value=70.0, step=1.0)
    height = st.number_input('Height (cm)', min_value=0.0, max_value=300.0, value=170.0, step=1.0)
    pCO2 = st.number_input('pCO2 (mmHg)', min_value=0.0, max_value=300.0, value=170.0, step=1.0)
    pO2 = st.number_input('pO2 (mmHg)', min_value=0.0, max_value=300.0, value=170.0, step=1.0)
    SaO2 = st.number_input('SaO2 (%)', min_value=0.0, max_value=300.0, value=170.0, step=1.0)
    24sofascore = st.number_input('Initial Sofa Score', min_value=0, max_value=20, value=5, step=1)
    

# Predict Sofa Score for the following day
predicted_deterioration= predict_sofa_score(weight, height, sofascore)

# Display predicted Sofa Score
st.subheader('Predicted Deterioration after 24h ')
st.write('A patient under these conditions is predicted to deteriorate.')
