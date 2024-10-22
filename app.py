import streamlit as st  # Import Streamlit for the web interface
import numpy as np      # Import Numpy for numerical operations
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Title of the app
st.title("Interactive Linear Regression Demo")

# Create sliders for the user to adjust the intercept and slope
intercept = st.slider('Intercept (φ₀)', min_value=-5.0, max_value=5.0, value=0.0)
slope = st.slider('Slope (φ₁)', min_value=-5.0, max_value=5.0, value=1.0)

# Generate data (Input and Output) based on the intercept and slope
x = np.linspace(0, 2, 100)  # Create 100 data points between 0 and 2
y = intercept + slope * x   # Simple linear regression equation

# Create a plot of the line
fig, ax = plt.subplots()
ax.plot(x, y, label=f'y = {intercept} + {slope}x')  # Plot the line with a label
ax.set_xlabel('Input, x')  # Label for x-axis
ax.set_ylabel('Output, y')  # Label for y-axis
ax.legend()  # Display the label

# Display the plot in the Streamlit app
st.pyplot(fig)
