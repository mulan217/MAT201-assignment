import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title("🏔️ Gradient Ascent Visualizer: Climbing the Math Mountain")
st.write("This app helps students visualize **Gradient Vectors** and the **Steepest Ascent** path on a 3D surface.")

# Sidebar for user input
st.sidebar.header("Settings")
function_choice = st.sidebar.selectbox(
    "Choose a Function f(x,y):",
    ("Simple Paraboloid: x^2 + y^2", "Complex Multi-Peak: x * exp(-x^2 - y^2)")
)

# Define grid
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)

# Logic for functions
if function_choice == "Simple Paraboloid: x^2 + y^2":
    Z = X**2 + Y**2
    st.latex(r"f(x, y) = x^2 + y^2")
    # Gradient calculation
    U = 2*X # df/dx
    V = 2*Y # df/dy
else:
    Z = X * np.exp(-X**2 - Y**2)
    st.latex(r"f(x, y) = x e^{-x^2 - y^2}")
    # Gradient calculation (approximate for vis)
    U, V = np.gradient(Z, x[1]-x[0], y[1]-y[0])

# Plotting
fig = plt.figure(figsize=(10, 6))

# 3D Plot
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_title("3D Surface View")
ax.set_xlabel("x")
ax.set_ylabel("y")

# 2D Contour Plot with Quiver (Gradient Arrows)
ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, cmap='viridis')
# Plot arrows (Gradient Field)
ax2.quiver(X, Y, U, V, color='white', alpha=0.5)
ax2.set_title("Contour Map with Gradient Vectors (Arrows)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

st.pyplot(fig)

st.info("💡 The **White Arrows** point in the direction of steepest ascent (The Gradient). The magnitude tells us how steep the slope is!")
