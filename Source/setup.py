# -*-coding:Utf-8 -*

from distutils.core import setup
import py2exe

"""A utiliser avec la commande ci-dessous dans le même dossier que main.py :
python setup.py py2exe
"""

setup(name="ClickMolette", 
      version="0.1.5", 
      description="Simulateur de clique molette", 
      author="Deutsch Thibault", 
      author_email="thibault.deutsch@gmail.com", 
      windows = [
        {
            "script": "main.py",
            "icon_resources": [(1, "icone.ico")]
        }
    ],)