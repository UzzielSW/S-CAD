import streamlit as st

st.title("Asignación 2")
st.subheader("Religiones Alrededor del Mundo: Templos y Construcciones")

#----
st.write("")
st.write("### :blue[Templo y Religión]")
st.image("./img/A2-1.jpg", caption="El Templo de Salta, Argentina")
st.write("Pertenece a la religión conocida como mormonismo o La Iglesia de Jesucristo de los Santos de los Últimos Días, es una denominación cristiana restaurada que se originó en los Estados Unidos en el siglo XIX.")

#----
st.write("")
st.write("### :blue[Historia y Origen]")
col1, col2 = st.columns(2)
with col1:
    st.write("La Iglesia de Jesucristo de los Santos de los Últimos Días fue fundada por Joseph Smith en 1830 en Nueva York, Estados Unidos. Joseph Smith afirmó haber recibido visiones divinas y haber traducido el Libro de Mormón.")
    st.write("Bajo el liderazgo de Brigham Young, los mormones se establecieron en Utah en 1847, donde la iglesia continuó creciendo y expandiéndose internacionalmente.")

with col2:
    st.image("./img/A2-2.png", caption="Iglesia de Jesucristo de los Santos de los Últimos Días")

#----
st.write("")
st.write("### :blue[Costumbres]")
col1, col2 = st.columns(2)
with col1:
    st.write("Algunas de sus costumbres y prácticas incluyen:")
    st.markdown("- Bautismo por inmersión a los 8 años de edad")
    st.markdown("- Reuniones dominicales que incluyen la Santa Cena")
    st.markdown("- Énfasis en la familia y la genealogía")
    st.markdown("- Abstinencia de alcohol, tabaco, café")
    st.markdown("- Diezmo (donación del 10% de los ingresos a la iglesia)")
    st.markdown("- Obra misional, con jóvenes sirviendo misiones de tiempo completo")

with col2:
    col3, col4 = col2.columns(2)
    with col3:
        st.image("./img/A2-3.jpg", caption="Bautismo")
        st.image("./img/A2-4.jpg", caption="Diezmo")
    with col4:
        st.image("./img/A2-5.jpg", caption="Reuniones dominicales")
        st.image("./img/A2-6.jpg", caption="Familia y la Genealogía")

#----
st.write("")
st.write("### :blue[Vestimenta]")
col1, col2 = st.columns(2)
with col1:
    st.write("La vestimenta de los miembros de la iglesia es generalmente modesta y conservadora. ")
    st.markdown("Para los servicios religiosos:")
    st.markdown("- Hombres: Suelen usar traje y corbata.")
    st.markdown("- Mujeres: Vestidos o faldas que lleguen a la rodilla o más abajo, blusas modestas.")
    st.markdown("Los misioneros tienen un código de vestimenta más estricto:")
    st.markdown("- Hombres: Traje oscuro, camisa blanca, corbata conservadora, cabello corto y bien arreglado.")
    st.markdown("- Mujeres: Faldas o vestidos modestos hasta la rodilla o más largos, blusas con mangas.")

with col2:
    st.image("./img/A2-7.png")
    st.image("./img/A2-8.jpg")
    st.image("./img/A2-9.jpg")
    
#----
st.write("")
st.write("### :blue[Ubicación]")
col1, col2 = st.columns(2)
with col1:
    st.image("./img/A2-10.png", caption="Ruta Nacional N 51, A4400 Salta, Argentina")

with col2:
    st.image("./img/A2-11.png", caption="Distancia entre Panamá")
    st.image("./img/A2-12.png", caption="Costos de Viaje")

#----
st.write("")
st.write("### :blue[Diseño Templo de Salta]")
st.image("./img/A2-13.png", caption="Diseño Base")
st.image("./img/A2-14.png", caption="Diseño en Shapr3D")

#----
st.write("")
st.write("### :blue[Visualización del Diseño]")
st.markdown('<iframe src="https://collaborate.shapr3d.com/v/VplQJwVNwTdaQhnx9ZALZ" title="Shapr3D Webviewer" width="640" height="640" frameborder="0" allow="web-share; xr-spatial-tracking" loading="lazy" scrolling="no" referrerpolicy="origin-when-cross-origin" allowfullscreen></iframe>', unsafe_allow_html=True)

