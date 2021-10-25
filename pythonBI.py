#IMPORTAÇÃO DE BIBLIOTECAS
from datetime import time
from os import close
import os
from numpy import string_
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
import plotly.express as px
import plotly.graph_objects as go
import time

#COLETA DE DADOS DO ARQUIVO EM XLSX
xlsx = pd.read_excel(r"C:\Users\gouve\Documents\GitHub\alccg\pythonbi\exemplo.xlsx")
print(xlsx)

#PLOTAGEM E EXPORT DOS GRÁFICOS
fig = px.bar(xlsx, x="valor1", y="valor4", text="valor4", color="valor4", title="TITULO DE TESTE")
fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.show()
fig.write_html(r"C:\Users\gouve\Documents\GitHub\alccg\pythonbi\export\exportHTML.html")
fig.write_image(r"C:\Users\gouve\Documents\GitHub\alccg\pythonbi\export\exportPDF.pdf")

fig = px.bar(xlsx, x="valor3", y="valor2", text="valor4", color="valor4", title="TITULO DE TESTE")
fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.show()
fig.write_html(r"C:\Users\gouve\Documents\GitHub\alccg\pythonbi\export\exportHTML1.html")
fig.write_image(r"C:\Users\gouve\Documents\GitHub\alccg\pythonbi\export\exportPDF1.pdf")