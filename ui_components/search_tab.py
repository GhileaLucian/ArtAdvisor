import streamlit as st

def render_search_tab():
    """Rendereaza cautarea avansata in colectia WikiArt / ArtEmis."""
    st.markdown('<h2 class="main-title">Căutare Semiotică Avansată</h2>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text" style="text-align: center;">Filtrare multi-criterială după stil, autor și taxonomie afectivă</p>', unsafe_allow_html=True)
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.selectbox("Curent Artistic:", ["Toate", "Baroc", "Impresionism", "Post-Impresionism", "Suprarealism", "Expresionism", "Realism"])
    with col2:
        st.selectbox("Stare Emoțională:", ["Toate", "Tristețe", "Fericire", "Încredere", "Frică", "Iubire", "Optimism"])
    with col3:
        st.selectbox("Artist:", ["Toți", "Vincent van Gogh", "Claude Monet", "Leonardo da Vinci", "Rembrandt", "Salvador Dalí"])

    st.button("Execută Căutarea în Baza de Date (~14.000 imagini)", use_container_width=True)
    st.info("Rezultatele sunt indexate prin vectori de embedding și cosine similarity în spațiul latent.")
