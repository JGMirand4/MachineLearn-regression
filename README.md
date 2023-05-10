# Análise de Incêndios Florestais

Este repositório contém um exemplo de código em Python para realizar uma análise de incêndios florestais usando regressão com árvore de decisão. O código utiliza a biblioteca pandas para ler e manipular os dados, numpy para operações numéricas, matplotlib para visualização e scikit-learn para a construção do modelo de regressão.

## Descrição do Código

O código possui as seguintes etapas:

1. Importação das bibliotecas necessárias: pandas, numpy, matplotlib, DecisionTreeRegressor do scikit-learn e LabelEncoder do scikit-learn.

2. Leitura da base de dados dos incêndios florestais usando o pandas.

3. Seleção dos atributos de entrada para análise. Neste caso, são considerados os atributos: X, Y, month, day, FFMC, DMC, DC, ISI, temp, RH, wind, rain e area.

4. Conversão das colunas de strings (month e day) para valores numéricos usando o LabelEncoder do scikit-learn.

5. Definição do atributo alvo (area), que representa a área queimada em hectares.

6. Divisão do conjunto de dados em conjuntos de treinamento e teste, com 70% dos dados sendo utilizados para treinamento e 30% para teste.

7. Treinamento do modelo de regressão com a função DecisionTreeRegressor do scikit-learn.

8. Realização de previsões usando o conjunto de teste.

9. Cálculo do Mean Squared Error (MSE), que mede a média dos erros ao quadrado entre os valores reais e as previsões.

10. Cálculo do R-quadrado (R^2 Score), que indica a proporção da variância nos valores da variável dependente que é previsível a partir das variáveis independentes.

11. Plotagem de um gráfico de dispersão para comparar os valores reais com as previsões.

## Execução do Código

Para executar o código, siga as etapas abaixo:

1. Certifique-se de ter as bibliotecas pandas, numpy, matplotlib e scikit-learn instaladas no seu ambiente Python.

2. Baixe o arquivo `forestfires.csv` e coloque-o no mesmo diretório do arquivo Python.

3. Execute o código Python e observe os resultados exibidos no console.

4. Verifique o gráfico de dispersão gerado para visualizar a relação entre os valores reais e as previsões.

Sinta-se à vontade para explorar e modificar o código de acordo com suas necessidades.

**Observação:** Certifique-se de ter as permissões necessárias para acesso aos dados e verifique a documentação oficial das bibliotecas utilizadas para obter mais informações sobre os métodos e funcionalidades utilizadas no código.

