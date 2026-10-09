import streamlit as st
from config import ARTIST_PERSONAS
from utils.ai_services import get_openai_client

def render_artist_chat_tab():
    """Rendereaza tab-ul interactiv de dialog cu marii artisti ai lumii."""
    st.markdown('<h2 class="main-title">Dialog cu Marii Artiști</h2>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text" style="text-align: center;">Conversație în timp real ghidată de LLM cu personalități artistice istorice</p>', unsafe_allow_html=True)
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

    selected_artist = st.selectbox(
        "Alege artistul cu care dorești să conversezi:",
        list(ARTIST_PERSONAS.keys()),
        index=0
    )

    persona = ARTIST_PERSONAS[selected_artist]
    
    st.info(f"**{selected_artist}:** {persona['greeting']}")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_query = st.chat_input(f"Adresează-i o întrebare lui {selected_artist}...")
    if user_query:
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        try:
            client = get_openai_client()
            messages = [
                {"role": "system", "content": persona["prompt"]},
                *[{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history]
            ]
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=350,
                temperature=0.7
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"*(Mod demonstrativ)* {selected_artist}: Îți împărtășesc viziunea mea despre lumină, formă și pasiune. Arta este o călătorie profundă a sufletului. (Cheia API OpenAI poate fi configurată în `.streamlit/secrets.toml`)."

        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
