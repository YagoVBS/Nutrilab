# **NUTRILAB** 🥗

Projeto fullstack desenvolvido em Django para gerenciamento de pacientes de nutrição.

## **📌 Funcionalidades**

- Autenticação de usuários (login, logout, cadastro)
- Gerenciamento de dados nutricionais
- Upload e manipulação de arquivos de mídia
- Dashboard interativo

## **🚀 Tecnologias Utilizadas**

- **Linguagem:** Python 3
- **Framework:** Django
- **Banco de Dados:** SQLite
- **Front-end:** HTML + CSS + Bootsrap + JS (Django Templates)

## **💂️ Estrutura do Projeto**

NUTRILAB/ 
│── autenticacao/    # Módulo de autenticação de usuários\
│── core/            # Configurações principais e apps globais\
│── media/           # Diretório para uploads de arquivos\
│── plataforma/      # Funcionalidades principais da aplicação\
│── templates/       # Arquivos HTML (Django Templates)\
│── manage.py        # Script para administração do Django\
│── requirements.txt # Dependências do projeto\
│── .gitignore       # Arquivos a serem ignorados pelo Git\
│── README.md        # Documentação do projeto

## **💻 Como Rodar o Projeto?**

### **1️⃣ Clone o repositório**

```bash
git clone https://github.com/seu-usuario/nutrilab.git
cd nutrilab
```

### **2️⃣ Crie um ambiente virtual e ative**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
```

### **3️⃣ Instale as dependências**

```bash
pip install -r requirements.txt
```

### **4️⃣ Realize as migrações**

```bash
python manage.py migrate
```

### **5️⃣ Crie um superusuário (opcional, para acessar o admin)**

```bash
python manage.py createsuperuser
```

### **6️⃣ Inicie o servidor**

```bash
python manage.py runserver
```

Agora, acesse no navegador:\
📍 [**http://127.0.0.1:8000/auth/cadastro**](http://127.0.0.1:8000/auth/cadastro)

## **✅ Como contribuir?**

1. **Fork** este repositório
2. Crie uma nova **branch**:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça as alterações e adicione os commits:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um **Pull Request** 🎉

## **📝 Licença**

Este projeto está sob a licença **MIT**.

