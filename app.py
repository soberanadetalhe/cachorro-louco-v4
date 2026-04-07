import streamlit as st
import base64 # Importante para imagens locais se necessário
from datetime import datetime

# --- CONFIGURAÇÃO DA VERSÃO ---
# Versão do Sistema: 2.0.0 (Menu e Cachorro Louco adicionados)
# Horário de Geração: 07/04/2026 - 16:16
# ------------------------------

def main():
    # 1. Configurações Iniciais da Página
    st.set_page_config(
        page_title="Casa Renovada - Limpeza e Higienização",
        page_icon="🏠",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # 2. SEUS LINKS DIRETOS DO IMGBB (Aqui está o segredo!)
    # Pegue o link que termina em .png ou .jpg
    url_banner_principal = "https://i.ibb.co/B5MR52nN/1775581320812.png"
    url_cachorro_louco   = "https://i.ibb.co/mVW7V5N8/1775581320812.png"
    
    # URL de exemplo para o carro (Substitua se tiver outra)
    url_carro_exemplo   = "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?q=80&w=600&auto=format&fit=crop"

    # 3. Criação do Menu Lateral (Sidebar)
    st.sidebar.image(url_banner_principal, use_container_width=True)
    st.sidebar.title("Navegação")
    
    # Opções do menu
    pagina_selecionada = st.sidebar.radio(
        "Selecione uma Seção:",
        ["Home", "Serviços Automotivos", "Galeria de Fotos", "Sobre Nós"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("📱 WhatsApp: (62) 9XXXX-XXXX")

    # 4. Lógica para Exibir Conteúdo Diferente Baseado na Navegação
    
    # --- SEÇÃO HOME (Início) ---
    if pagina_selecionada == "Home":
        # Exibe o Banner Principal no topo
        st.image(url_banner_principal, use_container_width=True, caption="Casa Renovada")
        
        # Títulos e Lista de Serviços
        st.header("🏠 Casa Renovada")
        st.subheader("Nada de sujeira no seu conforto.")

        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("""
            * **Higienização** de Sofás
            * **Limpeza** de Tapetes
            * **Tratamento** de Colchões
            * **Atendimento** Domiciliar
            """)
        
        with col2:
            st.markdown(" ") # Espaçamento
            st.markdown(" ") # Espaçamento
            st.success("✅ Equipamentos de Extração Profissional")

    # --- SEÇÃO AUTOMOTIVO (Mantendo o Carro) ---
    elif pagina_selecionada == "Serviços Automotivos":
        st.header("🚗 AUTOMOTIVO - Limpeza Especializada")
        
        col_img, col_txt = st.columns([1, 1])
        
        with col_img:
            # Exibe a imagem do carro (mantida)
            st.image(url_carro_exemplo, use_container_width=True, caption="Limpeza e Proteção Veicular")
        
        with col_txt:
            st.markdown("""
            **O que oferecemos para seu veículo:**
            * Higienização Completa de Bancos (Tecido ou Couro)
            * Limpeza Detalhada de Painéis e Portas
            * Remoção de Manchas e Odores
            * Tratamento com Ozonização
            
            _Revitalize o interior do seu carro!_
            """)
            st.button("Agendar Limpeza Automotiva")

    # --- SEÇÃO GALERIA (O Cachorro Louco) ---
    elif pagina_selecionada == "Galeria de Fotos":
        st.header("📸 Nossa Galeria de Resultados")
        
        # Estrutura de grid para fotos
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("O 'Cachorro Louco' da Limpeza")
            st.image(url_cachorro_louco, use_container_width=True, caption="Nosso mascote e padrão de qualidade!")
        
        with col2:
            st.subheader("Antes e Depois - Sofá")
            # Exemplo de como carregar outra imagem de teste se quisesse
            # st.image(url_outra_exemplo, use_container_width=True, caption="Resultados Reais")
            st.markdown("Adicione mais fotos aqui!")

    # --- SEÇÃO SOBRE NÓS ---
    elif pagina_selecionada == "Sobre Nós":
        st.header("🏢 Sobre a Casa Renovada")
        st.write("Somos especialistas em trazer vida nova ao seu ambiente, utilizando tecnologia profissional e atendimento personalizado.")
        st.write("Atuamos em Goiânia e região.")

    # 5. Rodapé fixo
    st.markdown("---")
    st.caption(f"© Casa Renovada | {datetime.now().strftime('%Y')} | Versão 2.0.0")

if __name__ == "__main__":
    main()
