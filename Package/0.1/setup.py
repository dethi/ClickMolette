from distutils.core import setup
import py2exe

"""A utiliser avec la commande ci-dessous dans le même dossier que main.py :
python setupe.py py2exe
"""

setup(console = ["main.py"], description = "Simulateur de clique molette", version = "0.1")