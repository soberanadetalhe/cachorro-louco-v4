import streamlit as st

# Versão 4.1 - Estável para Nuvem | 07/04/2026 16:05
st.set_page_config(page_title="Cachorro Louco V4.1", page_icon="🐶", layout="wide")

# CSS Industrial Dark
st.markdown("""
<style>
    .main { background-color: #0d1010; color: #ffffff; }
    .stTabs [data-baseweb="tab-list"] { gap: 15px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; background-color: #1a1a1a; color: #facc15; font-weight: bold; border-radius: 5px;
    }
    .stTabs [aria-selected="true"] { background-color: #2563eb !important; color: white !important; }
    div.stButton > button {
        background-color: #2563eb; color: white; border: 2px solid #facc15; font-weight: bold; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Título Blindado
st.markdown("""
<div style="background-color: #1a1a1a; padding: 20px; border-left: 10px solid #facc15; margin-bottom: 20px;">
    <h1 style="color: white; margin:0;">🐶 CACHORRO LOUCO LAVA JATO </h1>
    <h1 style="color: white; margin:0;">HIGIENIZAÇÃO PROFISSIONAL</h1>
    <p style="color: #2563eb; margin:0; font-weight:bold;">Estética Automotiva & Conforto Residencial</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚗 AUTOMOTIVO", " Couch🛋️ ESTOFADOS E TAPETES", "💰 ORÇAMENTO"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("## 🧼 Estética de Elite")
        st.write("Serviço bruto para quem é exigente.")
        st.markdown("* Lavagem Técnica de Motor\n* Higienização Detalhada\n* Proteção de Pintura")
    with c2:
        # Mantendo a primeira imagem original
        st.image("https://images.unsplash.com/photo-1607860108855-64acf2078ed9?auto=format&fit=crop&q=80&w=800")

with tab2:
    c3, c4 = st.columns(2)
    with c3:
        # AQUI ESTÁ O LINK DIRETO QUE RESOLVE O ERRO
        st.image("https://i.ibb.co/HDKm92Lh/1775581320812.jpg")
    with c4:
        st.markdown("## 🏠 Casa Renovada")
        st.write("Nada de sujeira no seu conforto.")
        st.markdown("* Higienização de Sofás\n* Limpeza de Tapetes\n* Tratamento de Colchões\n* Atendimento Domiciliar")
        st.success("✅ Equipamentos de Extração Profissional")

with tab3:
    st.markdown("## 💰 Orçamento")
    escolha = st.selectbox("O que vamos limpar?", ["Carro", "Sofá", "Tapete", "Combo Total"])
    if st.button("💬 CHAMAR NO WHATSAPP"):
        txt = f"Fala Johnny! Orçamento para: {escolha}"
        link = f"https://wa.me/556291760052?text={txt.replace(' ', '%20')}"
        st.markdown(f'<a href="{link}" target="_blank" style="text-decoration: none; color: white; background-color: #25d366; padding: 10px; border-radius: 5px; display: block; text-align: center;">CONFIRMAR PEDIDO NO WHATSAPP</a>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center><b>Cachorro Louco GYN © 2026 | Powered by Oráculo System</b></center>", unsafe_allow_html=True)
