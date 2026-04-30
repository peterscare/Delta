import streamlit as st
from src.models.usuario import Usuario
from src.data.cursos import obter_nomes_cursos

# Configuração da página - Identidade Visual Delta
st.set_page_config(page_title="Projeto Delta - UFRJ", page_icon="Δ", layout="wide")

def main():
    # Estilização básica (O Front-end vai melhorar isso em src/styles/)
    st.title("Δ Projeto Delta")
    st.subheader("Transformando atenção em desempenho acadêmico na UFRJ")

    # Lógica de Sessão (Login Simulado para o MVP)
    if 'usuario' not in st.session_state:
        st.info("Bem-vindo ao Delta! Vamos começar configurando seu perfil acadêmico.[cite: 1]")
        
        with st.form("cadastro_inicial"):
            nome = st.text_input("Como podemos te chamar?")
            # Usa a lista de cursos que você criou em src/data/cursos.py[cite: 1]
            curso = st.selectbox("Selecione seu curso na UFRJ:", obter_nomes_cursos())
            
            botao_confirmar = st.form_submit_button("Entrar no Delta")
            
            if botao_confirmar and nome:
                # Instancia o seu Model de Usuário[cite: 1]
                novo_usuario = Usuario(nome=nome, curso=curso)
                st.session_state.usuario = novo_usuario
                st.rerun()
    else:
        # Interface Principal após o Login
        user = st.session_state.usuario
        st.sidebar.success(f"Logado como: {user.nome}")
        st.sidebar.write(f"🎓 Curso: {user.curso}")
        st.sidebar.metric("Seu Saldo", f"{user.deltas} Deltas") # Sistema de moedas[cite: 1]
        
        # Menu de Navegação (Conecta com o que o Front-end vai criar)
        menu = st.sidebar.radio("Navegar", ["Home", "Learn Reels", "Exercícios", "Loja de Recompensas", "Missões"])

        if menu == "Home":
            st.write(f"### Olá, {user.nome}! Pronto para os desafios de Cálculo I de hoje?")
            st.write("O Delta preparou trilhas personalizadas para o curso de " + user.curso + ".[cite: 1]")
            
            # Espaço para os cards de resumo (Progresso)
            col1, col2 = st.columns(2)
            with col1:
                st.info("**Sua Ofensiva:** 1 dia seguidos! 🔥")
            with col2:
                st.success("**Próxima Meta:** O mestre do Limite (Missão)")

        # As outras páginas serão importadas de src/pages/ pelo time de Front-end[cite: 1]

if __name__ == "__main__":
    main()