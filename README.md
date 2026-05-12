# 🎯 Focus Track

> Sistema fullstack de gerenciamento de tarefas e produtividade pessoal.

![Version](https://img.shields.io/badge/version-1.0.0-6c63ff?style=flat-square)
![Python](https://img.shields.io/badge/python-3.11+-3776ab?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=flat-square&logo=fastapi&logoColor=white)
![Tests](https://img.shields.io/badge/tests-13%20passed-34d399?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-fbbf24?style=flat-square)

---

## 📌 O Problema

Estudantes e profissionais frequentemente enfrentam dificuldades para organizar suas tarefas diárias, perder o controle do tempo e manter a motivação ao longo do dia. A falta de uma ferramenta simples, rápida e focada resulta em procrastinação, sobrecarga mental e baixa produtividade.

## 💡 A Solução

O **Focus Track** é um sistema web fullstack que centraliza o gerenciamento de tarefas em uma interface limpa e responsiva. Com ele, o usuário pode criar, acompanhar e concluir tarefas, visualizar seu progresso em tempo real e receber frases motivacionais para manter o foco.

---

## ✨ Funcionalidades

- ✅ **CRUD completo de tarefas** — criar, listar, editar, concluir e excluir
- 📊 **Dashboard** — total de tarefas, concluídas, pendentes e tempo estimado
- 📈 **Barra de progresso** — visualização do percentual de conclusão
- 💬 **Frases motivacionais** — integração com a API pública ZenQuotes
- 🔍 **Filtros** — visualizar todas, pendentes ou concluídas
- 📱 **Responsivo** — funciona em desktop e mobile
- 📝 **Documentação automática** — Swagger UI em `/docs`

---

## 🛠️ Tecnologias

### Backend
| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.11+ | Linguagem principal |
| FastAPI | 0.111 | Framework web |
| SQLAlchemy | 2.0 | ORM |
| SQLite | — | Banco de dados |
| Pydantic | 2.7 | Validação de dados |
| Uvicorn | 0.29 | Servidor ASGI |
| Httpx | 0.27 | Cliente HTTP async |

### Frontend
| Tecnologia | Uso |
|---|---|
| HTML5 | Estrutura |
| CSS3 | Estilização (sem frameworks) |
| JavaScript puro (ES6+) | Lógica e integração com API |

### Qualidade & DevOps
| Ferramenta | Uso |
|---|---|
| Pytest | Testes automatizados |
| Ruff | Linting |
| GitHub Actions | CI/CD pipeline |

---

## 🏗️ Arquitetura

O projeto segue os princípios da **Clean Architecture**, com separação clara de responsabilidades:

```
focus-track/
├── app/
│   ├── api/
│   │   └── routes/          # Endpoints HTTP (controllers)
│   │       ├── tasks.py
│   │       └── quotes.py
│   ├── core/
│   │   ├── config/          # Configurações da aplicação
│   │   │   └── settings.py
│   │   └── database/        # Conexão e sessão do banco
│   │       └── connection.py
│   ├── models/              # Modelos ORM (entidades do banco)
│   │   └── task.py
│   ├── repositories/        # Acesso a dados (CRUD)
│   │   └── task_repository.py
│   ├── schemas/             # Schemas Pydantic (DTOs)
│   │   ├── task.py
│   │   └── quote.py
│   ├── services/            # Regras de negócio
│   │   ├── task_service.py
│   │   └── quote_service.py
│   ├── utils/
│   │   └── logging.py       # Configuração de logs
│   └── main.py              # Entry point da aplicação
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── api.js           # Camada de comunicação com a API
│   │   ├── tasks.js         # Lógica de tarefas
│   │   ├── quotes.js        # Lógica de frases
│   │   └── app.js           # Inicialização e eventos globais
│   └── assets/
│
├── tests/
│   ├── conftest.py
│   ├── test_tasks.py
│   └── test_quotes.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── ruff.toml
├── .env.example
├── .gitignore
├── LICENSE
├── VERSION
└── README.md
```

### Fluxo de dados

```
HTTP Request
    │
    ▼
 Router (api/routes)
    │
    ▼
 Service (regras de negócio)
    │
    ▼
 Repository (acesso ao banco)
    │
    ▼
 Model (SQLAlchemy ORM)
    │
    ▼
 SQLite Database
```

---

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.11 ou superior
- pip

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/focus-track.git
cd focus-track
```

### 2. Crie e ative o ambiente virtual

```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
# Edite o .env se necessário
```

---

## ▶️ Executando o projeto

### Backend

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

O servidor estará disponível em: **http://localhost:8000**

### Frontend

O frontend é servido automaticamente pelo FastAPI como arquivos estáticos.
Acesse **http://localhost:8000** para usar a aplicação completa.

> 💡 Para desenvolvimento frontend separado, abra `frontend/index.html` diretamente no navegador e altere `API_BASE` em `js/api.js` para `http://localhost:8000/api/v1`.

### Documentação da API (Swagger)

Acesse **http://localhost:8000/docs** para a documentação interativa.

---

## 🧪 Testes

### Executar todos os testes

```bash
pytest tests/ -v
```

### Executar com cobertura

```bash
pytest tests/ -v --tb=short
```

### Resultado esperado

```
tests/test_quotes.py::test_get_random_quote_fallback PASSED
tests/test_quotes.py::test_get_random_quote_structure PASSED
tests/test_quotes.py::test_health_check PASSED
tests/test_tasks.py::test_create_task PASSED
tests/test_tasks.py::test_list_tasks PASSED
tests/test_tasks.py::test_get_task PASSED
tests/test_tasks.py::test_update_task PASSED
tests/test_tasks.py::test_complete_task PASSED
tests/test_tasks.py::test_delete_task PASSED
tests/test_tasks.py::test_task_not_found PASSED
tests/test_tasks.py::test_invalid_task_empty_title PASSED
tests/test_tasks.py::test_invalid_task_blank_title PASSED
tests/test_tasks.py::test_task_stats PASSED

13 passed
```

---

## 🔍 Lint

### Verificar código

```bash
ruff check app/ tests/
```

### Corrigir automaticamente

```bash
ruff check app/ tests/ --fix
```

---

## 📡 Endpoints da API

### Tarefas

| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `/api/v1/tasks/` | Criar tarefa |
| `GET` | `/api/v1/tasks/` | Listar todas as tarefas |
| `GET` | `/api/v1/tasks/stats` | Estatísticas do dashboard |
| `GET` | `/api/v1/tasks/{id}` | Buscar tarefa por ID |
| `PUT` | `/api/v1/tasks/{id}` | Atualizar tarefa |
| `PATCH` | `/api/v1/tasks/{id}/complete` | Marcar como concluída |
| `DELETE` | `/api/v1/tasks/{id}` | Deletar tarefa |

### Frases

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/api/v1/quotes/random` | Frase motivacional aleatória |

### Sistema

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/health` | Health check |
| `GET` | `/docs` | Swagger UI |
| `GET` | `/redoc` | ReDoc |

### Exemplos de payload

**Criar tarefa:**
```json
POST /api/v1/tasks/
{
  "title": "Estudar FastAPI",
  "description": "Capítulos 3 e 4 da documentação oficial",
  "estimated_time": 90
}
```

**Resposta:**
```json
{
  "id": 1,
  "title": "Estudar FastAPI",
  "description": "Capítulos 3 e 4 da documentação oficial",
  "estimated_time": 90,
  "completed": false,
  "created_at": "2025-01-15T10:30:00"
}
```

**Stats:**
```json
GET /api/v1/tasks/stats
{
  "total": 5,
  "completed": 2,
  "pending": 3,
  "total_estimated_time": 240,
  "completion_rate": 40.0
}
```

---

## ⚙️ CI/CD — GitHub Actions

O pipeline executa automaticamente em `push` e `pull_request`:

```
1. Checkout do código
2. Setup Python 3.11
3. Instalação de dependências
4. Ruff lint
5. Pytest (13 testes)
```

Arquivo: `.github/workflows/ci.yml`

---

## 🌐 Deploy no Render

### Passo a passo

1. Faça push do projeto para o GitHub
2. Acesse [render.com](https://render.com) e crie uma conta
3. Clique em **New → Web Service**
4. Conecte seu repositório GitHub
5. Configure:

| Campo | Valor |
|---|---|
| **Environment** | Python |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |

6. Adicione as variáveis de ambiente:
   - `DATABASE_URL=sqlite:///./focus_track.db`
   - `DEBUG=false`

7. Clique em **Deploy**

> 🔗 Link do deploy: _adicione após fazer o deploy_

---

## 👤 Autor

Desenvolvido para o Bootcamp de Engenharia de Software / Desenvolvimento Fullstack.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📌 Versão

`1.0.0` — Veja o arquivo [VERSION](VERSION).
