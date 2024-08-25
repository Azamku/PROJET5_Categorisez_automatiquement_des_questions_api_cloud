## Ce code contient le code de l'interface utilisateur de notre api déployée sur Azure
import streamlit as st
import requests

st.title('Prédiction de Tags pour Stack Overflow')

input_text = st.text_area("Entrez une question:")

if st.button("Prédire"):
    response = requests.post("https://myfastapiappstack-hnfjcmgehydeb7hm.westeurope-01.azurewebsites.net/predict/", json={"text": input_text}) #adresse de notre app déployée sur azure
    print("toto")
    print(input_text) 
    print(response)
    tags = response.json().get("tags", [])
    st.write("Tags Prédits:", ", ".join(tags))
