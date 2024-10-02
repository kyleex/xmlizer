# Convertisseur DOCX vers XML

Ce projet propose une application web simple construite avec **Streamlit**, permettant aux utilisateurs de téléverser des fichiers `.docx` (par exemple, des documents téléchargés depuis Google Docs) et de les convertir en fichiers XML structurés. L'objectif de cet outil est de simplifier le processus de conversion de contenu de documents en XML pour un traitement ou une intégration ultérieure dans des systèmes plus complexes.

## Fonctionnalités

- Téléversez un fichier `.docx` et générez un fichier XML avec le contenu du document.
- Prend en charge les formats de base tels que :
  - Paragraphes
  - Titres (Headings)
  - Listes (optionnel)
- Interface web simple et intuitive propulsée par **Streamlit**.

## Installation

### Prérequis
Assurez-vous que Python est installé sur votre système. Vous pouvez le télécharger sur [python.org](https://www.python.org/downloads/).

### Dépendances
Installez les dépendances requises en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

### Lancer l'application
Pour démarrer l'application Streamlit, exécutez la commande suivante dans votre terminal :

```bash
streamlit run app.py
```
Cela ouvrira l'application dans votre navigateur par défaut. Si le navigateur ne s'ouvre pas automatiquement, visitez http://localhost:8501 pour accéder à l'application.

### Utilisation
- Téléchargez le document que vous souhaitez convertir au format .docx (par exemple, depuis Google Docs).
- Ouvrez l'application web.
- Téléversez le fichier .docx à l'aide de l'interface fournie.
- Téléchargez le fichier XML converti.


### Contribuer
N'hésitez pas à forker ce dépôt et à apporter vos contributions. Les pull requests sont les bienvenues !

### Licence
Ce projet est sous licence MIT - consultez le fichier LICENSE pour plus de détails.