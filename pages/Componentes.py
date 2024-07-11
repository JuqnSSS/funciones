import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

st.title('Componentes')

st.markdown('''
- **Variable independiente:** También conocida como variable de entrada o argumento. Se representa comúnmente con la letra x. Es la variable que se modifica o manipula para obtener un valor de la función.
''')

st.markdown('''
 Observese que al resolver la funcion con el valor dado, la variable independiente es la unica que cambia:''')

st.latex("Variable={x}")
st.latex("f(x)={x}^{2}+{36x}+{6}")
st.latex("f(5)={(5)}^{2}+{36(5)}+{6}")
st.latex("f(5)=25+180+{6}")
st.latex("f(5)=211")


st.markdown('''

- **Variable dependiente:** También conocida como variable de salida. Se representa comúnmente con la letra y. Es el valor que se obtiene al aplicar la función a la variable independiente. Su valor depende del valor que se le asigne a la variable independiente.
''')

st.markdown(''' Usemos el mismo ejemplo anterior, f(x) es lo mismo que y, siempre y cuando se usen para decir la funcion y no al resolverla:
''')

st.latex("f(x)={y}")
st.latex("f(x)={x}^{2}+{36x}+{6}")
st.latex("y={x}^{2}+{36x}+{6}")

st.markdown('''
- **Dominio:** Es el conjunto de todos los valores válidos que puede tomar la variable independiente
''')

st.latex("f(x) = x^2")

st.markdown('''
En este caso, el dominio sería el conjunto de números reales, sin embargo no siempre es asi, veamos otro ejemplo:

''')

st.latex("f(x) = \sqrt{x}")

st.markdown('''
Si nos fijamos bien, el dominio sería los reales positivos, debido a que no existen raices complejas en el campo de los Reales.
''')

st.markdown('''
- **Codominio:** Es el conjunto de todos los valores posibles que puede tomar la variable dependiente.
''')

st.markdown('''Usando el ejemplo del dominio, el codominio en este caso, al ser una funcion radical todos sus posibles resultados seran reales positivos, incuido el cero. 
''')


st.markdown('''
- **Rango o recorrido:** Es el subconjunto del codominio que efectivamente toma la variable dependiente. En otras palabras, son los valores de y que realmente se obtienen al aplicar la función a los valores del dominio. El rango puede ser igual o menor que el codominio.
''')

st.markdown('''En la siguiente funcion, podremos apreciar que cada valor de y se encuentra dentro del rango del codominio.
''')

st.latex(f"f(x)=5x+8")

st.markdown('''Sin embargo no siempre seran iguales, notece en la siguiente funcion:
''')

st.latex(f"f(x)=x^{2}")

st.markdown('''En este caso el rango seran todos los reales positivos, debido a que no existe un numero real que al elevarse al cuadrado de negativo.
''')

st.markdown('''

En resumen, los componentes básicos que determinan el comportamiento y características de una función son la variable independiente, la variable dependiente, el dominio, el codominio y el rango. Estos elementos permiten analizar y comprender a fondo cómo funciona una función y cómo se transforma la variable de entrada para obtener la variable de salida.

Es importante recordar que estos son los componentes esenciales, y que en algunos casos específicos pueden existir elementos adicionales que complementen la información sobre la función.

''')
