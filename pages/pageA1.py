import streamlit as st
import pandas as pd

st.title("Asignación 1")
st.subheader("INVERTIGAR SOBRE LOS SOFTWARE DE DISEÑO ASISTIDO POR COMPUTADORAS, QUE TENEMOS EN EL MERCADO ACTUAL DE ESTE TIPO DE SOFTWARE")

#----
st.write("")
st.write("#### :blue[QUÉ ES EL DISEÑO ASISTIDO POR COMPUTADORA]")

col1, col2 = st.columns(2)
with col1:
    st.write("El diseño asistido por computadora, comúnmente conocido como CAD (Computer-Aided Design), es una tecnología que utiliza sistemas informáticos para ayudar en la creación, modificación, análisis y optimización de un diseño. Esta herramienta permite a ingenieros, arquitectos y otros profesionales del diseño crear representaciones gráficas precisas de objetos físicos en dos o tres dimensiones.")
with col2:
    st.markdown("![CAD](https://cadrep.com/wp-content/uploads/2021/09/1c2f556480f704eed223041d207c9049.gif)")

#----
st.write("")
st.write("#### :blue[Ingenierias en las que se aplica CAD]")

col1, col2 = st.columns(2)

# ...organiza cada ingenieria para que siga el formato de la columna
with col1:
    st.write("##### Ingeniería Mecánica")
    st.write("Diseño de piezas, máquinas, herramientas, sistemas de transmisión, y análisis de estrés y fatiga.")
    st.write("")

    st.write("##### Ingeniería Civil")
    st.write("Diseño de edificios, puentes, carreteras, sistemas de alcantarillado, y planificación urbana.")
    st.write("")

    st.write("##### Arquitectura")
    st.write("Creación de planos, diseño de interiores, modelado 3D de edificios, y visualización arquitectónica.")
    st.write("")

    st.write("##### Ingeniería Biomédica")
    st.write("Diseño de prótesis, implantes, equipos médicos, y modelado de sistemas biológicos.")
    st.write("")

    st.write("##### Animación y Efectos Visuales")
    st.write("Modelado 3D para películas, videojuegos, y realidad virtual.")
    st.write("")

    st.write("##### Ingeniería de Materiales")
    st.write("Análisis de estructuras moleculares, diseño de nuevos materiales, y simulación de propiedades físicas.")
    st.write("")

    st.write("##### Ingeniería Química")
    st.write("Diseño de plantas de procesamiento, equipos de producción, y simulación de procesos químicos.")
    st.write("")

    st.write("##### Ingeniería de Telecomunicaciones")
    st.write("Diseño de antenas, redes de comunicación, y sistemas de transmisión.")
    st.write("")

    st.write("##### Ingeniería Óptica")
    st.write("Diseño de lentes, sistemas de iluminación, y dispositivos ópticos.")
    st.write("")

    st.write("##### Ingeniería Textil")
    st.write("Diseño de patrones, simulación de tejidos, y creación de modelos de ropa.")
    st.write("")

    st.write("##### Ingeniería Nuclear")
    st.write("Diseño de reactores, sistemas de contención, y modelado de procesos nucleares.")
    st.write("")

    st.write("##### Ingeniería de Alimentos")
    st.write("Diseño de equipos de procesamiento, empaquetado, y modelado de procesos alimentarios.")
    st.write("")

    st.write("##### Ingeniería de Seguridad")
    st.write("Diseño de sistemas de protección contra incendios, equipos de seguridad personal, y simulación de evacuaciones.")
    st.write("")

    st.write("##### Ingeniería Forense")
    st.write("Reconstrucción de accidentes, análisis de fallos estructurales, y simulación de eventos.")
    st.write("")

    st.write("##### Ingeniería de Software")
    st.write("Diseño de interfaces de usuario, modelado de arquitecturas de software.")
    st.write("")

    st.write("##### Ingeniería Hidráulica")
    st.write("Diseño de presas, canales, sistemas de bombeo y turbinas hidráulicas.")
    st.write("")

    st.write("##### Ingeniería de Plásticos")
    st.write("Diseño de moldes, simulación de inyección de plástico, y análisis de propiedades.")
    st.write("")

