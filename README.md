# 🎯 Object Detection with YOLOv8

Ce projet propose un système complet de **détection d'objets en temps réel** basé sur l'architecture **YOLOv8** (You Only Look Once) d'Ultralytics, avec une interface graphique interactive développée avec **Streamlit**.

Le modèle est entraîné pour identifier et localiser trois classes d'objets du quotidien à travers un flux vidéo / webcam :
- 💻 **Laptop** (Ordinateur portable)
- 🖊️ **Pen** (Stylo)
- 📱 **Cellphone** (Téléphone portable)

---

## 📋 Sommaire

- [Fonctionnalités](#-fonctionnalités)
- [Structure du Projet](#-structure-du-projet)
- [Prérequis et Installation](#-prérequis-et-installation)
- [Lancement de l'Application Streamlit](#-lancement-de-lapplication-streamlit)
- [Entraînement du Modèle](#-entraînement-du-modèle)
- [Jeu de Données (Dataset)](#-jeu-de-données-dataset)
- [Technologies Utilisées](#-technologies-utilisées)

---

## ✨ Fonctionnalités

- **Détection en temps réel** : Analyse fluide et détection d'objets via la webcam locale.
- **Modèle optimisé** : Poids légers et rapides basés sur `yolov8n` (`best.pt`), adaptés pour une exécution fluide même sans GPU dédié.
- **Interface intuitive** : Dashboard Streamlit permettant de démarrer/arrêter le flux vidéo d'un simple clic.
- **Pipeline d'entraînement reproductible** : Notebook Google Colab fourni pour réentraîner ou affiner le modèle.

---

## 📁 Structure du Projet

```text
Object_Detection_Yolo8/
│
├── Dataset/                     # Données d'entraînement, validation et test
│   ├── train/                   # Images et labels d'entraînement
│   ├── valid/                   # Images et labels de validation
│   ├── test/                    # Images et labels de test
│   └── data.yaml                # Configuration des classes et chemins du dataset
│
├── app.py                       # Application Streamlit pour la détection webcam
├── best.pt                      # Poids du modèle YOLOv8 entraîné
├── Training.ipynb               # Notebook d'entraînement (Google Colab / Jupyter)
├── requirements.txt             # Dépendances Python requises
└── README.md                    # Documentation du projet
```

---

## 🛠️ Prérequis et Installation

### 1. Prérequis
- **Python 3.8+** (recommandé : Python 3.10 ou 3.11)
- Une webcam fonctionnelle (pour l'inférence en direct)

### 2. Cloner le projet (ou se placer dans le répertoire)
```bash
cd Object_Detection_Yolo8
```

### 3. Créer et activer un environnement virtuel (recommandé)
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 4. Installer les dépendances
```bash
pip install -r requirements.txt
```
*(ou manuellement : `pip install ultralytics streamlit opencv-python numpy`)*

---

## 🚀 Lancement de l'Application Streamlit

Pour démarrer l'application web de détection en temps réel via la webcam :

```bash
streamlit run app.py
```

1. Le navigateur s'ouvrira automatiquement à l'adresse `http://localhost:8501`.
2. Cochez la case **"Démarrer la détection"**.
3. Autorisez l'accès à votre webcam si demandé.
4. Les cadres de détection (bounding boxes), les classes détectées et les scores de confiance s'affichent directement sur le flux vidéo.

---

## 🧠 Entraînement du Modèle

Le modèle a été entraîné à partir de `yolov8n.pt` sur Google Colab via le notebook [`Training.ipynb`](Training.ipynb).

### Configuration du fichier `Dataset/data.yaml` :
```yaml
path: ./Dataset
train: train/images
val: valid/images
test: test/images

nc: 3
names:
  0: laptop
  1: pen
  2: cellphone
```

### Ré-entraîner en ligne de commande :
Si vous souhaitez ré-entraîner le modèle en local avec Ultralytics :
```bash
yolo detect train data=Dataset/data.yaml model=yolov8n.pt epochs=20 imgsz=640
```

---

## 📊 Jeu de Données (Dataset)

Le dataset est organisé au format standard YOLO :
- **Images** : Format standard `.jpg` / `.png`.
- **Labels** : Fichiers texte `.txt` avec coordonnées normalisées :
  `<class_id> <x_center> <y_center> <width> <height>`

| Classe | Identifiant | Description |
| :--- | :---: | :--- |
| `laptop` | `0` | Ordinateurs portables |
| `pen` | `1` | Stylos / Feutres |
| `cellphone` | `2` | Téléphones mobiles |

---

## 💻 Technologies Utilisées

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - Architecture d'apprentissage profond pour la détection d'objets.
- [Streamlit](https://streamlit.io/) - Framework de déploiement d'applications web interactives en Python.
- [OpenCV](https://opencv.org/) - Traitement d'images et capture de flux vidéo.
- [PyTorch](https://pytorch.org/) - Moteur d'entraînement sous-jacent.
