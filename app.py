import streamlit as st

# Versão 5.5 - Premium Home Correction | 07/04/2026 17:50
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
    <a href="https://wa.me/556291760052" style="position:fixed;width:60px;height:60px;bottom:40px;right:40px;background-color:#25d366;color:#FFF;border-r>
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" style="width:100%; padding:10px; border:none; height:auto;">
    </a>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="background: linear-gradient(90deg, #000000 0%, #1a1a1a 100%); padding: 25px; border-left: 10px solid #2563eb; border-radius: 10px; margin-bot>
    <h1 style="color: white; margin:0; letter-spacing: 2px;">🧼 CACHORRO LOUCO GYN</h1>
    <p style="color: #facc15; margin:0; font-weight: bold;">ESTÉTICA AUTOMOTIVA & RESIDENCIAL DE ALTO PADRÃO</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚗 AUTOMOTIVO (ELITE)", "🛋️ RESIDENCIAL (ESTOFADOS)", "🗓️ AGENDAMENTO"])

with tab1:
    st.markdown("### 🏎️ Lavagem Técnica e Detalhamento")
    c1, c2, c3= st.columns(3)
    with c1:
        # A FOTO TOP (Mão no capô preto / Tatuagem) - Mantida conforme solicitado
        st.image("https://i.ibb.co/mVW7V5N8/1775581320812.png", caption="Reflexo Profundo e Detalhamento Técnico")
    with c2:
        # Foto Snow Foam / Espuma
        st.image("https://images.unsplash.com/photo-1607860108855-64acf2078ed9?q=80&w=1000", caption="Lavagem Técnica com Snow Foam")
    with c3:
        st.image("https://i.ibb.co/WNB5pNMx/1775581194742.png")
with tab2:
    st.markdown("### 🛋️ Especialista em Estofados de Veludo e Carpetes")

    col_e1, col_e2 = st.columns(2)
    with col_e1:
        # Foto de Poltrona de Veludo de alto padrão em sala de luxo (Para substituir a quebra)
        st.image("https://i.ibb.co/ynKgCXMV/1775580081625.png",
                 caption="Higienização de Poltronas e Cadeiras de Design")
        st.markdown("#### ✅ Puffs e Poltronas")
        st.write("Limpeza técnica em tecidos finos. Removemos manchas e ácaros preservando a maciez do veludo.")

    with col_e2:
        # Foto de Sofá de Veludo de alto padrão em sala de luxo (Correção da cadeira de madeira)
        st.image("https://i.ibb.co/bgFx4B8v/1775580077842.png",
                 caption="Higienização de Sofás e Puffs de Luxo")
        st.markdown("#### ✅ Sofás")
        st.write("Seu sofá renovado. Tecnologia de extração que elimina fungos, ácaros e sujeira incrustada.")

    st.divider()

    col_e3, col_e4 = st.columns(2)
    with col_e3:
        # Foto: Close em carpete de veludo/sala decorada (Para complementar)
        st.image("https://i.ibb.co/N6rcq709/1775580086384.png",
                 caption="Extração Profunda em Carpetes e Tapetes")
    with col_e4:
        st.markdown("#### ✅ Por que escolher o Cachorro Louco?")
        st.info("""
        - **Equipamentos Profissionais:** Extratoras de alta sucção.
        - **Atendimento Domiciliar:** Conforto total para você em Goiânia.
        - **Secagem Rápida:** Técnica que evita mofo e mau cheiro.
        - **Foco em Saúde:** Eliminação de 99% dos ácaros e bactérias.
        """)

with tab3:
    st.markdown("### 🗓️ Reservar seu Horário Instantaneamente")
    with st.form("agendamento"):
        servico = st.selectbox("O que vamos transformar hoje?",)
                               ["Lavagem  (Carro)", " Proteção no acabamento", "Higienização de Sofá (Veludo)", "Limpeza de Tapetes/Carpetes", "Combo car>

        data = st.date_input("Preferência de data:")

        obs = st.text_input("Alguma observação específica?")

        st.write("---")
        submit = st.form_submit_button("🚀 ENVIAR SOLICITAÇÃO VIA WHATSAPP")

        if submit:
            msg = f"Fala Johnny! Quero agendar: {servico} para o dia {data}. Obs: {obs}. Vi no site do Cachorro Louco!"
            link = f"https://wa.me/556291760052?text={msg.replace(' ', '%20')}"
            st.markdown(f'''
                <a href="{link}" target="_blank" style="text-decoration:none;">
                    <button style="width:100%; height:50px; background-color:#25d366; color:white; border:none; border-radius:5px; font-weight:bold; curs>
                        ABRIR CONVERSA NO WHATSAPP
                    </button>
                </a>
            ''', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center><b>Cachorro Louco GYN © 2026 | Powered by Oráculo System</b></center>", unsafe_allow_html=True)
