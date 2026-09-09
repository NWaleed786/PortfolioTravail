# Configuration de publication du portfolio sur GitHub Pages.
#
# Pour un dépôt GitHub Pages de type projet, les liens du site restent relatifs.
# Si vous souhaitez définir une URL complète, vous pouvez lancer :
#   SITEURL="https://github.com/NWaleed786/PortfolioTravail.git" pelican content -s publishconf.py

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = os.environ.get("SITEURL", "https://github.com/NWaleed786/PortfolioTravail.git")
RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
