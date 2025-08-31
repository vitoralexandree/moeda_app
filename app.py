import random
import time
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Jogando uma moeda", page_icon="🪙")
st.header("Jogando uma moeda")

if "exec_no" not in st.session_state:
  st.session_state.exec_no = 0

if "historico" not in st.session_state:
  st.session_state.historico = []

n = st.slider("Número de tentativas?", 1, 1000, 50)
col1, col2 = st.columns(2)
executar = col1.button("Executar")
limpar = col2.button("Limpar histórico")

chart =  st.line_chart([0.5])

def toss_coin(n: int) -> float:
  soma = 0
  media = 0.0
  for i in range(1,n + 1):
    r = 1 if random.random() < 0.5 else 0
    soma += r
    media = soma / i
    chart.add_rows([media])
    time.sleep(0.005)
  return media

if executar:
  st.session_state.exec_no += 1
  st.write(f"Executando o experimento de {n} tentativas...")
  media_final = toss_coin(n)
  st.success(f"Média final: {media_final:.3f}")

  st.session_state.historico.append({
    "no": st.session_state.exec_no,
    "tentativas": n,
    "media": round(media_final, 4),
  })

if limpar:
  st.session_state.exec_no = 0
  st.session_state.historico = []
  st.info("Histórico limpo.")

df = pd.DataFrame(st.session_state.historico)
st.subheader("Histórico de execuções")
st.dataframe(df if not df.empty else pd.DataFrame(columns=["no", "tentativas", "media"]))