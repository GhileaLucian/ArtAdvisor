import streamlit as st
import os
from PIL import Image

def render_gallery_tab():
    """Rendereaza galeria de opere de arta clasice."""
    st.markdown('<h2 class="main-title">Galeria de Opere de Artă</h2>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text" style="text-align: center;">Colecții reprezentative structurate pe curente artistice și maeștri clasici</p>', unsafe_allow_html=True)
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    sample_artworks = [
        {"title": "Noaptea Înstelată", "artist": "Vincent van Gogh", "year": "1889", "movement": "Post-Impresionism", "emotion": "Wonder & Melancholy"},
        {"title": "Mona Lisa", "artist": "Leonardo da Vinci", "year": "1503", "movement": "Renaștere", "emotion": "Serenity & Mystery"},
        {"title": "Nuferi", "artist": "Claude Monet", "year": "1916", "movement": "Impresionism", "emotion": "Peace & Light"},
        {"title": "Guernica", "artist": "Pablo Picasso", "year": "1937", "movement": "Cubism & Expresionism", "emotion": "Anguish & Turmoil"},
        {"title": "Rondul de Noapte", "artist": "Rembrandt", "year": "1642", "movement": "Baroc", "emotion": "Majesty & Vigilance"},
        {"title": "Persistența Memoriei", "artist": "Salvador Dalí", "year": "1931", "movement": "Suprarealism", "emotion": "Introspection & Time"}
    ]

    cols = st.columns(3)
    for idx, art in enumerate(sample_artworks):
        with cols[idx % 3]:
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border: 1px solid rgba(212,175,55,0.2); margin-bottom: 15px;">
                <h4 style="color: #D4AF37; margin: 0;">{art['title']}</h4>
                <p style="color: #bbb; margin: 5px 0;"><strong>Artist:</strong> {art['artist']} ({art['year']})</p>
                <p style="color: #bbb; margin: 0;"><strong>Curent:</strong> {art['movement']}</p>
                <p style="color: #aaa; margin: 0; font-size: 0.85rem;"><strong>Amprentă afectivă:</strong> {art['emotion']}</p>
            </div>
            """, unsafe_allow_html=True)