with col2:
    st.write("##### Ingeniería Eléctrica y Electrónica")
    st.write("Diseño de circuitos, PCBs, sistemas de distribución eléctrica, y componentes electrónicos.")
    st.write("")

    st.write("##### Ingeniería Aeroespacial")
    st.write("Diseño de aeronaves, satélites, cohetes, y componentes aeroespaciales.")
    st.write("")

    st.write("##### Ingeniería Automotriz")
    st.write("Diseño de carrocerías, sistemas de propulsión, interiores de vehículos, y simulación de crash tests.")
    st.write("")

    st.write("##### Diseño Industrial")
    st.write("Creación de productos de consumo, mobiliario, y bienes manufacturados.")
    st.write("")

    st.write("##### Ingeniería Naval")
    st.write("Diseño de barcos, submarinos, plataformas offshore, y sistemas de propulsión marina.")
    st.write("")

    st.write("##### Geología y Mineríaz")
    st.write("Modelado de yacimientos, planificación de minas, y diseño de equipos de extracción.")
    st.write("")

    st.write("##### Ingeniería Aeronáutica")
    st.write("Diseño de turbinas, fuselajes, y sistemas de control de vuelo.")
    st.write("")

    st.write("##### Ingeniería Robótica")
    st.write("Diseño de robots industriales, prótesis robóticas, y sistemas de automatización.")
    st.write("")

    st.write("##### Ingeniería Acústica")
    st.write("Diseño de sistemas de sonido, aislamiento acústico, y modelado de propagación del sonido.")
    st.write("")

    st.write("##### Ingeniería de Energías Renovables")
    st.write("Diseño de turbinas eólicas, paneles solares, y sistemas de energía limpia.")
    st.write("")

    st.write("##### Ingeniería Ambiental")
    st.write("Diseño de sistemas de tratamiento de agua, control de emisiones, y gestión de residuos.")
    st.write("")

    st.write("##### Ingeniería Agrícola")
    st.write("Diseño de maquinaria agrícola, sistemas de riego, y planificación de cultivos.")
    st.write("")

    st.write("##### Ingeniería de Packaging")
    st.write("Diseño de embalajes, optimización de formas para transporte y almacenamiento.")
    st.write("")

    st.write("##### Ingeniería de Sistemas")
    st.write("Modelado de sistemas complejos, análisis de interacciones entre componentes.")
    st.write("")

    st.write("##### Ingeniería Ferroviaria")
    st.write("Diseño de trenes, vías férreas, y sistemas de señalización.")
    st.write("")

    st.write("##### Ingeniería Costera")
    st.write("Diseño de estructuras de protección costera, modelado de erosión y sedimentación.")
    st.write("")

    st.write("##### Ingeniería de Climatización")
    st.write("Diseño de sistemas HVAC, modelado de flujo de aire y transferencia de calor.")
    st.write("")

    st.write("##### Ingeniería de Iluminación")
    st.write("Diseño de sistemas de iluminación, análisis de distribución lumínica.")
    st.write("")

#----
st.write("")
st.write("#### :blue[Mapa sobre los Tipos de Software CAD]")
st.image("img/A1-2.png")

#----
st.write("")
st.write("#### :blue[En que consiste el Software CAD]")
col1, col2 = st.columns(2)
with col1:
    st.markdown("![CAD](https://i.pinimg.com/originals/37/ff/34/37ff3403b827af202c55a6a4cf3e2ea1.gif)")

with col2:
    st.write("El software de CAD consiste en un conjunto de herramientas que permiten crear, modificar, analizar y optimizar diseños en 2D y 3D. Entre las características principales del software CAD: Modelado geométrico, Visualización, Simulación y Análisis,  Documentación, Colaboración, Bibliotecas de componentes, Parametrización.")

