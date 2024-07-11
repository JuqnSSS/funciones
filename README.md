import streamlit as st

st.set_page_config(
    page_title="Funciones",
    page_icon=":bar_chart:",
    layout="wide"
)

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

st.latex("f(x)={3x}^{3}-{x}^{2}+{\\frac{5}{2}}")

st.latex("y={x}^{2}+{36x}+{6}")

st.markdown('''

- **Gráfica:** La gráfica de una función es la representación visual de la relación entre el dominio y el codominio. Se obtiene al graficar los pares de valores (x, y) en un plano cartesiano.
''')

#Graficar la funcion para luego
#Usar latex para representar funciones
#Todo eso en orden de antes
