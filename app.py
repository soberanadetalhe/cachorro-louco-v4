import streamlit as st

# Versão 5.0 - Edição Elite GYN | 07/04/2026
st.set_page_config(page_title="Cachorro Louco GYN", page_icon="🧼", layout="wide")

# Interface Industrial Dark Refinada
st.markdown("""
<style>
    .main { background-color: #050505; color: #e0e0e0; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background-color: #111; color: #facc15; 
        font-weight: bold; border-radius: 8px 8px 0 0; border: 1px solid #222;
    }
    .stTabs [aria-selected="true"] { background-color: #2563eb !important; color: white !important; }
    
    /* Estilo para imagens e cards */
    .img-card { border: 2px solid #222; border-radius: 15px; transition: 0.3s; }
    .img-card:hover { border-color: #2563eb; }

    /* Botão Flutuante WhatsApp */
    .float-wa {
        position: fixed; width: 60px; height: 60px; bottom: 40px; right: 40px;
        background-color: #25d366; color: #FFF; border-radius: 50px; text-align: center;
        font-size: 30px; box-shadow: 2px 2px 3px #999; z-index: 100;
    }
</style>
""", unsafe_allow_html=True)

# Botão Flutuante do WhatsApp
st.markdown(f"""
    <a href="https://wa.me/556291760052" class="float-wa" target="_blank">
        <i style="margin-top:16px;" class="fa fa-whatsapp"></i>
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" style="width:100%; padding:10px;">
    </a>
""", unsafe_allow_html=True)

# Banner Principal
st.markdown("""
<div style="background: linear-gradient(90deg, #000000 0%, #1a1a1a 100%); padding: 30px; border-left: 10px solid #2563eb; border-radius: 10px; margin-bottom: 25px;">
    <h1 style="color: white; margin:0; letter-spacing: 2px;">🧼 CACHORRO LOUCO GYN</h1>
    <h3 style="color: #facc15; margin:0;">ESTÉTICA AUTOMOTIVA E RESIDENCIAL DE ALTO PADRÃO</h3>
    <p style="color: #888;">Goiânia - GO | Tecnologia em Limpeza Técnica</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🏎️ AUTOMOTIVO (ELITE)", "🛋️ ESTOFADOS & CARPETES", "🗓️ AGENDAMENTO"])

with tab1:
    st.markdown("## ⚡ Lavagem Técnica & Detalhada")
    c1, c2 = st.columns(2)
    with c1:
        # Imagem do capô preto com reflexo (aquela que você curtiu)
        st.image("https://images.unsplash.com/photo-1552933157-42744b9e4e21?q=80&w=1000", caption="Reflexo e Proteção de Pintura")
        st.markdown("### O Brilho que seu carro merece")
        st.write("Tratamento especializado em veículos de luxo. Lavagem técnica que preserva o verniz e destaca cada detalhe.")
    with c2:
        # Carro com muita espuma (Snow Foam)
        st.image("https://images.unsplash.com/photo-1607860108855-64acf2078ed9?q=80&w=1000", caption="Snow Foam - Limpeza Profunda")
        st.markdown("### Tecnologia em Espuma")
        st.write("Utilizamos produtos de pH neutro e técnicas de Snow Foam para remover a sujeira sem agredir a superfície.")

    st.divider()
    # Foto do detalhamento técnico (mão na máquina/detalhes)
    c3, c4 = st.columns(2)
    with c3:
        st.image("https://images.unsplash.com/photo-1605414654535-43ea237691f1?q=80&w=1000", caption="Detalhamento Interno e Motor")
    with c4:
        st.markdown("### Detalhamento Interno")
        st.write("- Higienização de Couro e Tecidos\n- Limpeza Detalhada de Painel e Plásticos\n- Proteção UV de Longa Duração\n- Lavagem Técnica de Motor")

with tab2:
    st.markdown("## 🏠 Conforto e Higiene Residencial")
    col_a, col_b = st.columns(2)
    with col_a:
        # Foto de Tapete sendo lavado
        st.image("https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=1000", caption="Lavagem Industrial de Tapetes")
        st.markdown("### Tapetes e Carpetes")
        st.write("Sistema de extração profunda que remove manchas, odores e 99% dos ácaros e bactérias.")
    with col_b:
        # Foto de Estofado/Poltrona sendo limpo
        st.image("https://images.unsplash.com/photo-1550581190-9c1c48d21d6c?q=80&w=1000", caption="Revitalização de Estofados")
        st.markdown("### Sofás e Poltronas")
        st.write("Seu sofá novo de novo. Atendimento domiciliar com equipamentos de alta sucção e secagem rápida.")

with tab3:
    st.markdown("## 🗓️ Agendamento de Serviço")
    st.info("Selecione o serviço abaixo para iniciar o atendimento via WhatsApp.")
    
    with st.container():
        servico = st.selectbox("O que vamos transformar hoje?", 
                               ["Lavagem Técnica (Carro Luxo)", "Polimento e Proteção", "Higienização de Sofá", "Limpeza de Tapetes", "Combo Total"])
        
        data_pref = st.date_input("Preferência de data:")
        
        if st.button("🚀 CONFIRMAR AGENDAMENTO"):
            msg = f"Fala Johnny! Gostaria de agendar: {servico} para o dia {data_pref}. Vi no site!"
            link_wa = f"https://wa.me/556291760052?text={msg.replace(' ', '%20')}"
            st.markdown(f'<a href="{link_wa}" target="_blank" style="text-decoration:none;"><div style="background-color:#25d366; color:white; padding:15px; text-align:center; border-radius:10px; font-weight:bold;">ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center><b>Powered by Oráculo System | GYN Pro Mundo © 2026</b></center>", unsafe_allow_html=True)
