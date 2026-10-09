import streamlit as st

def render_emotional_lab_tab():
    st.markdown('<h2 class="main-title">Laborator Emoțional</h2>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text" style="text-align: center;">Experimente interactive pe axele taxonomiei afective Plutchik</p>', unsafe_allow_html=True)
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
    st.info("Permite manipularea ponderilor afective pentru a genera noi narațiuni generative adaptive.")
