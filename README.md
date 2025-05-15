# Conversor de Números Cistercienses

Este projeto é um conversor de números arábicos para a notação numérica cisterciense, com uma interface web simples construída com Flask.

## 🧠 Sobre o Projeto

Os monges cistercienses usavam um sistema numérico visual único, que permite representar números de 1 a 9999 com um único símbolo. Este projeto transforma números arábicos (como `345`) em sua representação cisterciense correspondente.

## 🚀 Funcionalidades

- Conversão de números arábicos (1 a 9999) para notação cisterciense.
- Exibição visual da representação cisterciense usando uma imagem SVG.
- Interface web simples para uso interativo.

## 📦 Requisitos

- Python 3.10 ou superior
- Pip

## 🔧 Instalação e Execução

Siga os passos abaixo para rodar o projeto localmente:

```bash
# Clone o repositório
git clone https://github.com/gustavoKutzke/numeroCistercienses.git
cd numeroCistercienses

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
python app.py
