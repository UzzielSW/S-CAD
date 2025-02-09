import streamlit as st

st.title("Parcial 3 - Satélite y Dron")

st.write("### :blue[Satélite]")
st.write("""
Un satélite es un objeto que orbita alrededor de un cuerpo celeste más grande, ya sea natural o artificial. En el contexto espacial, podemos distinguir dos tipos principales:

- Satélites naturales: Son cuerpos celestes que orbitan alrededor de planetas o cuerpos más grandes. Un ejemplo clásico es la Luna, que orbita alrededor de la Tierra.

- Satélites artificiales: Son dispositivos creados por el ser humano que se colocan en órbita alrededor de la Tierra u otros cuerpos celestes con propósitos específicos.
""")
col1, col2 = st.columns(2)
with col1:
    st.image("./img/DP3-B1.png", caption="Diseño Base", width=330)

with col2:
    st.image("./img/DP3-1.jpg", caption="Diseño realizado en Fusion 360")

st.write("### :blue[Visualización del Diseño]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a4da6d8a7fac6416f2?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)

st.write("")
st.write("### :blue[Dron DJI Spark]")
st.write("""
Un dron (UAV) Vehículo Aéreo No Tripulado , es una aeronave que se controla de forma remota mediante un dispositivo de control o mediante sistemas de navegación automáticos programados. Estos dispositivos pueden ser operados a distancia y realizar diversas misiones y tareas en diferentes sectores como: Fotografía y video, Agricultura, Vigilancia, Búsqueda y rescate, Militar, Investigación científica.
""")

col1, col2 = st.columns(2)
with col1:
    st.write("#### :orange[Características Técnicas]")
    st.write("""
- Dimensiones compactas: 143 x 143 x 55 mm
- Peso: Aproximadamente 300 gramos
- Autonomía de vuelo: 16 minutos
- Alcance de control: 2 km
- Velocidad máxima: 50 km/h
- Resolución de cámara: 12 megapíxeles
- Estabilización con gimbal de 2 ejes
- Modos de vuelo: Automático y manual""")
    st.write("")


with col2:
    st.write("#### :orange[Aplicaciones]")
    st.write("""
- Fotografía aérea
- Grabación de video
- Selfies aéreas
- Uso recreativo
- Primeros pasos en pilotaje de drones""")
    
col1, col2 = st.columns(2)
with col1:
    st.image("./img/DP3-B2.jpg", caption="Diseño Base [Home]")
    st.image("./img/DP3-B3.jpg", caption="Diseño Base [Lateral]", width=315)
    st.image("./img/DP3-B4.png", caption="Diseño Base [Superior]", width=320)

with col2:
    st.image("./img/DP3-2.jpg", caption="Diseño realizado en Fusion 360", width=310)
    st.image("./img/DP3-3.jpg", caption="Diseño realizado en Fusion 360")
    st.image("./img/DP3-4.jpg", caption="Diseño realizado en Fusion 360")


st.write("### :blue[Visualización del Diseño]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a4773a7aadbc510c8f?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)