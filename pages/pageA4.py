import streamlit as st

st.title("Asignación 4")
st.subheader("Brazos Robóticos y Circuitos")

#----
st.write("")
st.write("### :blue[Los Brazos Robóticos Industriales]")
st.write("Los brazos robóticos industriales ayudan a las empresas a aumentar su ventaja competitiva y mantener los costos bajos mediante la activación de la automatización de los procesos clave, los cuales contribuyen a una mayor seguridad para los trabajadores, la producción acelerada y la mejora de la productividad.")
st.write("**Qué es un brazo robótico industrial?**")
st.write("Los brazos robóticos, también conocidos como brazos robóticos articulados, son rápidos, confiables y precisos, y se pueden programar para realizar una cantidad infinita de tareas en una variedad de entornos. Se usan en las fábricas para automatizar la ejecución de tareas repetitivas, por ejemplo, aplicar pintura a los equipos o las piezas; en los almacenes para elegir, seleccionar o clasificar productos en los transportadores de distribución para cumplir con los pedidos de los consumidores; entre otros.")
st.markdown("![Brazo Robótico](https://www.esneca.lat/wp-content/uploads/tipos-de-robots-industriales.jpg)")
    
col1, col2 = st.columns(2)
with col1:
    st.write("Los brazos robóticos son manipuladores programables multieje.")
    st.write("""**Principales componentes:**
- Base
- Articulaciones
- Enlaces/eslabones
- Efector final
- Actuadores
- Sensores
""")
    st.write("""**Ventajas en la Industria**
- Alta precisión y repetibilidad
- Trabajo continuo sin fatiga
- Capacidad para operar en ambientes peligrosos
- Aumento de la productividad
""")
with col2:
    st.image("./img/A4-1.png", caption="Estructura de un brazo robótico")
    st.write("""**Integración con Sistemas CAD/CAM**
- Programación fuera de línea
- Simulación de trayectorias
- Detección de colisiones
- Optimización de procesos
""")

#----
st.write("")
st.write("### :blue[Visualización de Diseños:]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a42a4c3a7798ea2e71?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)

#----
st.write("")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a47dd8a5cf9cd88ca0?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)

#----
st.write("")
st.write("")
st.write("### :blue[Circuito Sumador Binario]")
st.write("El sumador es un circuito digital que realiza la adición de números. En muchas computadoras y otros tipos de procesadores se utilizan sumadores en las unidades aritméticas lógicas. También se utilizan en otras partes del procesador, donde se utilizan para calcular direcciones, índices de tablas, operadores de incremento y decremento y operaciones similares.")
st.image("./img/A4-2.png", caption="Circuito Sumador y Restador Binario de 4 bits")

#----
st.write("")
st.write("### :blue[CIRCUITO DECODIFICADOR BCD A LED DE 7 SEGMENTOS]")
st.write("Un decodificador BCD a 7 segmentos es como un traductor que toma este número binario y lo convierte en una señal que enciende los segmentos correctos de un display de 7 segmentos, para que puedas ver visualmente el número decimal correspondiente.")
st.image("./img/A4-3.png", caption="Circuito Decodificador BCD a 7 Segmentos")

#----
st.write("")
st.write("### :blue[Circuito Para Conteo Entre Bits]")
st.write("""Este circuito es un contador que solo puede mostrar los números del 0 al 9. Este tipo de circuito se utiliza mucho en electrónica digital y funciona de la siguiente manera:

- La información en estos circuitos se representa mediante bits, que son señales eléctricas que pueden tener dos valores: 0 o 1.

- El circuito está diseñado para cambiar su estado internamente de forma secuencial, representando cada estado con una combinación única de bits.""")
st.image("./img/A4-4.png", caption="Circuito Para Conteo Entre 0 y 9")