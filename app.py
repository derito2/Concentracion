
# import streamlit as st

# if "page" not in st.session_state:
#     st.session_state.page = "principal"

# with st.sidebar:
#     st.image("danu.png", use_container_width=True)
#     #st.markdown("### Navegación")

#     if st.button("Principal"):
#         st.session_state.page = "principal"

#     if st.button("Clientes"):
#         st.session_state.page = "clientes"

#     if st.button("Modelo"):
#         st.session_state.page = "modelo"

# # Cargar la página correspondiente
# if st.session_state.page == "principal":
#     import views.principal as principal
#     principal.show()

# elif st.session_state.page == "clientes":
#     import views.clientes as clientes
#     clientes.show()

# elif st.session_state.page == "modelo":
#     import views.modelo as modelo
#     modelo.show()






import streamlit as st


## --- PAGE SETUP --- ##

principal = st.Page(
    page="views/principal.py",
    title="Principal",
    default=True,
)

clientes = st.Page(
    page="views/clientes.py",
    title="Clientes",
)

modelo = st.Page(
    page="views/modelo.py",
    title="Modelo",
)

pg = st.navigation(pages=[principal, clientes, modelo])

pg.run() 