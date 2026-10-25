# 1. L'OS de base : Python 3.12 en version allégée
FROM python:3.12-slim

# 2. Le dossier de travail
WORKDIR /app

# 3. Les dépendances (Optimisation du cache incluse en copiant requirements.txt en premier)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Le code source
COPY main.py .

# 5. La sécurité : Utilisateur non-root
RUN useradd -m appuser
USER appuser

# 6. Le lancement du serveur (uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