#----
st.write("")
st.write("#### :blue[Lista de Software CAD]")
col1, col2 = st.columns(2)
with col1:
    st.markdown("- AutoCAD (Autodesk)")
    st.markdown("- Maya (Autodesk)")
    st.markdown("- SolidWorks (Dassault Systemes)")
    st.markdown("- CATIA (Dassault Systemes)")
    st.markdown("- Fusion 360 (Autodesk)")
    st.markdown("- Inventor (Autodesk)")
    st.markdown("- Creo (PTC)")
    st.markdown("- NX (Siemens)")
    st.markdown("- Solid Edge (Siemens)")
    st.markdown("- Rhinoceros 3D (Robert McNeel & Associates)")
    st.markdown("- Tinkercad (Autodesk, basado en web)")
    st.markdown("- Cinema 4D")
    st.markdown("- ArchiCAD (Graphisoft)")
    st.markdown("- Revit (Autodesk)")
    st.markdown("- IronCAD")
    st.markdown("- KeyCreator (Kubotek3D)")
    st.markdown("- Alibre Design")
    st.markdown("- SpaceClaim (ANSYS)")
    st.markdown("- T-FLEX CAD (Top Systems)")
    st.markdown("- MEDUSA4 (CAD Schroer)")
    st.markdown("- QCAD (RibbonSoft)")
    st.markdown("- nanoCAD (Nanosoft)")

with col2:
    st.markdown("- SketchUp (Trimble)")
    st.markdown("- FreeCAD (Software libre)")
    st.markdown("- LibreCAD (Software libre)")
    st.markdown("- OnShape (PTC)")
    st.markdown("- BricsCAD (Bricsys)")
    st.markdown("- ZWCAD (ZWSOFT)")
    st.markdown("- DraftSight (Dassault Systèmes)")
    st.markdown("- TurboCAD (IMSI Design)")
    st.markdown("- Vectorworks (Nemetschek)")
    st.markdown("- MicroStation (Bentley Systems)")
    st.markdown("- VariCAD")
    st.markdown("- ARES Commander (Graebert)")
    st.markdown("- CorelCAD (Corel Corporation)")
    st.markdown("- ZW3D (ZWSOFT)")
    st.markdown("- Gstarsoft")
    st.markdown("- GstarCAD")
    st.markdown("- progeCAD (progeSOFT)")
    st.markdown("- DesignSpark Mechanical (RS Components)")
    st.markdown("- SolveSpace (Software libre)")
    st.markdown("- OpenSCAD (Software libre)")
    st.markdown("- Blender (Software libre, con capacidades CAD)")

#----
st.write("")
st.write("#### :blue[Áreas o Instituciones que utilizan CAD en Panamá]")
col1, col2 = st.columns(2)
with col1:
    st.markdown("##### Arquitectura y Construcción")
    st.markdown("- Constructora Urbana S.A. (CUSA)")
    st.markdown("- Constructora Rodak, Grupo Motta")

    st.markdown("##### Ingeniería Civil")
    st.markdown("- Ministerio de Obras Públicas (MOP)")
    st.markdown("- Metro de Panamá")

    st.markdown("##### Industria Marítima")
    st.markdown("- Autoridad del Canal de Panamá (ACP)")
    st.markdown("- Astilleros Nacionales S.A. (ANSA)")

with col2:
    st.markdown("##### Educación Superior")
    st.markdown("- Universidad de Panamá")
    st.markdown("- Universidad Tecnológica de Panamá (UTP)")

    st.markdown("##### Sector Energético")
    st.markdown("- ENSA (Elektra Noreste S.A.)")
    st.markdown("- AES Panamá")

#----
st.write("")
st.write("#### :blue[Resultados para las empresas sobre el uso de los aplicativos y contribuciones de los productos de los Software de CAD]")
col1, col2 = st.columns(2)

with col1:
    st.markdown("* Aumento de la productividad")
    st.markdown("* Mejora en la precisión y calidad")
    st.markdown("* Reducción de costos")
    st.markdown("* Personalización y flexibilidad")
    st.markdown("* Innovación acelerada")

