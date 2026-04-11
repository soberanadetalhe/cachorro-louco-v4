import streamlit as st
from datetime import datetime

# --- CONFIGURAÇÕES DE IDENTIDADE ---
APP_VERSION = "6.0.0 - Mobile Detail Focus"
CURRENT_TIME = datetime.now().strftime("%d/%m/%Y %H:%M")
LOGO_URL = "https://i.ibb.co/mVW7V5N8/1775581320812.png" # Sua foto do GTR
FOTO_TRABALHO = "https://i.ibb.co/WNB5pNMx/1775581194742.png" # Sua foto da mão no capô

st.set_page_config(
    page_title="Cachorro Louco GYN", 
    page_icon=LOGO_URL, 
    layout="wide"
)

# --- ESTILO INDUSTRIAL DARK ---
st.markdown(f"""
<style>
    .main {{ background-color: #0a0a0a; color: #f0f0f0; }}
    .stTabs [data-baseweb="tab-list"] {{ gap: 8px; }}
    .stTabs [data-baseweb="tab"] {{
        height: 50px; background-color: #111; color: #facc15;
        font-weight: bold; border-radius: 5px; border: 1px solid #333;
    }}
    .stTabs [aria-selected="true"] {{ background-color: #2563eb !important; color: white !important; }}
    
    .card-servico {{
        background: #151515; padding: 20px; border-radius: 15px;
        border-top: 5px solid #2563eb; margin-bottom: 20px;
    }}
    
    img {{ border-radius: 10px; border: 1px solid #222; }}
    
    .version-tag {{ color: #444; font-size: 0.7rem; text-align: right; font-family: monospace; }}
</style>
""", unsafe_allow_html=True)

st.markdown(f'<div class="version-tag">v{APP_VERSION} | {CURRENT_TIME}</div>', unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div style="background: linear-gradient(90deg, #000 0%, #111 100%); padding: 30px; border-left: 10px solid #2563eb; border-radius: 10px;">
    <h1 style="color: white; margin:0;">🧼 CACHORRO LOUCO GYN</h1>
    <p style="color: #facc15; margin:0; font-weight: bold; letter-spacing: 1px;">DETALHAMENTO AUTOMOTIVO MOBILE • GOIÂNIA</p>
</div>
""", unsafe_allow_html=True)

# --- SEÇÃO PRINCIPAL ---
st.write("")
col_main1, col_main2 = st.columns([1.2, 1])

with col_main1:
    st.image(LOGO_URL, use_container_width=True, caption="Qualidade Cachorro Louco GYN")
    st.markdown("### 🛠️ Lavagem de Verdade, Onde Você Estiver")
    st.write("""
    Não fazemos apenas uma lavagem, entregamos renovação. 
    Especialistas em limpeza técnica sem o uso de máquinas de polimento pesadas, 
    focando na integridade da pintura e no brilho instantâneo com ceras premium.
    """)

with col_main2:
    st.image(FOTO_TRABALHO, use_container_width=True, caption="Cuidado em cada detalhe")
    st.info("📍 Atendimento no Setor São José e Região.")

st.divider()

# --- OS 3 NÍVEIS DE LAVAGEM ---
st.markdown("## 📊 Nossos Níveis de Limpeza")
t1, t2, t3, t4 = st.tabs(["LÍVEL 1 (ESSENCIAL)", "NÍVEL 2 (INTERMEDIÁRIO)", "NÍVEL 3 (COMPLETO)", "🧼 TAPETES"])

with t1:
    st.markdown("""
    <div class="card-servico">
        <h3>🚗 Nível 1 - Essencial</h3>
        <ul>
            <li>Lavagem externa detalhada</li>
            <li>Limpeza de caixas de roda</li>
            <li>Pretinho nos pneus (Acabamento Dry)</li>
            <li><b>Acabamento:</b> Aplicação de cera líquida rápida</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1520340356584-f9917d1eea6f?q=80&w=1000", caption="Foco em brilho externo")

with t2:
    st.markdown("""
    <div class="card-servico">
        <h3>💎 Nível 2 - Intermediário</h3>
        <ul>
            <li>Tudo do Nível 1 +</li>
            <li>Aspiração interna completa</li>
            <li>Revitalização de plásticos (Proteção UV)</li>
            <li>Limpeza de painel e guarnições</li>
            <li><b>Acabamento:</b> Cera líquida de alta fixação</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1607860108855-64acf2078ed9?q=80&w=1000", caption="Cuidado interno e externo")

with t3:
    st.markdown("""
    <div class="card-servico">
        <h3>👑 Nível 3 - Master Detalhe</h3>
        <ul>
            <li>Tudo do Nível 2 +</li>
            <li>Lavagem técnica de motor (Segura)</li>
            <li>Limpeza profunda dos bancos</li>
            <li>Higienização de carpetes</li>
            <li>Condicionamento de borrachas</li>
            <li><b>Acabamento:</b> Proteção total com cera premium</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1552930294-6b595f4c2974?q=80&w=1000", caption="O tratamento completo para quem é exigente")

with t4:
    st.markdown("""
    <div class="card-servico">
        <h3>🧹 Lavagem de Tapetes</h3>
        <p>Traga seu tapete residencial ou automotivo! Lavagem com extratora e secagem controlada.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=1000", caption="Limpeza profunda de fibras")

# --- GALERIA DE RUA (FOTOS ALEATÓRIAS DE APOIO) ---
st.divider()
st.markdown("### 📸 Nosso Dia a Dia na Calçada")
g1, g2, g3 = st.columns(3)
with g1:
    st.image("https://images.pexels.com/photos/3354648/pexels-photo-3354648.jpeg?auto=compress&cs=tinysrgb&w=1000", caption="Espuma ativa")
with g2:
    st.image("https://images.pexels.com/photos/3728122/pexels-photo-3728122.jpeg?auto=compress&cs=tinysrgb&w=1000", caption="Limpeza de rodas")
with g3:
    st.image("https://images.pexels.com/photos/1144410/pexels-photo-1144410.jpeg?auto=compress&cs=tinysrgb&w=1000", caption="Detalhes internos")

# --- AGENDAMENTO WHATSAPP ---
st.write("")
if st.button("🚀 AGENDAR MINHA LAVAGEM AGORA", use_container_width=True):
    msg = "Olá Johnny! Vi o site e quero agendar uma lavagem técnica no meu carro."
    link = f"https://wa.me/556291760052?text={msg.replace(' ', '%20')}"
    st.markdown(f'<meta http-equiv="refresh" content="0;URL={link}">', unsafe_allow_html=True)

st.markdown("<br><center><b>Cachorro Louco GYN © 2026 | Powered by Oráculo System</b></center>", unsafe_allow_html=True)
