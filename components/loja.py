# components/loja.py

"""
Tela de loja do Delta.

Responsável por:
- listar recompensas disponíveis;
- verificar saldo do aluno;
- permitir resgate de recompensas;
- atualizar saldo de Deltas.
"""

import streamlit as st

from data.recompensas import (
    listar_recompensas_ativas,
    resgatar_recompensa,
)


def exibir_loja():
    """
    Exibe a loja de recompensas do Delta.
    """

    st.title("Loja de Recompensas")
    st.write(
        "Troque seus Deltas por benefícios simbólicos, acadêmicos ou institucionais."
    )

    st.metric("Seu saldo", f"{st.session_state.deltas} Deltas")

    st.divider()

    recompensas = listar_recompensas_ativas()

    if not recompensas:
        st.warning("Nenhuma recompensa disponível no momento.")
        return

    for recompensa in recompensas:
        with st.container(border=True):
            st.markdown(f"### {recompensa['nome']}")

            col1, col2 = st.columns([3, 1])

            with col1:
                st.write(recompensa["descricao"])
                st.caption(f"Tipo: {recompensa['tipo']}")
                st.caption(f"Parceiro: {recompensa['parceiro']}")

                if recompensa["depende_validacao"]:
                    st.warning("Esta recompensa depende de validação institucional.")

            with col2:
                st.metric("Custo", f"{recompensa['custo_deltas']} Deltas")

                pode_resgatar = st.session_state.deltas >= recompensa["custo_deltas"]

                if st.button(
                    "Resgatar",
                    key=f"resgatar_{recompensa['id']}",
                    disabled=not pode_resgatar
                ):
                    resultado = resgatar_recompensa(
                        recompensa["id"],
                        st.session_state.deltas
                    )

                    if resultado["sucesso"]:
                        st.session_state.deltas = resultado["novo_saldo"]
                        st.success(resultado["mensagem"])
                        st.rerun()
                    else:
                        st.error(resultado["mensagem"])

                if not pode_resgatar:
                    faltam = recompensa["custo_deltas"] - st.session_state.deltas
                    st.caption(f"Faltam {faltam} Deltas.")