with col2:
    st.markdown("* Mejora en la colaboración")
    st.markdown("* Integración con otras tecnologías")
    st.markdown("* Mejora en la visualización y presentación")
    st.markdown("* Competitividad mejorada")
    st.markdown("* Optimización de recursos")

#----
st.write("")
st.write("#### :blue[SUB AREAS DEL CAD]")
data = {
    'Área de CAD': ['CAM (Fabricación Asistida por Computadora)', 'CAE (Ingeniería Asistida por Computadora)', 'CIM (Fabricación Integrada por Computadora)'],
    'En que consiste': ['uso de sistemas informáticos para planificar, gestionar, automatizar y controlar las operaciones de una planta de fabricación', 'uso de software para simular y analizar el comportamiento de productos y sistemas antes de su fabricación.', 'Se refiere a la integración de sistemas informáticos en toda la cadena de valor de la fabricación, desde el diseño hasta la distribución.'],
    'Ventajas': ['Aumenta la eficiencia y precisión en la producción, reduce errores y costos, mejora la calidad de los productos y permite la fabricación de piezas complejas.', 'Mayor eficiencia y calidad, ya que permite prever posibles errores y corregir antes de la fase de prototipo y fabricación.', 'Aumenta la eficiencia y productividad en toda la cadena de suministro, mejora la calidad y consistencia de los productos, reduce tiempos de ciclo y costos, facilita la colaboración entre equipos y departamentos.'],
    'Contribuciones': ['Desarrollo de máquinas CNC (control numérico por computadora), sistemas de programación CAM avanzados, integración con sistemas ERP y PLM, fabricación aditiva (impresión 3D).', 'Desarrollo de software de análisis estructural (FEM), simulación de fluidos computacional (CFD), análisis térmico, simulación electromagnética.', 'Desarrollo de sistemas ERP (Planificación de Recursos Empresariales), Sistemas de gestión de la calidad (QMS).'],
}

df = pd.DataFrame(data)
st.table(df)

#----
st.write("")
st.write("#### :blue[Software CAD elegido]")
col1, col2 = st.columns(2)
with col1:
    st.markdown("![MAYA](https://logowik.com/content/uploads/images/autodesk-maya6778.logowik.com.webp)")
    st.markdown("Autodesk Maya es un software 3D profesional para crear personajes realistas y efectos dignos de películas taquilleras.")

with col2:
    st.image("./img/A1-3.jpg", caption="Animación de los personajes de Guardianes de la Galaxia vol. 3")

#----
st.write("")
st.write("#### :blue[Ventajas de MAYA]")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Modelado 3D avanzado**: Ofrece herramientas de modelado poligonal, NURBS y subdivisión de superficies.")
    st.markdown("**Animación de alta calidad**: Incluye animación de personajes, rigging, y simulación de físicas.")
    st.markdown("**Renderizado potente**: Integra Arnold como motor de renderizado predeterminado.")
    st.markdown("**Efectos visuales**: Ofrece herramientas avanzadas para la creación de efectos especiales.")

with col2:
    st.markdown("**Integración con otras herramientas de Autodesk**:  Se integra bien con otros productos de Autodesk como 3ds Max y MotionBuilder.")
    st.markdown("**Personalización y extensibilidad**:  Permite la creación de scripts y plugins personalizados.")
    st.markdown("**Actualizaciones regulares**:  Autodesk proporciona actualizaciones frecuentes con nuevas características y mejoras.")
    st.markdown("**Soporte para realidad virtual y aumentada**:  Incluye herramientas para crear contenido para VR y AR.")

#----
st.write("")
st.write("#### :blue[Deventajas de MAYA]")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Curva de aprendizaje empinada**:  Requiere tiempo y dedicaci n para dominar todas sus funcionalidades.")
    st.markdown("**Costo elevado**:  El software tiene un precio alto, especialmente para usuarios individuales o peque as empresas.")
    st.markdown("**Requisitos de hardware**:  Necesita un hardware potente para funcionar eficientemente, especialmente para proyectos complejos.")
    st.markdown("**Complejidad de la interfaz**:  La interfaz de usuario puede ser complicada debido a la gran cantidad de herramientas y opciones.")

