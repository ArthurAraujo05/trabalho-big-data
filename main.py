import pandas as pd
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Função para gerar dados fictícios de doações de sangue
def gerar_dados_doacoes(num_linhas):
    cidades = ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Salvador', 'Belo Horizonte', 'Porto Alegre', 'Brasília', 'Recife', 'Fortaleza', 'Manaus']
    tipos_sangue = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    
    datas = []
    quantidade_doada = []
    cidade = []
    tipo_sangue = []
    
    for _ in range(num_linhas):
        data_doacao = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365*2))
        quantidade = round(random.uniform(1.0, 3.5), 1)
        cidade_aleatoria = random.choice(cidades)
        tipo_aleatorio = random.choice(tipos_sangue)
        
        datas.append(data_doacao.strftime('%Y-%m-%d'))
        quantidade_doada.append(quantidade)
        cidade.append(cidade_aleatoria)
        tipo_sangue.append(tipo_aleatorio)
    
    df = pd.DataFrame({
        'data_da_doacao': datas,
        'quantidade_doada': quantidade_doada,
        'cidade': cidade,
        'tipo_sangue': tipo_sangue
    })
    
    return df

# Gerar os dados fictícios
df_doacoes = gerar_dados_doacoes(1000)

# Converter a data para datetime
df_doacoes['data_da_doacao'] = pd.to_datetime(df_doacoes['data_da_doacao'])

# Adicionar colunas de ano e mês
df_doacoes['ano'] = df_doacoes['data_da_doacao'].dt.year
df_doacoes['mes'] = df_doacoes['data_da_doacao'].dt.month

# Análise do tipo sanguíneo
tipo_sangue_count = df_doacoes['tipo_sangue'].value_counts()

# Análise da distribuição geográfica
cidade_count = df_doacoes['cidade'].value_counts()

# Previsões com Random Forest
X = df_doacoes[['ano', 'mes']]  # Ano e Mês
y = df_doacoes['quantidade_doada']  # Quantidade de sangue doada

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar e treinar o modelo Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Fazer previsões
previsao = rf_model.predict(X_test)

# Avaliar o modelo
erro = mean_squared_error(y_test, previsao)
print(f'Erro médio quadrático (MSE): {erro}')

# Visualizar as previsões vs os valores reais
plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Valores Reais', color='blue')
plt.plot(previsao, label='Previsões', linestyle='--', color='red')
plt.title('Previsão de Doações vs Valores Reais')
plt.legend()
plt.show()

# Exibir os resultados da análise do tipo sanguíneo e da distribuição geográfica
print("Distribuição dos tipos sanguíneos:")
print(tipo_sangue_count)

print("\nDistribuição das doações por cidade:")
print(cidade_count)

# Plotando a distribuição dos tipos sanguíneos
plt.figure(figsize=(10, 6))
tipo_sangue_count.plot(kind='bar', color='skyblue')
plt.title('Distribuição dos Tipos Sanguíneos nas Doações')
plt.xlabel('Tipo de Sangue')
plt.ylabel('Número de Doações')
plt.xticks(rotation=45)
plt.show()

# Plotando a distribuição geográfica
plt.figure(figsize=(10, 6))
cidade_count.plot(kind='bar', color='lightcoral')
plt.title('Distribuição das Doações por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Número de Doações')
plt.xticks(rotation=45)
plt.show()
