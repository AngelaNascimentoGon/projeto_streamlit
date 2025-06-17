import streamlit as st


st.set_page_config(page_title="projeto stremlit", layout="wide")
st.markdown("# Testando o Sreamlit")

def main():
    abas = st.tabs([
        "Clientes",
        "Cadastrar Cliente",
        "Editar",
        "Deletar"
    ])

    with abas[0]:
        st.title("Clientes")

    with abas[1]:
        st.title("Cadastrar clientes")

        with st.form(key='add_cliente', clear_on_submit=True):
            nome = st.text_input("nome", placeholder="nome")
            email = st.text_input("email", placeholder="email")
            idade = st.number_input("idade", placeholder="idade")
            telefone = st.number_input("telefone", placeholder="telefone")
            filmes = st.selectbox("selecione o filme", optins=[
            "Imagine me & you", "My first summer", "But i'm a Cheerleader", "Am i ok?"
            ])

 
    with abas[2]:
        st.title("Editar")
    
    with abas[3]:
        st.title("Deletar")


main()