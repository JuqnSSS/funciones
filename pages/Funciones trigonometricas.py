import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

st.title('Tipos de funciones')

st.markdown('''
## Funciones trigonométricas


Las funciones trigonométricas son funciones matemáticas que relacionan los ángulos de un triángulo rectángulo con sus lados. Se basan en las **razones trigonométricas**, que son cocientes entre dos lados específicos del triángulo.
''')

st.image("https://s1.significados.com/foto/las-6-razones-trigonometricas.jpg?class=article")
st.markdown('''
Estas funciones trigonométricas básicas se pueden extender a cualquier ángulo usando el concepto de **círculo unitario**. En este contexto, las funciones trigonométricas se definen como las coordenadas x e y de un punto que se mueve sobre la circunferencia del círculo a medida que el ángulo aumenta.
''')

with st.container(border=False):
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://www.neurochispas.com/wp-content/uploads/2021/05/formula-del-circulo-unitario.png")
    with col2:
        st.markdown('''Las funciones trigonométricas tienen diversas aplicaciones en matemáticas, física, ingeniería y otras áreas. Se utilizan para calcular distancias, ángulos, alturas, áreas y otras magnitudes en diversos contextos.''')
        st.markdown('''Además de las funciones trigonométricas básicas, existen otras funciones derivadas de estas, como la cotangente (cot), la secante (sec) y la cosecante (csc). Estas funciones se definen como las inversas de las funciones trigonométricas básicas.''')
        st.markdown('''A continuación se muestran las funciones trigonométricas básicas:''')
