# **Trabalho Big Data - Análise de Doações de Sangue**

Este projeto faz parte de um trabalho de Big Data e tem como objetivo analisar dados de doações de sangue. O foco é usar técnicas de **Machine Learning** para prever a quantidade de doações de sangue em diferentes cidades e tipos sanguíneos ao longo do tempo, além de realizar análises geográficas e de tipo sanguíneo.

## **Estrutura do Projeto**

O repositório contém scripts Python que fazem a geração de dados fictícios de doações de sangue, além de análise e previsões usando modelos de Machine Learning como **Random Forest**.

### **Funcionalidades**
1. **Geração de Dados**:
   - Geração de um conjunto de dados fictícios de doações de sangue com informações como:
     - Data da doação
     - Quantidade de sangue doado
     - Cidade de origem da doação
     - Tipo sanguíneo
     
2. **Análise de Dados**:
   - Análise de distribuição de doações por **tipo sanguíneo**.
   - Análise de distribuição geográfica das doações por **cidade**.
   
3. **Previsões de Doações**:
   - Uso de **Random Forest** para prever a quantidade de sangue doado com base em variáveis como o ano e o mês da doação.

---

## **Pré-requisitos**

Antes de rodar o projeto, você precisará garantir que as seguintes bibliotecas estejam instaladas no seu ambiente Python:

- **pandas**: Para manipulação de dados
- **numpy**: Para operações matemáticas
- **matplotlib**: Para visualização de gráficos
- **scikit-learn**: Para criação e avaliação de modelos de Machine Learning

### Instalação das dependências:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## **Rodando o Projeto**

### **1. Criando o Ambiente Virtual**
É recomendável rodar o projeto em um ambiente virtual para garantir que as dependências não interfiram com outros projetos.

Para criar o ambiente virtual, execute:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

- **No macOS/Linux**:

```bash
source venv/bin/activate
```

- **No Windows**:

```bash
.\venv\Scripts\activate
```

### **2. Rodando o Código**

Após ativar o ambiente virtual e instalar as dependências, basta executar o script principal:

```bash
python main.py
```

Isso gerará os gráficos de previsão de doações, análise de tipos sanguíneos e a distribuição geográfica das doações.

### **3. Gerando Dados Fictícios**
O script também inclui a geração de dados fictícios de doações de sangue. Caso queira rodar o script para gerar os dados antes de rodar a análise, basta executar a função de geração de dados.

---

## **Estrutura dos Dados**

O conjunto de dados contém as seguintes colunas:

- **data_da_doacao**: Data da doação de sangue.
- **quantidade_doada**: Quantidade de sangue doada (em litros ou unidades).
- **cidade**: Cidade onde a doação foi realizada.
- **tipo_sangue**: Tipo sanguíneo da pessoa que fez a doação.

---

## **Modelos de Machine Learning Utilizados**

- **Random Forest**: Utilizado para prever a quantidade de doações com base nas variáveis **ano** e **mês**. O modelo é treinado com os dados históricos e depois é avaliado com um conjunto de testes.

---

## **Visualizações**

O projeto gera as seguintes visualizações:

1. **Gráfico de Previsões vs Valores Reais**:
   - Comparação entre as previsões de doações feitas pelo modelo e os valores reais.

2. **Distribuição dos Tipos Sanguíneos**:
   - Gráfico de barras mostrando a quantidade de doações para cada tipo sanguíneo.

3. **Distribuição Geográfica das Doações**:
   - Gráfico de barras mostrando a quantidade de doações por cidade.

---

## **Contribuições**

Se você quiser contribuir para o projeto, sinta-se à vontade para abrir um **Pull Request**. Qualquer contribuição é bem-vinda!

---

## **Licença**

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
