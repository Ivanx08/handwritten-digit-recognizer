import streamlit as st
from streamlit_drawable_canvas import st_canvas
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
from keras.models import load_model

# Load the pre-trained digit recognition model
# This is cached so it loads only once when the app starts
@st.cache_resource
def load_digit_model():
    return tf.keras.models.load_model("digit_recognizer_model.keras")

model = load_digit_model()

# Streamlit page configuration
st.set_page_config(page_title="Handwritten Digit Recognizer", layout="wide")

# UI Title and Instructions
st.markdown("<h2 style='text-align: center;'>🖌️ Handwritten Digit Recognizer</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Draw a digit (0–9) and let's see if the model gets it right!</p>", unsafe_allow_html=True)
st.markdown("---")

# Two-column layout: left for canvas, right for prediction result
col1, col2 = st.columns([2, 1])

with col1:
    # Create a drawing canvas for the user to draw digits
    canvas = st_canvas(
        fill_color="white",             # Color to fill the drawing
        stroke_width=12,                # Pen thickness
        stroke_color="white",           # Pen color
        background_color="black",       # Background color of canvas
        height=280,
        width=280,
        drawing_mode="freedraw",        # Allow freehand drawing
        key="canvas",
    )

    # Button to trigger prediction
    predict_button = st.button("Predict")

with col2:
    # When the button is clicked and image exists
    if predict_button and canvas.image_data is not None:
        # Extract and preprocess the image for prediction
        img = canvas.image_data[:, :, 0]      # Get grayscale channel
        img = cv2.resize(img, (28, 28))       # Resize to 28x28 pixels
        img = img / 255.0                     # Normalize pixel values
        img = img.reshape(1, 28, 28, 1)       # Reshape to match model input

        # Make prediction using the model
        prediction = model.predict(img)
        predicted_digit = np.argmax(prediction)

        # Display the processed image
        st.markdown("#### Processed Input")
        st.image(img.reshape(28, 28), width=150)

        # Display the predicted digit
        st.success(f"✅ **Predicted Digit: {predicted_digit}**")

        # User feedback section
        with st.expander("Was the prediction correct?", expanded=True):
            feedback = st.radio("Select an option:", ["Yes", "No"], horizontal=True)

            if feedback:
                st.markdown("✔️ Thank you for the feedback! Let's do it again.")


# Signature block
st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>"
    "Made with ❤️ | Author: <strong>Shivam Bhati</strong><br>"
    "<em>Codec Technologies Internship Project</em>"
    "</div>",
    unsafe_allow_html=True
)