with st.container(border=True):
    st.markdown('''
    - **Función Seno:** La función seno es una función trigonométrica fundamental que se define como la razón entre el cateto opuesto a un ángulo en un triángulo rectángulo y la hipotenusa. En otras palabras, representa la oscilación vertical de un punto que se mueve alrededor de la circunferencia unitaria en el plano complejo, en función del ángulo que forma con el eje positivo de las x, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\sin({x})")
        with col2:
            st.latex("\sin({30})")
        with col3:
            st.latex("\sin({90})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\sin({\pi}/2)")
        with col2:
            st.latex("\sin({\pi})")
        with col3:
            st.latex("\sin({2\pi})")
st.markdown('''**Grafica de la función Seno**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini7"))
            fin=float(st.number_input("Fin:", value=5, key="fin7"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                y = np.sin(x*z)
                st.line_chart(y)
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor a 0")

with st.container(border=True):
    st.markdown('''
    - **Función Coseno:** La función coseno es una función trigonométrica fundamental que se define como la razón entre el cateto adyacente a un ángulo en un triángulo rectángulo y la hipotenusa. En otras palabras, representa la proporción entre la longitud del lado que se encuentra junto al ángulo y la longitud del lado opuesto al mismo, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\cos({x})")
        with col2:
            st.latex("\cos({30})")
        with col3:
            st.latex("\cos({90})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\cos({\pi}/2)")
        with col2:
            st.latex("\cos({\pi})")
        with col3:
            st.latex("\cos({2\pi})")
st.markdown('''**Grafica de la función Coseno**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta1"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini8"))
            fin=float(st.number_input("Fin:", value=5, key="fin8"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                y = np.cos(x*z)
                st.line_chart(y)
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor a 0")

with st.container(border=True):
    st.markdown('''
    - **Función Tangente:** La función tangente es una función trigonométrica fundamental que se define como la razón entre el cateto opuesto y el cateto adyacente a un ángulo en un triángulo rectángulo. En otras palabras,ambién se puede definir la función tangente como la relación entre el seno y el coseno del ángulo, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ tan({x})")
        with col2:
            st.latex("\ tan({30})")
        with col3:
            st.latex("sen({x})/\cos({x})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ tan({\pi}/2)")
        with col2:
            st.latex("\ tan({\pi})")
        with col3:
            st.latex("sen({2\pi})/\cos({2\pi})")
st.markdown('''**Grafica de la función Tangente**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta2"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini9"))
            fin=float(st.number_input("Fin:", value=5, key="fin9"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                w = np.sin(x*z)
                v = np.cos(x*z)
                y = w/v
                st.line_chart(y)
        
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor o igual a 0")

with st.container(border=True):
    st.markdown('''
    - **Función Secante:** La función secante es una función trigonométrica que se define como la razón entre la longitud de la hipotenusa y la longitud del cateto adyacente de un triángulo rectángulo. En otras palabras, es el recíproco del coseno de un ángulo, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\sec({x})")
        with col2:
            st.latex("\sec({30})")
        with col3:
            st.latex("\sec({90})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\sec({\pi}/2)")
        with col2:
            st.latex("\sec({\pi})")
        with col3:
            st.latex("\sec({2\pi})")
st.markdown('''**Grafica de la función Secante**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta3"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini11"))
            fin=float(st.number_input("Fin:", value=5, key="fin11"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                p = np.cos(x*z)
                y = p**-1
                st.line_chart(y)
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor a 0")

with st.container(border=True):
    st.markdown('''
    - **Función Cosecante:** 
La función cosecante, denotada como csc(x), es una función trigonométrica fundamental que se define como el recíproco del seno de un ángulo. En otras palabras, si θ es un ángulo en un triángulo rectángulo, la cosecante de θ es la razón entre la longitud de la hipotenusa y la longitud del cateto opuesto al ángulo θ, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\csc({x})")
        with col2:
            st.latex("\csc({30})")
        with col3:
            st.latex("\csc({90})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\csc({\pi}/2)")
        with col2:
            st.latex("\csc({\pi})")
        with col3:
            st.latex("\csc({2\pi})")
st.markdown('''**Grafica de la función Cosecante**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta5"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini12"))
            fin=float(st.number_input("Fin:", value=5, key="fin12"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                w = x*z
                p = np.sin(w)
                y = p**-1
                st.line_chart(y)
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor a 0")

with st.container(border=True):
    st.markdown('''
    - **Función Cotangente:** La función cotangente, denotada como cot(x) o cotg(x), es una función trigonométrica que se define como la razón inversa de la tangente de un ángulo. En otras palabras, si la tangente de un ángulo es la razón entre el seno y el coseno del ángulo, la cotangente es la razón entre el coseno y el seno del mismo ángulo, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ cot({x})")
        with col2:
            st.latex("\ cot({30})")
        with col3:
            st.latex("\cos({x})/sen({x})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ cot({\pi}/2)")
        with col2:
            st.latex("\ cot({\pi})")
        with col3:
            st.latex("\cos({2\pi})/sen({2\pi})")
st.markdown('''**Grafica de la función Cotangente**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta13"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini14"))
            fin=float(st.number_input("Fin:", value=5, key="fin14"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                w = np.tan(x*z)
                y = w**-1
                st.line_chart(y)
                
        
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor o igual a 0")


st.markdown('''
## Inversas trigonométricas


Las funciones trigonométricas inversas, también conocidas como funciones arco, antitrigonométricas o ciclométricas, son el complemento perfecto de las funciones trigonométricas tradicionales (seno, coseno y tangente). Al igual que las inversas de otras funciones, estas inversas "deshacen" lo que hacen sus funciones trigonométricas correspondientes.
''')

with st.container(border=True):
    st.markdown('''
    - **Función Arcoseno:** El arcoseno, también conocido como función seno inverso o asin(x), es una función matemática que representa el ángulo cuya medida en radianes es igual al seno de un número real x, que se encuentra entre -1 y 1. En otras palabras, si y = arcsin(x), entonces sen(y) = x, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arcsin({x})")
        with col2:
            st.latex("\ arcsin({30})")
        with col3:
            st.latex("\ arcsin({90})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arcsin({\pi}/2)")
        with col2:
            st.latex("\ arcsin({\pi})")
        with col3:
            st.latex("\ arcsin({2\pi})")
st.markdown('''**Grafica de la función Arcoseno**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta20"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini20"))
            fin=float(st.number_input("Fin:", value=5, key="fin20"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                y = np.asin(x*z)
                st.line_chart(y)
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor a 0")

with st.container(border=True):
    st.markdown('''
    - **Función Arcocoseno:** La función arcocoseno, también conocida como acoseno o coseno inverso, es una función matemática fundamental en trigonometría. Se define como la inversa del coseno, es decir, es la función que encuentra el ángulo cuyo coseno es un valor específico, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arccos({x})")
        with col2:
            st.latex("\ arccos({30})")
        with col3:
            st.latex("\ arccos({90})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arccos({\pi}/2)")
        with col2:
            st.latex("\ arccos({\pi})")
        with col3:
            st.latex("\ arccos({2\pi})")
st.markdown('''**Grafica de la función Arcocoseno**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta21"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini21"))
            fin=float(st.number_input("Fin:", value=5, key="fin21"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                y = np.acos(x*z)
                st.line_chart(y)
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor a 0")

with st.container(border=True):
    st.markdown('''
    - **Función Arcotangente:** La función arcotangente, también conocida como tangente inversa y simbolizada como arctan(x) o atan(x), es una función fundamental en trigonometría. Se define como la función inversa de la tangente, es decir, es la función que encuentra el ángulo cuya tangente es un valor específico x, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arctan({x})")
        with col2:
            st.latex("\ arctan({30})")
        with col3:
            st.latex("arctan({60})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arctan({\pi}/2)")
        with col2:
            st.latex("\ arctan({\pi})")
        with col3:
            st.latex("\ arctan({\pi}/6)")
st.markdown('''**Grafica de la función Arcotangente**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta22"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini22"))
            fin=float(st.number_input("Fin:", value=5, key="fin22"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                w = np.atan(x*z)
                st.line_chart(w)
        
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor o igual a 0")

with st.container(border=True):
    st.markdown('''
    - **Función Arcosecante:** La función arcosecante, denotada como arcsec(x) o asec(x), es una función trigonométrica inversa que se define como el ángulo cuya cosecante es un valor específico (x). En otras palabras, si csc(θ) = x, entonces arcsec(x) = θ; se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arcsec({x})")
        with col2:
            st.latex("\ arcsec({30})")
        with col3:
            st.latex("\ arcsec({90})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arcsec({\pi}/2)")
        with col2:
            st.latex("\ arcsec({\pi})")
        with col3:
            st.latex("\ arcsec({2\pi})")
st.markdown('''**Grafica de la función Arcosecante**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta30"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini30"))
            fin=float(st.number_input("Fin:", value=5, key="fin30"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                w = x*z
                p = (w)**-1
                y = np.acos(p)
                st.line_chart(y)
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor a 0")

with st.container(border=True):
    st.markdown('''
    - **Función Arcocosecante:** 
La función arcocosecante, también conocida como cosecante inversa, es una función trigonometrica que se define como la inversa de la función cosecante. En otras palabras, si la cosecante de un ángulo es un valor específico, la función arcocosecante nos da el ángulo cuya cosecante es ese valor, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arccsc({x})")
        with col2:
            st.latex("\ arccsc({30})")
        with col3:
            st.latex("\ arccsc({90})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arccsc({\pi}/2)")
        with col2:
            st.latex("\ arccsc({\pi})")
        with col3:
            st.latex("\ arccsc({2\pi})")
st.markdown('''**Grafica de la función Arcocosecante**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta40"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini40"))
            fin=float(st.number_input("Fin:", value=5, key="fin40"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                w = x*z
                p = (w)**-1
                y = np.asin(p)
                st.line_chart(y)
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor a 0")

with st.container(border=True):
    st.markdown('''
    - **Función Arcocotangente:** En trigonometría, la arcocotangente es la función inversa de la cotangente de un ángulo dentro de un intervalo (0, π). Se simboliza arccot α, o (arcctg)α, y su significado geométrico es el ángulo cuya cotangente es α, se puede expresar de las siguientes formas:
    ''')
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ acot({x})")
        with col2:
            st.latex("\ acot({30})")
        with col3:
            st.latex("\ acot({60})")
    with st.container(border=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.latex("\ arccot({\pi}/2)")
        with col2:
            st.latex("\ arccot({\pi})")
        with col3:
            st.latex("\ arccot({\pi}/6)")
st.markdown('''**Grafica de la función Arcocotangente**''')
with st.container(border=False):
        col1, col2 = st.columns(2)
        with col1:
            teta=float(st.number_input("Ángulo:", value=1, key="teta60"))
            ini=float(st.number_input("Inicio:", value=-5, key="ini60"))
            fin=float(st.number_input("Fin:", value=5, key="fin60"))
        if 0<=teta<=360:
            with col2:
                x = np.linspace(ini, fin, 100)
                z = teta*math.pi/180
                w = x*z
                v = w**-1
                y = np.atan(v)
                st.line_chart(y)
        
        else:
            st.error("El ángulo debe ser menor o igual a 360 y mayor o igual a 0")