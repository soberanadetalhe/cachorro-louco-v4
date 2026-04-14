import streamlit as st
import pandas as pd
import os
import datetime

# ======================================================
# PROTOCOLO SENTINELA - CAPTURA INVISÍVEL DE IP
# ======================================================
def registrar_acesso_sentinela():
    log_file = "log_acessos_operador.csv"
    try:
        # No Streamlit Cloud, o IP real vem nos headers
        headers = st.context.headers
        ip_v = headers.get("X-Forwarded-For", "127.0.0.1").split(',')[0]
        user_agent = headers.get("User-Agent", "Desconhecido")
        agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        df_novo = pd.DataFrame([{"Data": agora, "IP": ip_v, "Dispositivo": user_agent}])
        
        if not os.path.isfile(log_file):
            df_novo.to_csv(log_file, index=False)
        else:
            df_novo.to_csv(log_file, mode='a', header=False, index=False)
        return ip_v
    except:
        return "Erro na Captura"

# Executa o rastreio assim que o site abre
ip_alvo = registrar_acesso_sentinela()

# ======================================================
# INTERFACE CACHORRO LOUCO GYN - V5.5
# ======================================================

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
    img { border-radius: 12px; border: 1px solid #333; object-fit: cover; width: 100%; height: 350px; }
</style>
""", unsafe_allow_html=True)

# Botão Flutuante WhatsApp
st.markdown(f"""
    <a href="https://wa.me/556291760052" style="position:fixed;width:60px;height:60px;bottom:40px;right:40px;background-color:#25d366;color:#FFF;border-radius:50px;text-align:center;z-index:100;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" style="width:100%; padding:10px; border:none; height:auto;">
    </a>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="background: linear-gradient(90deg, #000000 0%, #1a1a1a 100%); padding: 25px; border-left: 10px solid #2563eb; border-radius: 10px; margin-bottom: 20px;">
    <h1 style="color: white; margin:0; letter-spacing: 2px;">🧼 CACHORRO LOUCO GYN</h1>
    <p style="color: #facc15; margin:0; font-weight: bold;">ESTÉTICA AUTOMOTIVA & RESIDENCIAL DE ALTO PADRÃO</p>
</div>
""", unsafe_allow_html=True)

# Radar de Operador (Só aparece para você se souber onde olhar)
if st.sidebar.checkbox("📡 MODO SENTINELA"):
    st.sidebar.write(f"**IP Detectado:** {ip_alvo}")
    if os.path.exists("log_acessos_operador.csv"):
        st.sidebar.download_button("Baixar Log de IPs", data=open("log_acessos_operador.csv", "rb"), file_name="acessos.csv")

tab1, tab2, tab3 = st.tabs(["🚗 AUTOMOTIVO (ELITE)", "🛋️ RESIDENCIAL (ESTOFADOS)", "🗓️ AGENDAMENTO"])

with tab1:
    st.markdown("### 🏎️ Lavagem Técnica e Detalhamento")
    c1, c2, c3= st.columns(3)
    with c1:
        st.image("https://i.ibb.co/mVW7V5N8/1775581320812.png", caption="Reflexo Profundo e Detalhamento Técnico")
    with c2:
        st.image("https://images.unsplash.com/photo-1607860108855-64acf2078ed9?q=80&w=1000", caption="Lavagem Técnica com Snow Foam")
    with c3:
        st.image("https://i.ibb.co/WNB5pNMx/1775581194742.png")

with tab2:
    st.markdown("### 🛋️ Especialista em Estofados de Veludo e Carpetes")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.image("https://i.ibb.co/ynKgCXMV/1775580081625.png", caption="Higienização de Poltronas e Cadeiras de Design")
        st.markdown("#### ✅ Puffs e Poltronas")
        st.write("Limpeza técnica em tecidos finos. Removemos manchas e ácaros preservando a maciez do veludo.")
    with col_e2:
        st.image("https://i.ibb.co/bgFx4B8v/1775580077842.png", caption="Higienização de Sofás e Puffs de Luxo")
        st.markdown("#### ✅ Sofás")
        st.write("Seu sofá renovado. Tecnologia de extração que elimina fungos, ácaros e sujeira incrustada.")

with tab3:
    st.markdown("### 🗓️ Reservar seu Horário Instantaneamente")
    with st.form("agendamento"):
        servico = st.selectbox("O que vamos transformar hoje?",
                               ["Lavagem Técnica", "Proteção de Acabamento", "Higienização de Sofá", "Limpeza de Tapetes"])
        data = st.date_input("Preferência de data:")
        obs = st.text_input("Alguma observação específica?")
        submit = st.form_submit_button("🚀 ENVIAR SOLICITAÇÃO VIA WHATSAPP")

        if submit:
            msg = f"Fala Johnny! Quero agendar: {servico} para o dia {data}. Obs: {obs}. Vi no site!"
            link = f"https://wa.me/556291760052?text={msg.replace(' ', '%20')}"
            st.write(f"Redirecionando para WhatsApp...")
            st.markdown(f'<meta http-equiv="refresh" content="0;URL={link}">', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center><b>Cachorro Louco GYN © 2026 | Powered by Oráculo System</b></center>", unsafe_allow_html=True)
