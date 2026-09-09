# Configuration de publication du portfolio sur GitHub Pages.
#
# Pour un dépôt GitHub Pages de type projet, les liens du site restent relatifs.
# Si vous souhaitez définir une URL complète, vous pouvez lancer :
#   SITEURL="https://votre-compte.github.io/votre-depot" pelican content -s publishconf.py

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = os.environ.get("SITEURL", "")
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
