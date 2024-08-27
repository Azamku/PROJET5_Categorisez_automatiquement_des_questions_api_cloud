from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
from typing import List
from utils import preprocess_text  # Assurez-vous que utils.py est dans le même répertoire

app = FastAPI(title='API de prédiction de tags', description='Renvoie les tags liés au post.')

# Chargement des modèles pré-entraînés
try:
    bow_model = joblib.load('tag_predictor_bow_model.pkl')
    mlb_job = joblib.load('mlb_bow_model.pkl')
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Erreur lors du chargement des modèles: {e}")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

class Question(BaseModel):
    text: str

class Prediction(BaseModel):
    tags: List[str]


@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API de prédiction de tags. Consultez /docs pour plus d'informations."}

@app.post("/predict/")
async def predict_tags(question: Question):
    try:
        print("debut de la fonction predict sur main.py!")
        print(question.text)
        # Prétraiter le texte
        text_cleaned_list = preprocess_text(question.text)
        text_cleaned_joined = ' '.join(text_cleaned_list)

        # Faire la prédiction
        bow_predict_result = bow_model.predict([text_cleaned_joined])
        tags_predits = mlb_job.inverse_transform(bow_predict_result)
        predicted_tags_list = [tag for tags in tags_predits for tag in tags]
        print(predicted_tags_list)
        return {"tags": predicted_tags_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la prédiction: {e}")