with col2:
    st.markdown("**Estabilidad**:  Ocasionalmente puede sufrir problemas de estabilidad, especialmente con proyectos muy grandes o complejos.")
    st.markdown("**Enfoque en la industria del entretenimiento**:  Aunque es versátil, está más orientado hacia la industria del cine y los videojuegos.")
    st.markdown("**Tiempo de renderizado**:  Los tiempos de renderizado pueden ser largos para escenas complejas, incluso con hardware potente.")
    st.markdown("**Dependencia de plugins**:  Algunas funcionalidades avanzadas requieren plugins adicionales, que pueden aumentar el costo total.")

#----
st.write("")
st.write("#### :blue[Descripción General de la Interfaz]")
st.markdown("![Intrefaz de MAYA](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Basics/images/GUID-48F006ED-B5CD-4D18-AA3B-9C0D07B4E825.png)")

st.markdown("1. **Conjuntos de menús**: Los conjuntos de menús dividen el tipo de menús disponibles en categorías: Modelado, Rigging, Animación, FX y Renderizado.")
st.markdown("2. **Menús**: Los menús contienen tanto herramientas como acciones para trabajar en su escena.")
st.markdown("3. **Línea de estado**: La línea de estado contiene iconos para algunos comandos generales de uso común, como Archivo > Guardar, así como iconos para configurar la selección de objetos, el ajuste, el renderizado, etc.")
st.markdown("4. **Menú Cuenta de usuario**: Inicie sesión en su cuenta de Autodesk.")
st.markdown("5. **Estante**: La estantería contiene iconos para tareas comunes, organizados por pestañas basadas en categorías.")
st.markdown("6. **Selector de espacio de trabajo**: Seleccione una disposición personalizada o predefinida de ventanas y paneles diseñados para diferentes flujos de trabajo.")
st.markdown("7. **Iconos de la barra lateral**: Los iconos situados en el extremo derecho de la línea de estado abren y cierran herramientas que utilizará con frecuencia. De izquierda a derecha, los iconos muestran el kit de herramientas de modelado, la ventana HumanIK, el editor de atributos, la configuración de herramientas y el editor de cajas de canal/capas.")
st.markdown("8. **Cuadro de canales**: El cuadro de canales le permite editar los atributos y valores clave de los objetos seleccionados.")
st.markdown("9. **Editor de capas**: Hay dos tipos de capas que se muestran en el Editor de capas: Las capas de visualización se utilizan para organizar y gestionar los objetos de una escena, por ejemplo, para configurar su visibilidad y capacidad de selección. Las capas de animación se utilizan para mezclar, bloquear o silenciar varios niveles de animación.")
st.markdown("10. **Panel de vista**: El panel Vista ofrece diferentes formas de ver los objetos de la escena con una vista de cámara. ")
st.markdown("11. **Caja de Herramientas**: La Caja de Herramientas contiene herramientas que usted utiliza todo el tiempo para seleccionar y transformar objetos en su escena.")
st.markdown("12. **Botones de diseño rápido/Outliner**: Los tres botones superiores de Disposición rápida situados debajo de la Caja de herramientas le permiten cambiar entre las útiles disposiciones del panel Vista.")
st.markdown("13. **Deslizador de tiempo**: El Deslizador de Tiempo muestra el rango de tiempo disponible definido por el deslizador de rango.")
st.markdown("14. **Deslizador de rango**: El Deslizador de Rango te permite establecer el tiempo de inicio y fin de la animación de la escena..")
st.markdown("15. **Controles de reproducción**: Los Controles de Reproducción te permiten moverte en el tiempo y previsualizar tu animación según lo definido por el rango del Deslizador de Tiempo.")
st.markdown("16. **Menús Anim/Carácter**: Los menús de Animación o Personaje te permiten cambiar la Capa de Animación y el Juego de Personajes actual.")
st.markdown("17. **Opciones de Reproducción**: Utiliza las opciones de Reproducción para controlar cómo se reproduce la animación en tu escena.")
st.markdown("18. **Línea de ayuda**: La Línea de ayuda ofrece una breve descripción de las herramientas y los elementos de menú a medida que se desplaza sobre ellos en la interfaz de usuario.")
st.markdown("19. **Línea de comandos**: La Línea de comandos tiene un área a la izquierda para introducir comandos MEL individuales, y un área a la derecha para comentarios.")

