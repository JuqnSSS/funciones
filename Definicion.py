import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

st.title('Funciones matemáticas')

st.markdown('''
## ¿Que es una función?

En matemáticas, una función es una relación entre dos conjuntos, llamada dominio y codominio, que asocia a cada elemento del dominio un único elemento del codominio.

En otras palabras, una función es una regla que establece cómo se transforma un valor de entrada (del dominio) en un valor de salida (del codominio).
''')

st.markdown('''
## ¿Como se representa una función?

- **Ecuación:** La forma más común de representar una función es mediante una ecuación. Por ejemplo, la ecuación y = 2x define una función que asocia a cada valor de x (dominio) el doble de ese valor (codominio). Un ejemplo podrian ser las siguientes ecuaciones:

''')

st.latex("f(x)={a}_{0}+{a}_{1}x+{a}_{2}{x}^{2}+...+{a}_{n}{x}^{n}")
st.latex("y={x}^{2}+{36x}+{6}")

st.markdown('''

- **Gráfica:** La gráfica de una función es la representación visual de la relación entre el dominio y el codominio. Se obtiene al graficar los pares de valores (x, y) en un plano cartesiano.
''')

with st.container(border=True):
    st.markdown("**Gráfica de la función cuadrática**")
    x = np.linspace(-5, 5, 100)
    y = x**2
    st.line_chart(y)

st.title('''Juan Medina 2240646''')