# Focus Track API

Sistema de gerenciamento de tarefas desenvolvido com FastAPI, seguindo uma arquitetura backend moderna inspirada no projeto FinTrack.

---

# Problema

Muitas pessoas enfrentam dificuldades para organizar tarefas, controlar produtividade e acompanhar o tempo gasto em atividades importantes.

Além disso, sistemas simples de lista de tarefas normalmente possuem:

* pouca escalabilidade
* baixa organização de código
* ausência de API
* dificuldade de integração com aplicações web/mobile

---

# Solução

O Focus Track API foi desenvolvido para fornecer uma solução moderna de gerenciamento de tarefas utilizando arquitetura backend profissional.

O sistema permite:

* criar tarefas
* acompanhar tempo estimado
* concluir tarefas
* atualizar tarefas
* remover tarefas
* calcular métricas de produtividade

Além disso, a aplicação foi construída utilizando FastAPI e SQLite, permitindo futura integração com frontend React e deploy em nuvem.

---

# Público-Alvo

* Estudantes
* Desenvolvedores
* Profissionais
* Usuários que desejam melhorar produtividade
* Pessoas interessadas em organização pessoal

---

# Funcionalidades

* Criar tarefas
* Listar tarefas
* Buscar tarefa por ID
* Atualizar tarefas
* Concluir tarefas
* Remover tarefas
* Calcular tempo total
* Persistência em banco de dados SQLite
* API RESTful
* Documentação automática Swagger
* Validação de dados com Pydantic

---

# Tecnologias Utilizadas

* Python 3.12+
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Alembic
* Uvicorn
* Pytest
* Git e GitHub

---

# Estrutura do Projeto

```plaintext
focus-track/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── dependencies/
│   │
│   ├── core/
│   │   ├── config/
│   │   ├── security/
│   │   └── exceptions/
│   │
│   ├── database/
│   │   ├── connection.py
│   │   └── base.py
│   │
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── middlewares/
│   ├── utils/
│   │
│   └── main.py
│
├── alembic/
├── tests/
├── .env
├── .env.example
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Endpoints

## Criar tarefa

```http
POST /tasks
```

## Listar tarefas

```http
GET /tasks
```

## Buscar tarefa por ID

```http
GET /tasks/{id}
```

## Atualizar tarefa

```http
PUT /tasks/{id}
```

## Concluir tarefa

```http
PATCH /tasks/{id}/complete
```

## Deletar tarefa

```http
DELETE /tasks/{id}
```

## Tempo total das tarefas

```http
GET /tasks/metrics/total-time
```

---

# Exemplo de Request

```json
{
  "titulo": "Estudar FastAPI",
  "descricao": "Aprender arquitetura backend",
  "tempo_estimado": 120
}
```

---

# Exemplo de Response

```json
{
  "id": 1,
  "titulo": "Estudar FastAPI",
  "descricao": "Aprender arquitetura backend",
  "tempo_estimado": 120,
  "concluida": false,
  "data_criacao": "2026-05-11T14:00:00"
}
```

---

# Como executar o projeto

## 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/focus-track.git
```

---

## 2. Entre na pasta

```bash
cd focus-track
```

---

## 3. Crie o ambiente virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 5. Configure o arquivo .env

```env
DATABASE_URL=sqlite:///./focus_track.db
SECRET_KEY=sua_chave_secreta
DEBUG=True
```

---

## 6. Execute o servidor

```bash
uvicorn app.main:app --reload
```

Servidor disponível em:

```plaintext
http://127.0.0.1:8000
```

---

# Documentação da API

## Swagger

```plaintext
http://127.0.0.1:8000/docs
```

## ReDoc

```plaintext
http://127.0.0.1:8000/redoc
```

---

# Banco de Dados

O projeto utiliza SQLite como banco de dados principal utilizando SQLAlchemy ORM.

As migrations são gerenciadas com Alembic.

---

# Executando Migrations

## Criar migration

```bash
alembic revision --autogenerate -m "create tasks table"
```

## Aplicar migration

```bash
alembic upgrade head
```

---

# Executando Testes

```bash
pytest
```

---

# Melhorias Futuras

* Autenticação JWT
* Sistema de usuários
* Frontend React
* Docker
* PostgreSQL
* Deploy em nuvem
* Logs estruturados
* CI/CD
* Testes automatizados completos

---

# Autor

Marcos André Camargo Belo

Desenvolvedor Backend | Python | FastAPI | APIs RESTful
