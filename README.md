# Portfolio BTS SIO — SLAM

Portfolio personnel réalisé dans le cadre du BTS SIO, option **SLAM**.

Le site présente mon parcours, mes réalisations, mes stages, mes projets et ma veille technologique. Il est généré avec **Pelican**, **Jinja2**, **Markdown** et **Bootstrap 5**, puis publié avec **GitHub Pages**.

## Structure

```text
content/                 # Contenu source en Markdown
├── pages/               # Parcours, stages, projets, certifications...
└── veille/              # Articles de veille technologique

themes/sio_portfolio/   # Thème du portfolio
├── templates/           # Templates Jinja2
└── static/              # CSS, JavaScript, images et bibliothèques

docs/                    # Version statique publiée par GitHub Pages
```

## Travailler en local

Python 3.10+ est recommandé.

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Installer les dépendances :

```bash
pip install pelican markdown
```

Lancer le serveur local :

```bash
pelican -lr
```

Le site est alors accessible sur `http://localhost:8000`.

## Générer la version GitHub Pages

```bash
pelican content -s publishconf.py
```

La version générée est placée dans `docs/`.

Le dépôt peut ensuite être publié avec GitHub Pages en sélectionnant **Deploy from a branch**, puis la branche `main` et le dossier `/docs`.

Les liens du portfolio sont configurés en chemins relatifs afin de fonctionner aussi lorsqu'il est publié dans un dépôt GitHub de type `https://compte.github.io/nom-du-depot/`.

## Personnalisation

Les contenus à modifier se trouvent principalement dans `content/`.

Le rendu général se trouve dans :

- `themes/sio_portfolio/templates/`
- `themes/sio_portfolio/static/css/custom.css`
- `themes/sio_portfolio/static/js/custom.js`

Les fichiers générés dans `docs/` peuvent être régénérés après chaque modification du contenu ou du thème.

## Git

Un `.gitignore` est fourni afin d'éviter de versionner l'environnement virtuel, les fichiers Python temporaires et les fichiers système.

