import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def hermite_polynomial(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * hermite_polynomial(n - 1, x) - 2 * (n - 1) * hermite_polynomial(n - 2, x)

def hermite_equation(n):
    if n == 0:
        return r"H_0(x) = 1"
    elif n == 1:
        return r"H_1(x) = 2x"
    else:
        return   r"H_{%d}(x) = 2x \cdot H_{%d}(x) - 2(%d) \cdot H_{%d}(x)" % (n, n-1, n-1, n-2)

def main():
    st.title('Hermite Polynomials Visualization and Applications')

    st.markdown("---")

    st.header('Hermite Polynomials Visualization')

    # Input the maximum order of Hermite polynomial
    max_order = st.slider('Maximum Order of Hermite Polynomial', 0, 10, 5)

    # Generate x values
    x_values = np.linspace(-2, 2, 400)

    # Plot Hermite polynomials
    fig, ax = plt.subplots(figsize=(10, 6))

    for n in range(max_order + 1):
        y_values = [hermite_polynomial(n, x) for x in x_values]
        ax.plot(x_values, y_values, label=f'$H_{n}(x)$')

    ax.set_xlabel('x')
    ax.set_ylabel('Hermite Polynomials')
    ax.set_title('Hermite Polynomials')
    ax.legend()
    ax.grid(True)

    # Display the plot
    st.pyplot(fig)

    st.markdown("---")

    st.header('Hermite Polynomial Equations')

    # Display the equations
    for n in range(max_order + 1):
        st.latex(hermite_equation(n))

    st.markdown("---")

    st.header('Applications of Hermite Polynomials')

    # Display Applications
    st.markdown("""
    - **Quantum Mechanics:** Hermite polynomials arise in the solutions of the quantum harmonic oscillator problem.
    - **Signal Processing:** They are used in the analysis of signals and noise.
    - **Probability Theory:** Hermite polynomials are related to the Hermite distribution in probability theory.
    - **Heat Transfer:** In heat transfer problems, Hermite polynomials are used to solve partial differential equations.
    """)

if __name__ == "__main__":
    main()