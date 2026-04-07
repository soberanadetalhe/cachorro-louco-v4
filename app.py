import streamlit as st

# Versão 5.3 - Premium Home & Auto | 07/04/2026 17:45
st.set_page_config(page_title="Cachorro Louco GYN", page_icon="🧼", layout="wide")

# CSS Industrial Dark (Padrão Oráculo)
st.markdown("""
<style>
    .main { background-color: #050505; color: #e0e0e0; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background-color: #111; color: #facc15; 
        font-weight: bold; border-radius: 8px 8px 0 0; border: 1px solid #222;
    }
    .stTabs [aria-selected="true"] { background-color: #2563eb !important; color: white !important; }
    
    img { border-radius: 12px; border: 1px solid #333; object-fit: cover; }
</style>
""", unsafe_allow_html=True)

# Botão Flutuante WhatsApp
st.markdown(f"""
    <a href="https://wa.me/556291760052" style="position:fixed;width:60px;height:60px;bottom:40px;right:40px;background-color:#25d366;color:#FFF;border-radius:50px;text-align:center;font-size:30px;box-shadow: 2px 2px 10px rgba(0,0,0,0.5);z-index:100;" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" style="width:100%; padding:10px; border:none;">
    </a>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="background: linear-gradient(90deg, #000000 0%, #1a1a1a 100%); padding: 25px; border-left: 10px solid #2563eb; border-radius: 10px; margin-bottom: 20px;">
    <h1 style="color: white; margin:0; letter-spacing: 2px;">🧼 CACHORRO LOUCO GYN</h1>
    <p style="color: #facc15; margin:0; font-weight: bold;">ESTÉTICA AUTOMOTIVA & RESIDENCIAL DE ALTO PADRÃO</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🏎️ AUTOMOTIVO (ELITE)", "🛋️ ESTOFADOS & CARPETES", "🗓️ AGENDAMENTO"])

with tab1:
    st.markdown("### 🏎️ O Padrão de Elite")
    c1, c2 = st.columns(2)
    with c1:
        # A FOTO TOP (Mão no capô preto / Tatuagem)
        st.image("https://images.unsplash.com/photo-1605414654535-43ea237691f1?q=80&w=1000", caption="Detalhamento Técnico de Alta Performance")
    with c2:
        # Foto Snow Foam / Espuma
        st.image("https://images.unsplash.com/photo-1607860108855-64acf2078ed9?q=80&w=1000", caption="Lavagem Técnica com Snow Foam")

with tab2:
    st.markdown("### 🛋️ Tratamento em Estofados e Carpetes de Veludo")
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        # Foto de Sofá de Veludo sendo limpo/aspirado
        st.image("https://images.unsplash.com/photo-1556912177-c54030639a67?q=80&w=1000", 
                 caption="Higienização de Sofás e Poltronas de Luxo")
        st.markdown("#### ✅ Sofás e Poltronas")
        st.write("Limpeza profunda em tecidos delicados como veludo, linho e camurça.")
    
    with col_e2:
        # Foto de Tapete de alto padrão (Veludo/Carpete)
        st.image("https://images.unsplash.com/photo-1600166898405-da9535204843?q=80&w=1000", 
                 caption="Renovação de Carpetes e Tapetes")
        st.markdown("#### ✅ Carpetes e Tapetes")
        st.write("Extração industrial que remove a sujeira da base do carpete, restaurando o toque macio.")

    st.divider()
    
    col_e3, col_e4 = st.columns(2)
    with col_e3:
        # Foto de Puffs ou cadeiras decorativas sendo higienizadas
        st.image("https://images.unsplash.com/photo-1586023492125-27b2c045efd7?q=80&w=1000", 
                 caption="Higienização de Puffs e Mobiliário")
    with col_e4:
        st.markdown("#### ✅ Especialista em Puffs e Veludos")
        st.info("""
        - **Tecnologia de Extração:** Removemos ácaros e manchas sem molhar a estrutura.
        - **Cuidado com Veludo:** Produtos específicos para manter o brilho do tecido.
        - **Puffs e Almofadas:** Higienização completa de itens de decoração.
        """)

with tab3:
    st.markdown("### 🗓️ Agendamento Via WhatsApp")
    servico = st.selectbox("Selecione o serviço:", 
                           ["Lavagem Técnica Automotiva", "Limpeza de Sofá (Veludo/Linho)", "Limpeza de Carpete/Tapete", "Higienização de Puffs/Poltronas"])
    
    data = st.date_input("Preferência de data:")
    
    if st.button("🚀 CHAMAR JOHNNY NO WHATSAPP"):
        msg = f"Fala Johnny! Gostaria de um orçamento para {servico} para o dia {data}."
        link = f"https://wa.me/556291760052?text={msg.replace(' ', '%20')}"
        st.markdown(f'<a href="{link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:15px; text-align:center; border-radius:10px; font-weight:bold;">ABRIR CONVERSA AGORA</div></a>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center><b>Cachorro Louco GYN © 2026 | Powered by Oráculo System</b></center>", unsafe_allow_html=True)
