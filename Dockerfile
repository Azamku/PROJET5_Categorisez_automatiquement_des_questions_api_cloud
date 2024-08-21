# Utiliser une image Python de base
FROM python:3.9-slim

# D�finir le r�pertoire de travail
WORKDIR /app

# Copier les fichiers n�cessaires
COPY . /app

# Installer les d�pendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port pour l'application
EXPOSE 8000

# Lancer l'application FastAPI avec Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
