import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime


st.title("Hello, Streamlit!", anchor="inicio")
#âncora

st.subheader("Primeiro projeto com Streamlit")
st.write("Digite no terminal `streamlit run app.py`")
st.markdown("**AUTOR:** RAFAEL PROENÇA")
st.markdown("[Como usar markdown?](https://www.markdownguide.org/basic-syntax/)")
st.markdown("[API Reference](https://docs.streamlit.io/develop/api-reference)")

st.subheader("Exibição de dados com Pandas", anchor="pandas")
data = {
    "Nome": ["Rafael", "João", "Maria"],
    "Idade": [20, 30, 40],
    "Sexo": ["M", "M", "F"]}
df = pd.DataFrame(data)
st.dataframe(df)
st.table(df)

fig, ax = plt.subplots()
ax.bar(df["Nome"], df["Idade"], color=["blue", "green", "red"])
st.pyplot(fig)


if st.button(f"Clicar"):
   st.write("Você clicou no botão!")

numero = st.slider("Selecione um número", 0, 100, 50)
st.write(f"O número selecionado foi: {numero}")


st.selectbox("Selecione uma opção", ["Opção 1", "Opção 2", "Opção 3"])
st.multiselect("Selecione várias opções", ["Opção A", "Opção B", "Opção C"])

st.subheader("Banco de dados (csv)")

df_func = pd.read_csv("/bd/funcionarios.csv")
df_func['birthdate'] = pd.to_datetime(df_func['birthdate'])
st.write(df_func.dtypes)
st.dataframe(df_func)
birthdate_min = st.slider ("Selecione a data de nascimento mínima:",datetime.datetime(1980,1,1),datetime.datetime(2000,1,1))

birthdate_max = st.slider ("Selecione a data de nascimento máxima:",datetime.datetime(1980,1,1), datetime.datetime(2000,1,1))

df_filtrado = df_func[(df_func["birthdate"] >= birthdate_min) & (df_func["birthdate"] <= birthdate_max)]
#df_filtrado = df_func[df_func["birthdate"] <= birthdate]
st.dataframe(df_filtrado)

col1, col2 = st.columns(2)
with col1:
    st.header("Coluna 1")
    st.write("Conteúdo da coluna 1")
with col2:
    st.header("Coluna 2")
    st.write("Conteúdo da coluna 2")

st.sidebar.header("Sidebar")
st.sidebar.write("Conteúdo da sidebar")
st.sidebar.slider("Slider na sidebar", 0, 100, 50)

#âncora "#inicio" simples

st.sidebar.markdown("[Ir para o topo](#inicio)")

#âncora "#inicio" com botão
st.sidebar.markdown("""
<a href="#inicio"> 
           <div class="stButton st-emotion-cache-8atqhb e1mlolmg0" data-testid="stButton"><button kind="secondary" data-testid="stBaseButton-secondary" aria-label="" class="st-emotion-cache-z8vbw2 e1e4lema2"><div data-testid="stMarkdownContainer" class="st-emotion-cache-3jjymv e1g8wfdw0"><p>Teste</p></div></button></div>
           </a>""", unsafe_allow_html=True)

