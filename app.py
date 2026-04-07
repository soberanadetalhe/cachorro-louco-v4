import streamlit as st

# Versão 4.2 - Edição "Alpha" | 07/04/2026 16:20
st.set_page_config(page_title="Cachorro Louco GYN", page_icon="🐶", layout="wide")

# Interface Industrial Dark (Sistema Oráculo)
st.markdown("""
<style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: #0e1117; }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background-color: #1c1f26; color: #ffffff; 
        font-weight: bold; border-radius: 5px 5px 0 0; border: 1px solid #333;
    }
    .stTabs [aria-selected="true"] { 
        background-color: #facc15 !important; color: #000000 !important; 
        border: 1px solid #facc15 !important;
    }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e3137,#0e1117); }
</style>
""", unsafe_allow_html=True)

# Link Direto da Imagem Principal (Cachorro Louco)
IMG_LOGO = "https://i.ibb.co/B5MR52nN/47638.jpg"

# --- SIDEBAR (MENU DE COMANDO) ---
with st.sidebar:
    st.image(IMG_LOGO, use_container_width=True)
    st.markdown("### 🛠️ OPERAÇÃO GYN")
    st.info("Operador: Johnny\n\nLocal: Goiânia - GO")
    st.markdown("---")
    st.write("V 4.2 | 2026 ©")

# --- CORPO PRINCIPAL ---
st.markdown(f"""
<div style="text-align: center; padding: 10px; border: 2px solid #facc15; border-radius: 10px; background-color: #1a1a1a;">
    <h1 style="color: #facc15; margin:0;">CACHORRO LOUCO LAVA JATO</h1>
    <p style="color: #ffffff; font-size: 20px;">SÓ PARA QUEM GOSTA DE CARRO LIMPO E SEM RODEIOS</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚗 AUTOMOTIVO", "🛋️ CASA (ESTOFADOS)", "📲 ORÇAMENTO"])

with tab1:
    col1, col2 = st.columns([1.2, 1])
    with col1:
        # Aqui entra a sua foto de Estética Automotiva
        st.image("https://images.unsplash.com/photo-1520340356584-f9917d1eea6f?q=80&w=1000", caption="Serviço de Elite")
    with col2:
        st.markdown("### ⚡ Estética Automotiva")
        st.write("Onde o brilho encontra a brutalidade.")
        st.markdown("""
        - **Lavagem Técnica Detalhada**
        - **Higienização de Bancos** (Couro/Tecido)
        - **Limpeza de Motor e Chassi**
        - **Proteção e Revitalização**
        """)
        st.warning("⚠️ Atendimento com agendamento prévio.")

with tab2:
    col3, col4 = st.columns([1, 1.2])
    with col3:
        st.markdown("### 🏠 Casa Renovada")
        st.write("Tecnologia industrial no seu sofá.")
        st.success("✅ Higienização de Sofás e Poltronas")
        st.success("✅ Limpeza de Tapetes e Carpetes")
        st.success("✅ Tratamento Anti-ácaro em Colchões")
        st.markdown("**Utilizamos extratoras profissionais de alta sucção.**")
    with col4:
        # Mantendo o padrão Cachorro Louco também nesta seção conforme solicitado
        st.image(IMG_LOGO, caption="Padrão Cachorro Louco de Limpeza", use_container_width=True)

with tab3:
    st.markdown("### 💰 Solicitar Orçamento")
    with st.form("orcamento"):
        tipo = st.selectbox("Selecione o serviço:", ["Completo (Carro + Casa)", "Só Automotivo", "Só Estofados", "Tapetes"])
        obs = st.text_input("Alguma observação específica?")
        submit = st.form_submit_button("GERAR LINK WHATSAPP")
        
        if submit:
            msg = f"Fala Johnny! Quero um orçamento para {tipo}. Obs: {obs}"
            link_wa = f"https://wa.me/556291760052?text={msg.replace(' ', '%20')}"
            st.markdown(f'''
                <a href="{link_wa}" target="_blank">
                    <button style="width:100%; height:50px; background-color:#25d366; color:white; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">
                        ABRIR CONVERSA NO WHATSAPP
                    </button>
                </a>
            ''', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center><b>Powered by Oráculo System | GYN Pro Mundo</b></center>", unsafe_allow_html=True)
