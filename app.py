import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import numpy as np

# Charger le modèle
@st.cache_resource
def load_model():
    return YOLO("best.pt")  # ton modèle YOLOv8

model = load_model()

# Titre Streamlit
st.title("Détection en temps réel avec YOLOv8")
st.markdown("## Ouvrir la webcam pour détecter")

# Démarrer webcam
run = st.checkbox('Démarrer la détection')
FRAME_WINDOW = st.image([])

cap = None

if run:
    cap = cv2.VideoCapture(0)
    st.info("Appuyez sur 'Stop' pour arrêter")
else:
    st.warning("Webcam désactivée")

# Boucle de détection
while run and cap.isOpened():
    success, frame = cap.read()
    if not success:
        st.error("Erreur lors de la lecture de la webcam")
        break

    # Conversion pour le modèle
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Détection avec YOLOv8
    results = model.predict(frame_rgb, imgsz=640, conf=0.5)

    # Annoter l'image
    annotated_frame = results[0].plot()

    # Afficher
    FRAME_WINDOW.image(annotated_frame)

# Libération
if cap:
    cap.release()
