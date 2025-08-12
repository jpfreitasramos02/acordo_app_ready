# Acordo App - Render Ready

Aplicação Flask para gerar documento DOCX a partir de questionário.

## Rodando localmente
```
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:8000 --workers 2
```
