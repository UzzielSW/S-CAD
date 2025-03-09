import streamlit as st

st.title("Asignación 5 - CPU - SOCKET - MEMORY")

#----
st.write("")
st.write("### :blue[CPU]")
st.image("./img/A5-1.jpg", caption="AMD RYZEN 9 - 5950X")

col1, col2 = st.columns(2)
with col1:
    st.write("#### :orange[¿En qué consiste?]")
    st.write("El AMD Ryzen 9 5950X es un procesador de alta gama lanzado en 2020, perteneciente a la serie Zen 3 de AMD. Es un CPU diseñado para usuarios que requieren alto rendimiento.")
    st.write("")

    st.write("#### :orange[¿Para qué sirve?]")
    st.write("""Este procesador está orientado a:
- Workstations profesionales
- Renderizado 3D
- Edición de video en alta resolución
- Gaming de alto rendimiento
- Compilación de código
- Virtualización
- Streaming profesional
- Tareas de computación intensiva""")

with col2:
    st.write("#### :orange[¿En qué socket?]")
    st.write("""Utiliza el socket AM4, específicamente compatible con placas base que tienen los chipsets:
- X570
- B550
- X470 (con actualización de BIOS)
- B450 (con actualización de BIOS)""")
    st.write("")

    st.write("#### :orange[¿Cómo está formado?]")
    st.write("""
- 16 núcleos físicos y 32 hilos (threads)
- Frecuencia base: 3.4 GHz
- Frecuencia boost máxima: hasta 4.9 GHz
- Caché L3: 64MB
- Caché L2: 8MB (512KB por núcleo)
- TDP: 105W
- Proceso de fabricación de 7nm
- Soporte para PCIe 4.0""")

#----
col1, col2 = st.columns(2)
with col1:
    st.write("")
    st.write("### :blue[Medidas]")
    st.image("./img/A5-2.png", caption="Medidas del CPU")

with col2:
    st.write("")
    st.write("###")
    st.image("./img/A5-3.jpg", caption="Sketch", width=270)

#----
col1, col2 = st.columns(2)
with col1:
    st.write("")
    st.write("### :blue[Diseño Base]")
    st.image("./img/A5-4.png", caption="Vista Superior")

    st.write("")
    st.image("./img/A5-6.jpg", caption="Vista Inferior")

with col2:
    st.write("")
    st.write("### :orange[Diseño en Fusion 360]")
    st.image("./img/A5-5.jpg", width=250)

    for i in range(3):
        st.write("")
    st.image("./img/A5-7.jpg", width=250)


#----
st.write("")
st.write("### :blue[SOCKET]")
st.image("./img/A5-8.png", caption="Socket AM4 - AMD", width=500)

col1, col2 = st.columns(2)
with col1:
    st.write("#### :orange[¿En qué consiste?]")
    st.write("""El AM4 es socket de CPU desarrollado por AMD, lanzado en 2016. Es una interfaz física que sirve como punto de conexión entre el procesador y la placa base, utilizando un diseño PGA (Pin Grid Array).

- Compatible con múltiples generaciones de procesadores AMD""")
    st.write("")

    st.write("#### :orange[¿Para qué sirve?]")
    st.write("""El Socket AM4 tiene como funciones principales:
- Proporcionar conexión física entre CPU y placa base
- Asegurar la correcta alineación del procesador
- Distribuir energía al procesador
- Facilitar la comunicación entre CPU y otros componentes
- Permitir el intercambio de procesadores compatibles""")

with col2:
    st.write("#### :orange[¿Cómo está formado?]")
    st.write("""
- Base de plástico que aloja los pines
- Marco metálico de retención
- Cuenta con un sistema de retención con palanca
- Dispone de 1331 contactos dispuestos en rejilla
- Sistema de alineación para evitar instalación incorrecta
- Mecanismo de presión cero (ZIF)
- Sistema de refrigeración compatible con el estándar AMD""")

    st.write("#### :orange[Características técnicas]")
    st.write("""
- Dimensiones: 40x40mm
- Soporte para TDP desde 45W hasta 105W
- Soporte para memoria DDR4
- Compatible con PCIe Gen 4.0 (en procesadores compatibles)""")

