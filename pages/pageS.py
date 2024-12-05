import streamlit as st

st.title("Ingeniera en Energías Renovables")

st.write("### :blue[Qué es y en qué consiste]")

col1, col2 = st.columns(2)
with col1:
    st.write("La Ingeniería en Energías Renovables es una disciplina profesional especializada que se enfoca en el diseño, desarrollo, implementación y gestión de sistemas de generación de energía provenientes de fuentes naturales renovables e inagotables. Su objetivo principal es transformar los recursos naturales como el sol, el viento, el agua y la biomasa en energía eléctrica o térmica de manera sostenible y eficiente.")

with col2:
    st.markdown("![Paneles Solares](https://www.solartechmexico.com/wp-content/uploads/2024/02/cuanto_cuesta_poner_paneles_solares_en_mexico.webp)")


#----
st.write("### :blue[¿Cómo se utiliza?]")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
- **Diseño de parques solares fotovoltaicos**: Evaluando la ubicación, orientación e instalación de paneles solares para máxima captación energética.
- **Planificación de proyectos eólicos**: Seleccionando sitios estratégicos para aerogeneradores y optimizando su rendimiento.
- **Desarrollo de sistemas de energía hidroeléctrica**: Evaluando recursos hídricos y diseñando infraestructuras para generación eléctrica.
- **Implementación de sistemas de biomasa**: Transformando residuos orgánicos en fuentes de energía aprovechables.
- **Análisis de viabilidad técnica y económica**: Evaluando diferentes proyectos de energías renovables.
""")

with col2:
    st.markdown("![Aerogeneradores](https://mediacdn.acciona.com/media/40ecurus/accciona-aerogeneradores.jpg)")
    st.markdown("![Panel Solar](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvp41TLoMIetOzQUqK6SgD3yDYZ0E7U3SCZw&s)")

    
#----
st.write("### :blue[¿Cuáles son los beneficios para la sociedad?]")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
### Medioambientales

- Reducción de las emisiones de gases de efecto invernadero
- Mitigación del cambio climático
- Disminución de la contaminación
- Protección de los recursos naturales

### Económicos

- Creación de nuevos empleos
- Reducción de la dependencia de combustibles fósiles
- Aumento de la seguridad energética

### Sociales

- Mejora de la calidad de vida
- Acceso a la energía en zonas remotas
- Promoción del desarrollo sostenible
""")

with col2:
    st.markdown("![Beneficios](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjcWqoJaz2s4D4q7XqPEkAvEyii6HGCmwzVw&s)")


#----
st.write("")
st.write("### :blue[Visualización de Diseños:]")
st.write("### :orange[Panel Solar]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a49228566b345e8624?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)

#----
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
### Características
- Dispositivos que convierten luz solar en electricidad
- Fabricados con células fotovoltaicas de silicio
- Funcionan con radiación solar directa e indirecta
- Vida útil aproximada de 25-30 años
- No generan ruido ni emisiones
""")

    st.write("")

    st.markdown("""
### Ventajas
- Energía limpia y renovable
- Bajos costos de mantenimiento
- Reducción de facturas eléctricas
- Aplicables en múltiples escalas
- No contaminan durante su operación
""")

with col2:

    st.markdown("""
### Configuración
- Paneles individuales
- Arreglos en serie o paralelo
- Sistemas conectados a red
- Sistemas autónomos o aislados
- Con o sin sistemas de seguimiento solar
""")

    st.write("")

    st.markdown("""
### Desventajas
- Alta inversión inicial
- Dependencia de condiciones climáticas
- Eficiencia limitada (15-22%)
- Requieren espacio significativo
- Producción intermitente
""")


st.write("### :orange[Aerogeneradores]")
st.markdown('<iframe src="https://myup3745.autodesk360.com/shares/public/SH286ddQT78850c0d8a460b952cd507a3459?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>', unsafe_allow_html=True)

#----
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
### Características
- Dispositivos que convierten luz solar en electricidad
- Fabricados con células fotovoltaicas de silicio
- Funcionan con radiación solar directa e indirecta
- Vida útil aproximada de 25-30 años
- No generan ruido ni emisiones
""")

    st.write("")

    st.markdown("""
### Ventajas
- Energía renovable
- Bajo costo operativo
- No generan emisiones
- Aprovechamiento de espacios
- Generación en zonas rurales
- Complementariedad con otras renovables
""")

with col2:
    st.markdown("""
### Configuración
- Paneles individuales
- Arreglos en serie o paralelo
- Sistemas conectados a red
- Sistemas autónomos o aislados
- Con o sin sistemas de seguimiento solar
""")

    st.write("")
        
    st.markdown("""
### Desventajas
- Impacto visual
- Ruido
- Afectación a fauna voladora
- Dependencia de condiciones meteorológicas
- Alta inversión inicial
- Mantenimiento especializado
""")