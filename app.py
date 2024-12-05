# streamlit run streamlit_app.py
import streamlit as st

# col1, col2 = st.columns(2)
# col1.write("This is column 1")
# col2.write("This is column 2")

pagA1_page = st.Page(
    page = "pages/pageA1.py",
    title = "A1: Software de CAD",
    icon = "⚙️",
    default = True
)

pagA2_page = st.Page(
    page = "pages/pageA2.py",
    title = "A2: Religiones Alrededor del Mundo",
    icon = "⛪",
)

pagA3_page = st.Page(
    page = "pages/pageA3.py",
    title = "A3: Monedas y Escudos",
    icon = "🛡️",
    # icon = ":material/smart_toy:", #iconos de material design font.google.com/icons
)

pagA4_page = st.Page(
    page = "pages/pageA4.py",
    title = "A4: Brazos Robóticos y Circuitos",
    icon = "️🤖",
)

pagA5_page = st.Page(
    page = "pages/pageA5.py",
    title = "A5: Socket - CPU - Memory",
    icon = "️💻",
)

pagP1_page = st.Page(
    page = "pages/pageP1.py",
    title = "Parcial 1",
    icon = "️📝",
)

pagP2_page = st.Page(
    page = "pages/pageP2.py",
    title = "Parcial 2",
    icon = "️📝",
)

pagP3_page = st.Page(
    page = "pages/pageP3.py",
    title = "Parcial 3",
    icon = "️📝",
)

pagS_page = st.Page(
    page = "pages/pageS.py",
    title = "Ingeniera en Energías Renovables",
    icon = "️📝",
)



# pg = st.navigation(pages=[pagA1_page, pagA2_page, pagA3_page, pagA4_page])

pg = st.navigation(
    {
        "Asignaciones": [pagA1_page, pagA2_page, pagA3_page, pagA4_page, pagA5_page],
        "Parciales": [pagP1_page, pagP2_page, pagP3_page],
        "Semestral": [pagS_page]
    }
)

st.sidebar.text("Made with ❤️‍🔥🥷 by @Uzziel_sw")

pg.run()