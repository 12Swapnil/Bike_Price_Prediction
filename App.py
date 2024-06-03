
import numpy as np  # Import numpy for numerical operations
import pickle  # Import pickle for loading the machine learning model
import streamlit as st  # Import Streamlit for building web applications

# Load the machine learning model from the pickle file
pickle_in = open(r"C:\Users\Shantanu\Desktop\Bike\lr.pkl", "rb")

# Try to load the model, handle error if file not found
try:
    lr = pickle.load(pickle_in)
except FileNotFoundError:
    st.error("Model file (lr.pkl) not found. Please make sure the file exists.")

# Function to predict bike price using the loaded model
def predict_bike_price(year, seller_type, owner, km_driven, ex_showroom_price):
    prediction = lr.predict([[year, seller_type, owner, km_driven, ex_showroom_price]])
    return prediction

# Main function to create the Streamlit web app
def main():
  #  st.title("Bike Price Prediction")  # Set the title of the web app
    st.markdown(
        """
        <div style="background-color:tomato;padding:10px">
            <h2 style="color:white;text-align:center;">Bike Price Prediction </h2>
        </div>
        """,
        unsafe_allow_html=True,
    )  # Add HTML styling for the title

    # Input fields for user to input data for prediction
    year = st.number_input("Year", min_value=2000, max_value=2024, value=2015, step=1)
    seller_type = st.number_input("Seller Type(Individual:0, Dealer:1)", min_value=0, max_value=1, value=0, step=1)
    owner = st.number_input("Owner (1:1st, 2:2nd, 3:3rd, 4:4th)", min_value=0, max_value=3, value=0, step=1)
    km_driven = st.number_input("Km's Driven", min_value=1000, max_value=50000, value=5000, step=100)
    ex_showroom_price = st.number_input("Ex Showroom Price", min_value=50000, max_value=1500000, value=50000, step=1000)

    result = ""  # Variable to store the prediction result

    # Button to trigger prediction
    if st.button("Predict"):
        try:
            result = predict_bike_price(year, seller_type, owner, km_driven, ex_showroom_price)
            st.success(f"The predicted bike price is: {result[0]:.2f}")  # Display prediction result
        except Exception as e:
            st.error(f"An error occurred: {e}")  # Display error if prediction fails

# Entry point of the program
if __name__ == "__main__":
    main()
