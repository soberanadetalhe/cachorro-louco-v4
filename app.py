import streamlit as st

# Versão 5.6 - Full Integration | 07/04/2026 19:55
st.set_page_config(page_title="Cachorro Louco GYN", page_icon="🧼", layout="wide")

# CSS Industrial Dark Refinado - Corrigido e sem cortes
st.markdown("""
<style>
    .main { background-color: #050505; color: #e0e0e0; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background-color: #111; color: #facc15;
        font-weight: bold; border-radius: 8px 8px 0 0; border: 1px solid #222;
    }
    .stTabs [aria-selected="true"] { background-color: #2563eb !important; color: white !important; }

    img { border-radius: 12px; border: 1px solid #333; object-fit: cover; width: 100%; height: 350px; }
    
    /* Botão flutuante WhatsApp */
    .float-wa {
        position:fixed; width:60px; height:60px; bottom:40px; right:40px; 
        background-color:#25d366; color:#FFF; border-radius:50px; 
        text-align:center; box-shadow: 2px 2px 3px #999; z-index:1000;
    }
</style>
""", unsafe_allow_html=True)

# Botão Flutuante WhatsApp
st.markdown("""
    <a href="https://wa.me/556291760052" class="float-wa" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" style="width:100%; padding:10px; border:none; height:auto;">
    </a>
""", unsafe_allow_html=True)

# Header com degradê corrigido
st.markdown("""
<div style="background: linear-gradient(90deg, #000000 0%, #1a1a1a 100%); padding: 25px; border-left: 10px solid #2563eb; border-radius: 10px; margin-bottom: 25px;">
    <h1 style="color: white; margin:0; letter-spacing: 2px;">🧼 CACHORRO LOUCO GYN</h1>
    <p style="color: #facc15; margin:0; font-weight: bold;">ESTÉTICA AUTOMOTIVA & RESIDENCIAL DE ALTO PADRÃO</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚗 AUTOMOTIVO (ELITE)", "🛋️ RESIDENCIAL (ESTOFADOS)", "🗓️ AGENDAMENTO"])

# --- ABA 1: AUTOMOTIVO ---
with tab1:
    st.markdown("### 🏎️ Lavagem Técnica e Detalhamento")
    c1, c2, c3 = st.columns(3) # Corrigido: adicionada a vírgula
    
    with c1:
        st.image("https://i.ibb.co/mVW7V5N8/1775581320812.png", caption="Reflexo Profundo e Detalhamento Técnico")
    with c2:
        st.image("https://images.unsplash.com/photo-1607860108855-64acf2078ed9?q=80&w=1000", caption="Lavagem Técnica com Snow Foam")
    with c3:
        # Foto solicitada: Mão no capô preto / Tatuagem
        st.image("https://i.ibb.co/WNB5pNMx/1775581194742.png", caption="Trabalho de Precisão")

# --- ABA 2: RESIDENCIAL ---
with tab2:
    st.markdown("### 🛋️ Especialista em Estofados de Veludo e Carpetes")

    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.image("https://i.ibb.co/dsv4BQH7/1775603861601.png", caption="Higienização de Poltronas")
        st.markdown("#### ✅ Puffs e Poltronas")
        st.write("Limpeza técnica em tecidos finos. Removemos manchas e ácaros.")

    with col_e2:
        st.image("https://i.ibb.co/bgFx4B8v/1775580077842.png", caption="Higienização de Sofás de Luxo")
        st.markdown("#### ✅ Sofás")
        st.write("Seu sofá renovado com tecnologia de extração profunda.")

    st.divider()

    col_e3, col_e4 = st.columns(2)
    with col_e3:
        st.image("https://i.ibb.co/1t6ZpSx4/1775603874804.png", caption="Extração em Carpetes e Tapetes")
    with col_e4:
        st.markdown("#### ✅ Por que escolher o Cachorro Louco?")
        st.info("""
        - **Equipamentos Profissionais:** Extratoras de alta sucção.
        - **Atendimento Domiciliar:** Conforto total em Goiânia.
        - **Secagem Rápida:** Técnica que evita mofo.
        - **Saúde:** Eliminação de 99% dos ácaros e bactérias.
        """)

# --- ABA 3: AGENDAMENTO ---
with tab3:
    st.markdown("### 🗓️ Reservar seu Horário Instantaneamente")
    with st.form("agendamento"):
        servico = st.selectbox("O que vamos transformar hoje?",
                               ["Lavagem (Carro)", "Proteção no acabamento", "Higienização de Sofá (Veludo)", "Limpeza de Tapetes/Carpetes", "Combo Completo"])

        data = st.date_input("Preferência de data:")
        obs = st.text_input("Alguma observação específica?")

        submit = st.form_submit_button("🚀 ENVIAR SOLICITAÇÃO VIA WHATSAPP")

        if submit:
            msg = f"Fala Johnny! Quero agendar: {servico} para o dia {data}. Obs: {obs}. Vi no site do Cachorro Louco!"
            link = f"https://wa.me/556291760052?text={msg.replace(' ', '%20')}"
            st.markdown(f'''
                <a href="{link}" target="_blank" style="text-decoration:none;">
                    <div style="width:100%; height:50px; background-color:#25d366; color:white; border-radius:5px; font-weight:bold; display:flex; align-items:center; justify-content:center;">
                        ABRIR CONVERSA NO WHATSAPP
                    </div>
                </a>
            ''', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center><b>Cachorro Louco GYN © 2026 | Powered by Oráculo System</b></center>", unsafe_allow_html=True)
