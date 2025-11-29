# SmartFlow - Plataforma de Automação Inteligente de Workflows com IA

## Setup Local
1. `pip install -r requirements.txt`
2. Crie `.env` com: `OPENAI_API_KEY=sk-...` (ou GROK_API_KEY)
3. `flask db init` (se usar migrate)
4. `python run.py` → API em http://localhost:5000
5. `celery -A app.celery worker --loglevel=info`
6. Teste via Postman: POST /workflows com JWT.

## Docker
docker-compose up --build

## Branches
- develop: Integração
- feature/*: Novos dev

Mais no diagrama draw.io (anexe se quiser).