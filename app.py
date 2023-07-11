import streamlit as st
import requests

# Define the base URL of your API
base_url = 'http://localhost:8000'

# Define the streamlit app code
def main():
    # Set page title and layout
    st.set_page_config(page_title='Medial Insurance Premium Prediction', layout='wide')
    
    # Center the title
    st.markdown("<h1 style='text-align: center;'>Medial Insurance Premium Prediction</h1>", unsafe_allow_html=True)
    
    # Create two columns for the input fields
    col1, col2 = st.columns(2)
    
    with col1:
        # Age input field
        age = st.number_input('Age', value=35)
        
        # BMI input field
        bmi = st.number_input('BMI', value=25.5)
        
        # Children input field
        children = st.number_input('Children', value=2)
    
    with col2:
        # Sex input field
        sex = st.selectbox('Sex', ['male', 'female'])
        
        # Smoker input field
        smoker = st.selectbox('Smoker', ['yes', 'no'])
        
        # Region input field
        region = st.selectbox('Region', ['southwest', 'southeast', 'northwest', 'northeast'])
    
    # Create the payload from user inputs
    payload = {
        'age': age,
        'sex': sex,
        'bmi': bmi,
        'children': children,
        'smoker': smoker,
        'region': region
    }
    
    # Make a POST request to the API
    response = requests.post(f'{base_url}/predict', json=payload)
    
    # Get the prediction from the response
    prediction = response.json()['prediction']
    
    # Display the prediction to the user

     # Center-align the prediction header
    st.markdown("<h2 style='text-align: center;'>Prediction</h2>", unsafe_allow_html=True)
    
    # Center-align the prediction message
    st.markdown(f"<p style='text-align: center;'>The predicted insurance premium is: ${round(prediction, 2)}</p>", unsafe_allow_html=True)
    
# Run the Streamlit app
if __name__ == '__main__':
    main()
