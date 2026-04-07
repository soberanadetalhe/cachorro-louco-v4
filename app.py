import streamlit as st
from datetime import datetime

# ==========================================================
# SISTEMA: CASA RENOVADA (ORÁCULO ECOSYSTEM)
# VERSÃO: 2.1.0 | LOCAL: GYN | DATA: 07/04/2026 - 16:20
# STATUS: PRONTO PARA DEPLOY (GITHUB)
# ==========================================================

def main():
    # Configurações de Layout
    st.set_page_config(
        page_title="Casa Renovada - Estofados & Automotivo",
        page_icon="🏠",
        layout="wide"
    )

    # --- BANCO DE LINKS DIRETOS (IMG BB) ---
    URL_BANNER_HOME = "https://i.ibb.co/B5MR52nN/1775581320812.png"
    URL_CACHORRO_LOUCO = "https://i.ibb.co/mVW7V5N8/1775581320812.png"
    URL_CARRO = "https://i.ibb.co/6R0pT9L0/1775581320812.jpg" # Ajuste conforme seu link de carro

    # --- MENU LATERAL ---
    st.sidebar.image(URL_CACHORRO_LOUCO, caption="Padrão Cachorro Louco 🛠️")
    st.sidebar.title("MENU DE COMANDO")
    
    aba = st.sidebar.radio(
        "Navegação:",
        ["🏠 Início", "🚗 Automotivo", "📸 Galeria", "📲 Contato"]
    )

    # --- LÓGICA DAS ABAS ---

    if aba == "🏠 Início":
        st.image(URL_BANNER_HOME, use_container_width=True)
        st.title("Casa Renovada")
        st.subheader("Higienização de Estofados e Tapetes em Goiânia")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### Serviços Domiciliares:
            * ✅ **Sofás e Poltronas**
            * ✅ **Tapetes e Carpetes**
            * ✅ **Colchões (Tratamento Anti-ácaro)**
            * ✅ **Cadeiras de Jantar**
            """)
        with col2:
            st.info("Utilizamos extratoras profissionais de alta sucção.")

    elif aba == "🚗 Automotivo":
        st.header("Estética Automotiva Profissional")
        st.image(URL_CARRO, width=500)
        st.markdown("""
        ### Limpeza Veicular Detalhada:
        * Higienização de bancos (couro e tecido).
        * Limpeza de teto e carpetes.
        * Hidratação de plásticos internos.
        """)
        st.button("Solicitar Orçamento Automotivo")

    elif aba == "📸 Galeria":
        st.header("Galeria de Resultados")
        cols = st.columns(2)
        cols[0].image(URL_BANNER_HOME, caption="Antes/Depois 01")
        cols[1].image(URL_CACHORRO_LOUCO, caption="Equipe em Ação")

    elif aba == "📲 Contato":
        st.header("Fale com o Oráculo")
        st.write("Agende sua visita técnica pelo WhatsApp.")
        st.success("📱 (62) 9XXXX-XXXX")

    # Rodapé Técnico
    st.markdown("---")
    st.caption(f"Operador: Johnny | GYN Pro Mundo | {datetime.now().strftime('%d/%m/%Y %H:%M')}")

if __name__ == "__main__":
    main()
