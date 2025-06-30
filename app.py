import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Hello, Streamlit!")
st.subheader("Primeiro projeto com Streamlit")
st.write("Digite no terminal `streamlit run app.py`")
st.markdown("**AUTOR:** RAFAEL PROENÇA")
st.markdown("[Como usar markdown?](https://www.markdownguide.org/basic-syntax/)")
st.markdown("[API Reference](https://docs.streamlit.io/develop/api-reference)")

st.subheader("Exibição de dados com Pandas")
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