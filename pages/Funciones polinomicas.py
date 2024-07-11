import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

st.title('Tipos de funciones')

st.markdown('''
## Funciones polinómicas

Una función polinómica es una función matemática que se expresa como una suma de monomios. Un monomio es una expresión algebraica compuesta por un coeficiente numérico (que puede ser cero) y una o varias variables elevadas a exponentes enteros no negativos.

En otras palabras, una función polinómica se puede escribir como:

''')

st.latex("f(x)={a}_{0}+{a}_{1}x+{a}_{2}{x}^{2}+...+{a}_{n}{x}^{n}")
st.markdown('''
    Existen cuatro tipos de funciones polinómicas:''')
with st.container(border=True):
    st.markdown('''
    - **Funciones lineales:** Son funciones donde m y b son constantes, m es diferente a cero y se expresan de la siguiente forma:
    ''')

    st.latex("f(x)=mx+b")
    st.latex("f(x)=5x+8")
with st.container(border=False):
    st.markdown("**Digite**")
    col1, col2 = st.columns(2)
    with col1:
        m=float(st.number_input("m:", value=1, key="m"))
    with col2:
        b1=float(st.number_input("b:", value=1, key="b"))
    if m != 0:
        st.markdown("Usted ingreso la siguiente ecuacion:")
        st.latex(f"{m}x+{b1}")

        st.markdown("**Gráfica de la función ingresada**")
        col1, col2= st.columns([1, 2], gap="medium")
        with col1:
            ini=float(st.number_input("Inicio:", value=-5, key="ini"))
            fin=float(st.number_input("Fin:", value=5, key="fin"))
        with col2:
            x=np.linspace(ini,fin,100)
            y= m*x + b1
            fig, ax= plt.subplots()
            ax.plot(x,y)
            st.pyplot(fig)
    else:
        st.error("El valor de m debe ser diferente de cero")

with st.container(border=True):
    st.markdown('''
    - **Funciones cuadráticas:** Son funciones donde a, b y c son constantes, a es diferente a cero y se expresan de la siguiente forma:
    ''')

    st.latex("f(x) = a{x}^{2}+bx+c")
    st.latex("f(x) = {x}^{2}+6x+9")

with st.container(border=False):
    st.markdown("**Digite**")
    col1, col2, col3 = st.columns(3)
    with col1:
        a=float(st.number_input("a:", value=1, key="a1"))
    with col2:
        b=float(st.number_input("b:", value=1, key="b1"))
    with col3:
        c=float(st.number_input("c:", value=1, key="c1"))
    if a != 0:
        st.markdown("Usted ingreso la siguiente ecuacion:")
        st.latex(f"{a}x^{2}+{b}x+{c}")

        st.markdown("**Gráfica de la función ingresada**")
        col1, col2= st.columns([1, 2], gap="medium")
        with col1:
            ini=float(st.number_input("Inicio:", value=-5, key="ini1"))
            fin=float(st.number_input("Fin:", value=5, key="fin1"))
        with col2:
            x=np.linspace(ini,fin,100)
            y= a*x**2 + b*x + c
            fig, ax= plt.subplots()
            ax.plot(x,y)
            st.pyplot(fig)
    else:
        st.error("El valor de a debe ser diferente de cero")

with st.container(border=True):
    st.markdown('''
    - **Funciones cúbicas:** Son funciones donde a, b, c y d son constantes, a es diferente a cero y se expresan de la siguiente forma:
    ''')

    st.latex("f(x) = a{x}^{3}+b{x}^{2}+cx+d")
    st.latex("f(x) = 8{x}^{3}+2{x}^{2}+3x+5")

