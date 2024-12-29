# PyFacture
PyFacture est un projet Python destiné à automatiser la gestion des dépenses à partir de tickets de caisse. L'application utilise des techniques de traitement d'image et d'extraction de texte (OCR) pour extraire les informations pertinentes d'une photo de ticket de caisse, telles que les produits achetés, leurs prix et la date de l'achat. 

PyFacture/
├── README.md              # Description du projet (inclure la description et des instructions de démarrage)
├── LICENSE                # (Optionnel) Licence du projet
├── .gitignore             # Fichier pour exclure les fichiers inutiles du contrôle de version
├── requirements.txt       # Liste des dépendances Python
├── pyfacture/             # Répertoire principal du code source
│   ├── __init__.py        # Indique que c'est un package Python
│   ├── main.py            # Point d'entrée principal de l'application
│   ├── ocr/               # Module pour le traitement d'image et OCR
│   │   ├── __init__.py
│   │   ├── ocr_processor.py  # Gestion de l'extraction de texte
│   ├── excel/             # Module pour la gestion des fichiers Excel
│   │   ├── __init__.py
│   │   ├── excel_manager.py  # Création et mise à jour des fichiers Excel
│   ├── utils/             # Fonctions utilitaires
│       ├── __init__.py
│       ├── file_utils.py  # Gestion des fichiers et répertoires
│       ├── date_utils.py  # Gestion des dates
├── data/                  # Répertoire pour stocker les données (temporairement ou en sortie)
│   ├── input/             # Photos de tickets de caisse
│   ├── output/            # Fichiers Excel générés
├── tests/                 # Tests unitaires et fonctionnels
│   ├── __init__.py
│   ├── test_ocr.py        # Tests pour le module OCR
│   ├── test_excel.py      # Tests pour la gestion des fichiers Excel
├── docs/                  # Documentation supplémentaire (optionnel)
│   ├── architecture.md    # Description de l'architecture du projet
│   ├── usage.md           # Guide d'utilisation de l'application
