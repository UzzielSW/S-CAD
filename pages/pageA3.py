import streamlit as st

st.title("Asignación 3 - Monedas y Escudos")

#----
st.write("")
st.write("### :blue[Moneda de 5 Yenes y 1 Yen]")
col1, col2 = st.columns(2)
with col1:
    st.write("Lugar de Origen Las monedas de 5 yenes y 1 yen se originan en Japón. Son acuñadas por la Casa de la Moneda de Japón, ubicada en Tokio.")
    st.write("El significado de los símbolos en Moneda de 5 yenes:")
    st.write("- El agujero central representa una cosecha abundante de arroz.")
    st.write("- El diseño de flores de paulownia simboliza al gobierno japonés.")

with col2:
    st.markdown("![1 Yen](https://upload.wikimedia.org/wikipedia/commons/1/15/1JPY.JPG)")
    st.markdown("![5 Yen](https://upload.wikimedia.org/wikipedia/commons/1/10/5JPY.JPG)")

#----
st.write("")
st.write("### :blue[Visualización de Diseño]")
st.markdown('<iframe src="https://collaborate.shapr3d.com/v/IRKX4sRhrjm1ZZpRnOp6J" title="Shapr3D Webviewer" width="640" height="440" frameborder="0" allow="web-share; xr-spatial-tracking" loading="lazy" scrolling="no" referrerpolicy="origin-when-cross-origin" allowfullscreen></iframe>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.write(" ### :gray[Moneda de 1 yen]")
    st.markdown("""
    - **Material**: Aluminio 100%
    - **Diámetro**: 20 mm
    - **Grosor**: 1.5 mm
    - **Peso**: 1 g
    - **Borde**: Liso
    """)

with col2:
    st.write(" ### :orange[Moneda de 5 yen]")
    st.markdown("""
    - **Material**: Aleación de cobre-zinc (75% cobre, 25% zinc)
    - **Diámetro**: 22 mm
    - **Grosor**: 1.5 mm
    - **Peso**: 3.75 g
    - **Borde**: Liso
    """)

#----
st.write("")
st.write("### :blue[Escudo de Aquiles]")
col1, col2 = st.columns(2)
with col1:
    st.markdown("- Lugar de Origen: Grecia antigua, descrito en la Ilíada de Homero.")
    st.markdown("- Significado de símbolos: Representa el cosmos y la vida humana. Incluye escenas de ciudades en paz y guerra.")
    st.markdown("Especificaciones técnicas:")
    st.markdown("- **Material**: Bronce, oro, plata y estaño")
    st.markdown("- **Tamaño**: Aproximadamente 1-1.5 metros de diámetro")

with col2:
    st.markdown("![Escudo de Aquiles](https://i.pinimg.com/736x/2d/a7/55/2da755ffa5e5fcaf2ab5ab026715426f.jpg)")
    
#----
st.write("")
st.write("### :blue[Visualización de Diseño]")
st.markdown('<iframe src="https://collaborate.shapr3d.com/v/8gPlC19U6MvYtC7rqiPz-" title="Shapr3D Webviewer" width="640" height="440" frameborder="0" allow="web-share; xr-spatial-tracking" loading="lazy" scrolling="no" referrerpolicy="origin-when-cross-origin" allowfullscreen></iframe>', unsafe_allow_html=True)

#----
st.write("")
st.write("")
st.write("### :blue[Escudo de Juana de Arco]")
col1, col2 = st.columns(2)
with col1:
    st.markdown("- Lugar de Origen: Francia, siglo XV.")
    st.markdown("- Significado de símbolos/elementos: Flor de lis (símbolo real francés) y posiblemente una cruz, representando la fe católica y la lealtad a la corona francesa.")
    st.markdown("Especificaciones técnicas:")
    st.markdown("- **Material**: Acero o hierro")
    st.markdown("- **Tamaño**: Aproximadamente 60-70 cm de alto (dimensiones parametrizables)")

with col2:
    st.image("https://www.worldhistory.org/img/r/p/1000x1200/8662.jpg.webp?v=1722621123", width=200, caption="Escudo de Juana de Arco")
    
#----
st.write("")
st.write("### :blue[Visualización de Diseño]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a44aac02bffc97e5d7?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)

#----
st.write("")
st.write("")
st.write("### :blue[Escudo de Golden State Warrios]")
col1, col2 = st.columns(2)
with col1:
    st.write("Lugar de Origen Los Golden State Warriors se originaron en Filadelfia, Pensilvania, en 1946. Se trasladaron a San Francisco, California, en 1962, y actualmente tienen su sede en San Francisco, representando el área de la Bahía de San Francisco.")

    st.write("El logo actual representa el puente Golden Gate, un símbolo icónico de San Francisco. Los colores azul y amarillo representan el estado de California. El círculo del logo simboliza unidad y el espíritu de equipo.")

with col2:
    st.markdown("![Escudo de Golden State Warriors](https://1000marcas.net/wp-content/uploads/2020/02/logo-Golden-State-Warriors-500x281.png)")
    
#----
st.write("")
st.write("### :blue[Visualización de Diseño]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a480271810f4c08ef2?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)

#----
st.write("")
st.write("")
st.write("### :blue[Escudo de FC Barcelona]")
col1, col2 = st.columns(2)
with col1:
    st.write("El escudo actual contiene varios símbolos significativos:")
    st.markdown("1. **La Cruz de San Jorge (Cruz roja sobre fondo blanco)**: Representa a Sant Jordi, patrón de Cataluña.")
    st.markdown("2. **Las barras rojas y amarillas (Senyera)**: Son las cuatro barras de la bandera catalana, simbolizando la identidad catalana del club.")
    st.markdown("3. **Los colores azul y grana**: Son los colores tradicionales del club, supuestamente inspirados en los del FC Basilea, aunque hay varias teorías sobre su origen.")
    

with col2:
    st.markdown("![Escudo de FC Barcelona](https://images3.alphacoders.com/601/thumb-1920-601283.jpg)")
    st.markdown("4. **El balón de fútbol**: Representa el deporte principal del club.")
    st.markdown("5. **Las iniciales FCB**: Football Club Barcelona.")
    

#----
st.write("")
st.write("### :blue[Visualización de Diseño]")
st.markdown('<iframe src="https://collaborate.shapr3d.com/v/KHOCodmyXyMTcjpkku8AE" title="Shapr3D Webviewer" width="640" height="640" frameborder="0" allow="web-share; xr-spatial-tracking" loading="lazy" scrolling="no" referrerpolicy="origin-when-cross-origin" allowfullscreen></iframe>', unsafe_allow_html=True)

#----
st.write("")
st.write("")
st.write("### :blue[Escudo Personal]")
col1, col2 = st.columns(2)
with col1:
    st.write("Los 6 puntos azules significan los principales aspectos que busco dominar y que son la base de mi código o estilo de vida:")
    st.markdown("- **Train (entrenar)**: Entrenar y mejorar constantemente")
    st.markdown("- **Eat (comer bien)**: Comer bien para mantener una buena salud")
    st.markdown("- **Sleep (dormir bien)**: Dormir lo suficiente para estar descansado")
    st.markdown("- **Patience (paciencia)**: Ser paciente y no darse por vencido")
    st.markdown("- **Hard Work (trabajo duro)**: Trabajar fuerte y perseverar")
    st.markdown("- **Sacrifice (sacrificio)**: Sacrificar tiempo y energ a para lograr objetivos")

    
    
with col2:
    st.image("./img/A3-1.png", caption="Escudo Personal")
    st.write("Mediante los segmentos verdes y morados se hace referencia a el uróboro (representa la unidad de todas las cosas materiales y espirituales, que no desaparecen nunca, sino que cambian de aspecto en un ciclo perpetuo de destrucción y creación)")

#----
st.write("")
st.write("### :blue[Visualización de Diseño]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a43fc204f856173d13?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)