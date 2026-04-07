import streamlit as st

# Versão 5.2 - Foco em Estofados & Tapetes | 07/04/2026 17:50
st.set_page_config(page_title="Cachorro Louco GYN", page_icon="🧼", layout="wide")

# CSS Industrial Dark Refinado
st.markdown("""
<style>
    .main { background-color: #050505; color: #e0e0e0; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background-color: #111; color: #facc15; 
        font-weight: bold; border-radius: 8px 8px 0 0; border: 1px solid #222;
    }
    .stTabs [aria-selected="true"] { background-color: #2563eb !important; color: white !important; }
    
    img { border-radius: 15px; border: 1px solid #333; transition: 0.3s; }
    img:hover { border-color: #2563eb; transform: scale(1.01); }

    .float-wa {
        position: fixed; width: 60px; height: 60px; bottom: 40px; right: 40px;
        background-color: #25d366; color: #FFF; border-radius: 50px; text-align: center;
        font-size: 30px; box-shadow: 2px 2px 10px rgba(0,0,0,0.5); z-index: 100;
    }
</style>
""", unsafe_allow_html=True)

# Botão Flutuante WhatsApp
st.markdown(f"""
    <a href="https://wa.me/556291760052" class="float-wa" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" style="width:100%; padding:10px; border:none;">
    </a>
""", unsafe_allow_html=True)

# Header Oráculo Style
st.markdown("""
<div style="background: linear-gradient(90deg, #000000 0%, #1a1a1a 100%); padding: 25px; border-left: 10px solid #2563eb; border-radius: 10px; margin-bottom: 20px;">
    <h1 style="color: white; margin:0; letter-spacing: 2px;">🧼 CACHORRO LOUCO GYN</h1>
    <h3 style="color: #facc15; margin:0;">ESTÉTICA AUTOMOTIVA E RESIDENCIAL DE ALTO PADRÃO</h3>
    <p style="color: #888;">Goiânia - GO | Tecnologia em Limpeza Técnica</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🏎️ AUTOMOTIVO (ELITE)", "🛋️ ESTOFADOS & TAPETES", "🗓️ AGENDAMENTO"])

with tab1:
    st.markdown("### 🏎️ Lavagem Técnica e Detalhamento")
    c1, c2 = st.columns(2)
    with c1:
        # Foto Capô Preto / Detalhamento (A foto que você curtiu!)
        st.image("https://images.unsplash.com/photo-1605414654535-43ea237691f1?q=80&w=1000", caption="Reflexo Profundo e Detalhamento de Elite")
        st.markdown("#### ✅ Detalhamento Interno")
        st.write("Higienização minuciosa de cada centímetro do interior, de painéis a plásticos.")
    with c2:
        # Foto Carro com Espuma (Snow Foam)
        st.image("https://images.unsplash.com/photo-1607860108855-64acf2078ed9?q=80&w=1000", caption="Snow Foam - Remoção de Sujeira Técnica")
        st.markdown("#### ✅ Lavagem Técnica Externa")
        st.write("Técnicas avançadas que removem a sujeira sem agredir o verniz do seu veículo.")
    st.divider()
    st.markdown("<center><b>Padrão de entrega elevado: utilizamos apenas produtos de pH neutro e proteção UV.</b></center>", unsafe_allow_html=True)

with tab2:
    st.markdown("### 🛋️ Higienização Residencial Profunda")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        # Foto Extratora trabalhando no sofá (Lavagem Profunda)
        st.image("https://images.unsplash.com/photo-1550581190-9c1c48d21d6c?q=80&w=1000", 
                 caption="Extração de Sujeira Profunda em Sofás")
        st.markdown("#### ✅ Sofás e Poltronas")
        st.write("Seu sofá renovado. Tecnologia de extração que elimina fungos, ácaros e sujeira incrustada.")
    
    with col_e2:
        # Foto de Tapete sendo lavado (Tratamento Especializado)
        st.image("https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=1000", 
                 caption="Tratamento Técnico em Tapetes e Carpetes")
        st.markdown("#### ✅ Tapetes e Carpetes")
        st.write("Lavagem técnica industrial que remove a sujeira profunda e odores sem danificar as fibras.")

    st.divider()
    
    col_e3, col_e4 = st.columns(2)
    with col_e3:
        # Foto de Poltrona ou Cadeira sendo limpa
        st.image("https://images.unsplash.com/photo-1519947486511-46149fa0a254?q=80&w=1000", 
                 caption="Higienização de Poltronas e Cadeiras")
        st.markdown("#### Cadeiras e Poltronas")
        st.write("Limpeza técnica para renovar as poltronas e cadeiras da sua casa ou escritório.")
    with col_e4:
        st.markdown("#### ✅ Por que escolher o Cachorro Louco?")
        st.info("""
        - **Equipamentos Profissionais:** Extratoras de alta sucção.
        - **Atendimento Domiciliar:** Conforto total para você em Goiânia.
        - **Secagem Rápida:** Técnica que evita mofo e mau cheiro.
        - **Foco em Saúde:** Eliminação de 99% dos ácaros e bactérias.
        """)

with tab3:
    st.markdown("### 🗓️ Reserve seu Horário Instantaneamente")
    with st.form("agendamento"):
        servico = st.selectbox("O que vamos transformar hoje?", 
                               ["Lavagem Técnica (Carro Luxo)", "Polimento e Proteção", "Higienização de Sofá", "Limpeza de Tapetes", "Combo Carro + Casa"])
        
        data = st.date_input("Para quando você precisa?")
        
        obs = st.text_input("Alguma observação específica?")
        
        st.write("---")
        submit = st.form_submit_button("🚀 ENVIAR SOLICITAÇÃO VIA WHATSAPP")
        
        if submit:
            msg = f"Fala Johnny! Quero agendar: {servico} para o dia {data}. Obs: {obs}. Vi no site!"
            link = f"https://wa.me/556291760052?text={msg.replace(' ', '%20')}"
            st.markdown(f'''
                <a href="{link}" target="_blank" style="text-decoration:none;">
                    <button style="width:100%; height:50px; background-color:#25d366; color:white; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">
                        ABRIR CONVERSA NO WHATSAPP
                    </button>
                </a>
            ''', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center><b>Powered by Oráculo System | GYN Pro Mundo © 2026</b></center>", unsafe_allow_html=True)