#----
col1, col2 = st.columns(2)
with col1:
    st.write("")
    st.write("### :blue[Medidas]")
    st.image("./img/A5-9.png", caption="Medidas del Socket")

with col2:
    st.write("")
    st.write("###")
    st.image("./img/A5-10.jpg", caption="Sketch")

#----
col1, col2 = st.columns(2)
with col1:
    st.write("")
    st.write("### :blue[Diseño Base]")
    st.image("./img/A5-11.png")

    st.write("")
    st.image("./img/A5-4.png")

with col2:
    st.write("")
    st.write("### :orange[Diseño en Fusion 360]")
    st.image("./img/A5-12.png")

    for i in range(16):
        st.write("")
    st.image("./img/A5-13.png")

#----
st.write("")
st.write("### :blue[Visualización de Diseños]")
st.write("### :orange[Socket y CPU]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a4cf1dbf4ba5357c80?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)

#----
st.write("")
st.write("### :blue[Animación]")
st.video("./img/AnimacionSocketCPU.mp4")



#----
st.write("")
st.write("### :blue[Memoria RAM]")
st.image("./img/A5-14.png", caption="DDR5 UDIMM")
st.image("./img/A5-15.jpg", caption="Lexar DDR5 UDIMM")
st.write("""DDR5 es la 5ta generación de memorias RAM síncrona de doble velocidad de datos. Es un módulo de memoria que ofrece:
- Mayor ancho de banda que DDR4
- Menor consumo de energía
- Mayor densidad de datos
- Mejor gestión de errores
- Voltaje operativo de 1.1V (menor que DDR4)
- Frecuencias que van desde 4800MHz hasta 6000MHz
- ECC (Error Correction Code) integrado""")

col1, col2 = st.columns(2)
with col1:
    st.write("#### :orange[¿Para qué sirve?]")
    st.write("""
- Almacenamiento temporal de datos
- Procesamiento rápido de información
- Multitarea eficiente
- Mejora del rendimiento en gaming
- Optimización de aplicaciones profesionales
- Soporte para cargas de trabajo intensivas""")

    st.write("#### :orange[¿Qué Modelo de Placas Base?]")
    st.write("""Intel:
- Placas base con chipset Z690
- Placas base con chipset B660
- Placas base con chipset H670
- Placas base con chipset Z790
- Placas base con chipset B760D

AMD:
- Placas base con socket AM5
- Placas base con chipset X670E
- Placas base con chipset X670
- Placas base con chipset B650E
- Placas base con chipset B650
""")
    st.write("")

with col2:
    st.write("#### :orange[¿Cómo está formado?]")
    st.write("""
- Chips de memoria DDR5
- Módulo de 288 pines
- PMIC (Power Management Integrated Circuit) integrado
- Circuito de control de voltaje on-die
- Sistema de gestión térmica
- Capacidades disponibles:
    - 8GB
    - 16GB
    - 32GB""")

    st.write("#### :orange[Características técnicas]")
    st.write("""
- Voltaje: 1.1V
- Frecuencias disponibles: 4800-6000MHz
- Latencias CAS variables según modelo
- Compatibilidad con XMP 3.0
- Diseño de PCB multicapa
- Sistema de disipación térmica (en modelos específicos)
- ECC on-die para corrección de errores""")

#----
st.write("")
st.write("### :blue[Diseños Base]")
st.image("./img/A5-20.jpg")
st.image("./img/A5-16.jpg")

st.write("")
st.write("### :orange[Diseño en Fusion 360]")
st.image("./img/A5-21.png")
st.image("./img/A5-17.png")
st.image("./img/A5-18.png")
st.image("./img/A5-19.png")

#----
st.write("")
st.write("### :blue[Visualización de Diseño]")
st.write("### :orange[Memoria RAM]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a4ddd57951040cdcb5?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)

#----
st.write("")
st.write("### :blue[Animación]")
st.video("./img/AnimacionRAM.mp4")

#----
st.write("")
st.write("#### :blue[Conclusión]")
st.markdown("""Durante el proceso pude aprender los siguientes puntos:
- Estudio de movimiento (realizar la animación)
- Análisis de sección (visualización de componentes)
""")