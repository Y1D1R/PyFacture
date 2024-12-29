# PyFacture
PyFacture est un projet Python destiné à automatiser la gestion des dépenses à partir de tickets de caisse. L'application utilise des techniques de traitement d'image et d'extraction de texte (OCR) pour extraire les informations pertinentes d'une photo de ticket de caisse, telles que les produits achetés, leurs prix et la date de l'achat. 

PyFacture/ <br>
├── README.md              # Description du projet (inclure la description et des instructions de démarrage)<br>
├── LICENSE                # (Optionnel) Licence du projet<br>
├── .gitignore             # Fichier pour exclure les fichiers inutiles du contrôle de version<br>
├── requirements.txt       # Liste des dépendances Python<br>
├── pyfacture/             # Répertoire principal du code source<br>
│   ├── __init__.py        # Indique que c'est un package Python<br>
│   ├── main.py            # Point d'entrée principal de l'application<br>
│   ├── ocr/               # Module pour le traitement d'image et OCR<br>
│   │   ├── __init__.py<br>
│   │   ├── ocr_processor.py  # Gestion de l'extraction de texte<br>
│   ├── excel/             # Module pour la gestion des fichiers Excel<br>
│   │   ├── __init__.py<br>
│   │   ├── excel_manager.py  # Création et mise à jour des fichiers Excel<br>
│   ├── utils/             # Fonctions utilitaires<br>
│       ├── __init__.py<br>
│       ├── file_utils.py  # Gestion des fichiers et répertoires<br>
│       ├── date_utils.py  # Gestion des dates<br>
├── data/                  # Répertoire pour stocker les données (temporairement ou en sortie)<br>
│   ├── input/             # Photos de tickets de caisse<br>
│   ├── output/            # Fichiers Excel générés<br>
├── tests/                 # Tests unitaires et fonctionnels<br>
│   ├── __init__.py<br>
│   ├── test_ocr.py        # Tests pour le module OCR<br>
│   ├── test_excel.py      # Tests pour la gestion des fichiers Excel<br>
├── docs/                  # Documentation supplémentaire (optionnel)<br>
│   ├── architecture.md    # Description de l'architecture du projet<br>
│   ├── usage.md           # Guide d'utilisation de l'application<br>
