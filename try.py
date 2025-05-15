import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define a simple function
def greet(name):
    return f"Hello, {name}!"

# Create an alias for the function
greeting = greet

# Display the original function and its alias
st.title("Function Aliasing Visualization")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Original function output: {greet(name)}")
    st.write(f"Alias function output: {greeting(name)}")

    # Visualize the function aliasing using a line plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, label='sin(x)', color='blue')
    ax.plot(x, y + 0.5, label='sin(x) + 0.5', color='red', linestyle='--')
    ax.set_title("Function Aliasing Demonstration")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()

    st.pyplot(fig)

