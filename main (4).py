import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Lendo a base de dados dos incêndios com a ajuda do Pandas
dados = pd.read_csv('forestfires.csv')

# Atributos de entrada para análise
x = dados[['X', 'Y', 'month', 'day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area']].values

# Convetendo as colunas de strings, para valores numéricos
le = LabelEncoder()
x[:, 2] = le.fit_transform(x[:, 2])
x[:, 3] = le.fit_transform(x[:, 3])

# Atributo alvo 
y = dados['area'].values

# Divisão do conjuto em treinamento e teste, como visto anteriormente
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=0)

# Treinando modelo com a função de regressão linear
modelo_arvore = DecisionTreeRegressor(random_state=0)
modelo_arvore.fit(x_treino, y_treino)

# Fazendo as previsões com o conjunto de teste
y_prev = modelo_arvore.predict(x_teste)

# Calculando o MSE 
mse = mean_squared_error(y_teste, y_prev)
print('Mean Squared Error:', mse)

# Calculando o R-quadratico
r2 = r2_score(y_teste, y_prev)
print('R^2 Score:', r2)

# Plotando gráfico de dispersão
plt.scatter(y_teste, y_prev)
plt.xlabel('Valores reais')
plt.ylabel('Previsões')
plt.show()