with st.container(border=False):
    st.markdown("**Digite**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        a=float(st.number_input("a:", value=1, key="a2"))
    with col2:
        b=float(st.number_input("b:", value=1, key="b2"))
    with col3:
        c=float(st.number_input("c:", value=1, key="c2"))
    with col4:
        d=float(st.number_input("d:", value=1, key="d2"))
    if a != 0:
        st.markdown("Usted ingreso la siguiente ecuacion:")
        st.latex(f"{a}x^{3}+{b}x^{2}+{c}x+{d}")

        st.markdown("**Gráfica de la función ingresada**")
        col1, col2= st.columns([1, 2], gap="medium")
        with col1:
            ini=float(st.number_input("Inicio:", value=-5, key="ini2"))
            fin=float(st.number_input("Fin:", value=5, key="fin2"))
        with col2:
            x=np.linspace(ini,fin,100)
            y= a*x**3 + b*x**2 + c*x + d
            fig, ax= plt.subplots()
            ax.plot(x,y)
            st.pyplot(fig)
    else:
        st.error("El valor de a debe ser diferente de cero")

with st.container(border=True):
    st.markdown('''
    - **Funciones exponenciales:** Son funciones donde a es una constante positiva y se expresan de la siguiente forma:
    ''')

    st.latex("f(x) = {a}^{x}")
    st.latex("f(x) = {2}^{x}")
    st.latex("f(5) = {2}^{5}")

with st.container(border=False):
    st.markdown("**Digite**")
    col1, col2 = st.columns(2)
    with col1:
        a=float(st.number_input("a:", value=1, key="a3"))
    with col2:
        x=int(st.number_input("x:", value=1, key="b3"))
    if a >= 0:
        st.markdown("Usted ingreso la siguiente ecuacion:")
        st.latex(f"{a}^{x}")

        st.markdown("**Gráfica de la función ingresada**")
        col1, col2= st.columns([1, 2], gap="medium")
        with col1:
            ini=float(st.number_input("Inicio:", value=-5, key="ini3"))
            fin=float(st.number_input("Fin:", value=5, key="fin3"))
        with col2:
            x=np.linspace(ini,fin,100)
            y= a**x
            fig, ax= plt.subplots()
            ax.plot(x,y)
            st.pyplot(fig)
    else:
        st.error("El valor de a debe ser cero o mayor que cero")

with st.container(border=True):
    st.markdown('''
    - **Funciones logarítmicas:** Son funciones donde a es una constante positiva, a es diferente a uno y se expresan de la siguiente forma:
    ''')

    st.latex("f(x) = \log_{a}{x}")
    st.latex("f(x) = \log_{6}{x}")
    st.latex("f(54) = \log_{6}{54}")

with st.container(border=False):
    st.markdown("**Digite**")
    col1, col2 = st.columns(2)
    with col1:
        a=int(st.number_input("a:", value=1, key="a4"))
    with col2:
        x=float(st.number_input("x:", value=1, key="b4"))
    if a > 1:
        st.markdown("Usted ingreso la siguiente ecuacion:")
        st.latex(f"\log_{a}{x}")

        st.markdown("**Gráfica de la función ingresada**")
        col1, col2= st.columns([1, 2], gap="medium")
        with col1:
            ini=float(st.number_input("Inicio:", value=-5, key="ini4"))
            fin=float(st.number_input("Fin:", value=5, key="fin4"))
        with col2:
            x=np.linspace(ini,fin,100)
            y=np.emath.logn(a, x)
            fig, ax= plt.subplots()
            ax.plot(x,y)
            st.pyplot(fig)
    else:
        st.error("El valor de a debe ser mayor que 1")

    st.markdown('''
    ## Función constante''')
with st.container(border=True):
    st.markdown('''
    Una función constante es una función matemática que es una linea recta.
    Es aquella en donde lo unico que cambia es a y se expresa de la siguiente forma:

    ''')

    st.latex("f(x) = a")
    st.latex("f(x) = 8")
with st.container(border=False):
    st.markdown("**Digite**")
    col1, col2 = st.columns(2)
    with col1:
        a=int(st.number_input("a:", value=1, key="a5"))
    x=1
    if a != 0:
        st.markdown("Usted ingreso la siguiente ecuacion:")
        st.latex(f"{a}")

        st.markdown("**Gráfica de la función ingresada**")
        col1, col2= st.columns([1, 2], gap="medium")
        with col1:
            ini=float(st.number_input("Inicio:", value=-5, key="ini5"))
            fin=float(st.number_input("Fin:", value=5, key="fin5"))
        with col2:
            x=np.linspace(ini,fin,100)
            y= a*x**0
            fig, ax= plt.subplots()
            ax.plot(x,y)
            st.pyplot(fig)
    else:
        st.markdown("Usted ingreso la siguiente ecuacion:")
        st.latex(f"{0}")

        st.markdown("**Gráfica de la función ingresada**")
        col1, col2= st.columns([1, 2], gap="medium")
        with col1:
            ini=float(st.number_input("Inicio:", value=-5, key="ini6"))
            fin=float(st.number_input("Fin:", value=5, key="fin6"))
        with col2:
            x=np.linspace(ini,fin,100)
            y=a**x
            fig, ax= plt.subplots()
            ax.plot(x,y)
            st.pyplot(fig)