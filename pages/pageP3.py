import streamlit as st

st.title("Parcial 3")

st.write("### :blue[Satélite]")

col1, col2 = st.columns(2)
with col1:
    st.image("./img/DP3-B1.png", caption="Diseño Base")

with col2:
    st.image("./img/DP3-1.jpg", caption="Diseño realizado en Fusion 360")

st.write("### :blue[Visualización del Diseño]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a4da6d8a7fac6416f2?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)

st.write("")
st.write("### :blue[Dron DJI Spark]")

col1, col2 = st.columns(2)
with col1:
    st.image("./img/DP3-B2.jpg", caption="Diseño Base [Home]")
    st.image("./img/DP3-B3.jpg", caption="Diseño Base [Lateral]")
    st.image("./img/DP3-B4.png", caption="Diseño Base [Superior]")

with col2:
    st.image("./img/DP3-2.jpg", caption="Diseño realizado en Fusion 360")
    st.image("./img/DP3-3.jpg", caption="Diseño realizado en Fusion 360")
    st.image("./img/DP3-4.jpg", caption="Diseño realizado en Fusion 360")


st.write("### :blue[Visualización del Diseño]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a4773a7aadbc510c8f?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)