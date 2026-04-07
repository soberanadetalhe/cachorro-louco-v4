import streamlit as st

# Versão 4.3 - Edição "Nitidez Máxima" | 07/04/2026 16:30
st.set_page_config(page_title="Cachorro Louco GYN", page_icon="🐶", layout="wide")

# CSS para forçar nitidez e estilo industrial
st.markdown("""
<style>
    .main { background-color: #0e1117; color: #ffffff; }
    
    /* Forçar nitidez em imagens que o navegador tenta suavizar */
    img {
        image-rendering: -webkit-optimize-contrast;
        image-rendering: crisp-edges;
        border-radius: 10px;
        border: 1px solid #333;
    }
    
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background-color: #1c1f26; color: #ffffff; 
        font-weight: bold; border-radius: 5px;
    }
    .stTabs [aria-selected="true"] { 
        background-color: #facc15 !important; color: #000000 !important; 
    }
</style>
""", unsafe_allow_html=True)

# Link da Imagem - USE O LINK QUE TERMINA EM .jpg PARA ALTA RESOLUÇÃO
# Se a imagem continuar ruim, é porque o arquivo original subido tem resolução baixa.
IMG_LOGO_HD = "https://i.ibb.co/B5MR52nN/47638.jpg"

st.markdown(f"""
<div style="text-align: center; padding: 15px; border-bottom: 3px solid #facc15; background-color: #1a1a1a;">
    <h1 style="color: #facc15; margin:0;">🐶 CACHORRO LOUCO LAVA JATO</h1>
    <p style="color: #ffffff; margin:0;">SISTEMA DE ESTÉTICA AVANÇADA</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚗 AUTOMOTIVO", "🛋️ RESIDENCIAL", "📲 CONTATO"])

with tab1:
    col1, col2 = st.columns([1, 1])
    with col1:
        # Usando use_container_width=True para o Streamlit ajustar ao espaço
        st.image(IMG_LOGO_HD, caption="Padrão Cachorro Louco GYN", use_container_width=True)
    with col2:
        st.markdown("### 🛞 Estética Automotiva")
        st.info("Tratamento de elite para o seu veículo.")
        st.write("- Lavagem Detalhada\n- Higienização Interna\n- Proteção de Verniz")
        st.button("VER GALERIA DE RESULTADOS")

with tab2:
    col3, col4 = st.columns([1, 1])
    with col3:
        st.markdown("### 🛋️ Higienização de Estofados")
        st.success("✅ Sofás, Colchões e Tapetes")
        st.write("Eliminação de fungos, ácaros e sujeira profunda com extratoras de alta pressão.")
    with col4:
        # Mantendo a consistência visual
        st.image(IMG_LOGO_HD, use_container_width=True)

with tab3:
    st.markdown("### ⚡ Orçamento Instantâneo")
    if st.button("CHAMAR NO WHATSAPP"):
        st.markdown("Redirecionando para Johnny...")

st.markdown("---")
st.markdown("<center><b>Powered by Oráculo System | GYN Pro Mundo © 2026</b></center>", unsafe_allow_html=True)
