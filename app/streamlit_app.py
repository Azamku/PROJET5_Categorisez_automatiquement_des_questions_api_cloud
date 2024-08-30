## Ce code contient le code de l'interface utilisateur de notre api déployée sur Azure
import streamlit as st
import requests

st.title('Prédiction de Tags pour Stack Overflow')

input_text = st.text_area("Entrez une question:")

if st.button("Prédire"):
    response = requests.post("http://fastapistack.azurewebsites.net/predict", json={"text": input_text}) #adresse de notre app déployée sur azure
    print("toto")
    print(input_text) 
    print(response)
    if response.status_code == 200:
        tags = response.json().get("tags", [])
        st.write("Tags Prédits:", ", ".join(tags))
    else:
        st.write(f"Erreur: Impossible de contacter l'API (status code: {response.status_code})")