#----
st.write("")
st.write("#### :orange[Diferencias entre AutoCAD y MAYA]")
col1, col2 = st.columns(2)
col1.write("##### :red[AutoCAD]")
col2.write("##### :blue[MAYA]")
st.write("##### Diferencias en Componentes")
col1, col2 = st.columns(2)
with col1:
    st.markdown("- **Dibujo 2D y 3D**: Ofrece herramientas para crear formas, líneas, curvas y sólidos.")
    st.markdown("- **Diseño asistido por computadora (CAD)**: Se utiliza principalmente para proyectos arquitectónicos, ingeniería y diseño industrial.")
    st.markdown("- **Renderizado**: Puede producir imágenes realistas a partir de modelos 3D.")
    st.markdown("- **Animación básica**: Permite crear animaciones simples, pero no es su especialidad.")

with col2:
    st.markdown("- **Modelado 3D**: Especializado en la creación de modelos 3D detallados y complejos.")
    st.markdown("- **Animación**: Ofrece herramientas avanzadas para crear animaciones realistas y complejas.")
    st.markdown("- **Renderizado**: Produce imágenes y animaciones de alta calidad.")
    st.markdown("- **Simulación**: Puede simular fenómenos físicos como el movimiento de líquidos, partículas y deformaciones.")

st.write("##### Ventajas")
col1, col2 = st.columns(2)
with col1:
    st.markdown("- **Fácil de usar**: Tiene una interfaz intuitiva y es accesible para usuarios con poca experiencia.")
    st.markdown("- **Versátil**: Se puede utilizar en una amplia variedad de industrias.")
    st.markdown("- **Gran base de usuarios**: Cuenta con una comunidad activa y muchos recursos disponibles.")

with col2:
    st.markdown("- **Potente para el modelado y la animación**: Ofrece herramientas avanzadas para crear personajes, entornos y efectos especiales.")
    st.markdown("- **Ideal para la producción de películas y videojuegos**: Se utiliza ampliamente en la industria del entretenimiento.")
    st.markdown("- **Alta calidad de renderizado**: Produce imágenes y animaciones foto realistas.")

st.write("##### Desventajas")
col1, col2 = st.columns(2)
with col1:
    st.markdown("- **Puede ser lento para proyectos grandes**: Puede ser menos eficiente que Maya para proyectos complejos.")
    st.markdown("- **Limitado en cuanto a animación**: No es tan adecuado para crear animaciones complejas como Maya.")

with col2:
    st.markdown("- **Complejo de aprender**: Tiene una curva de aprendizaje más pronunciada que AutoCAD.")
    st.markdown("- **Requiere hardware potente**: Puede ser exigente en términos de recursos del sistema.")

#----
st.write("")
st.write("#### :blue[Diseño de objeto con SmartArt y con software de CAD]")
st.image("./img/A1-4.png", caption="Diseño Base realizado en Office", width=500)
st.image("./img/A1-5.png", caption="Diseño realizado en MAYA (TOP)", width=500)
st.image("./img/A1-6.png", caption="Diseño realizado en MAYA (HOME)", width=500)

#----
st.write("")
st.write("#### :blue[Conclusión]")
st.write("""
Este fue mi primer acercamiento a un software de CAD, específicamente Autodesk Maya. Aprendí cosas como moverme en el espacio de trabajo, además de cómo mover, rotar y escalar una figura o un sólido.
""")