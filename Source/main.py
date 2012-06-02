# -*-coding:Utf-8 -*

"""Simulateur de clique molette,
Version 0.1.4,
Réalisé par Deutsch Thibault,
Plus d'info sur http://www.thionnux.fr/
"""

import time
from Tkinter import *

import win32api
import win32con
import pythoncom
import pyHook


class Interface(Frame, application):

    """Cette classe gère l'ensemble de l'interface graphique.

    +-- Méthodes --
    | __init__(self, fenetre, application, **kwargs)
    | demarrer(self)
    | arreter(self)
    +-------------

    +-- Attributs --
    | self.application
    | self.message
    | self.cadre_info
    | self.message_info
    | self.bouton_demarrer
    | self.bouton_arreter
    +-------------- 
    """
	
    def __init__(self, fenetre, application, **kwargs):
        """Méthode d'initialisation de l'interface graphique"""
        self.application = application

        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)

        # en-tête
        self.message = Label(self, text="Le simulateur de clique molette est démarré.")
        self.message.pack()

        # information d'utilisation
        self.cadre_info = Frame(self, width=700, borderwidth=1)
        self.cadre_info.pack()
        self.message_info = Label(self.cadre_info, 
            text="Appuyer sur le bouton 'arrêt défil' pour simuler un clique molette")
        self.message_info.pack(fill=X)

        # boutons
        self.bouton_demarrer = Button(self, text="Démarrer", command=self.demarrer)
        self.bouton_demarrer.pack()
        self.bouton_arreter = Button(self, text="Arrêter", command=self.arreter)
        self.bouton_arreter.pack()

    def demarrer(self):
        """Méthode appelée lors de l'appui sur le bouton DEMARRER"""
        self.application.demarrer()
        self.message["text"] = "Le simulateur de clique molette est démarré."

    def arreter(self):
        """Méthoe appelée lors de l'appui sur le bouton ARRETER"""
        self.application.arreter()
        self.message["text"] = "Le simulateur de clique molette est arrêté."
		
class Application():

    """Cette classe gère le coeur de l'application

    +-- Méthodes --
    | __init__(self)
    | demarre(self)
    | arreter(self)
    +--------------

    +-- Attribut --
    | self.hm
    +--------------
    """

    def __init__(self):
        """Méthode d'initialisation de l'application"""
        self.hm = pyHook.HookManager()
        self.hm.KeyDown = self.OnKeyboardEvent

        # demarre le hook
        self.demarrer()

        # initialise l'interface graphique
        fenetre = Tk()
        interface = Interface(fenetre, self)
        interface.mainloop()

    def demarrer(self):
        """Démarre le hook"""
        self.hm.HookKeyboard()

    def arreter(self):
        """Arrête le hook"""
        self.hm.UnhookKeyboard()

    def OnKeyboardEvent(self, event):
        """Cette méthode reçoit en entrer l'ensemble des événements clavier.
        Elle s'occupe de renvoyer l'événement normal au système ou une touche 
        modifié si l'on appuie sur 'Arret défil'
        """
        if event.Key == "Scroll":
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,0,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,0,0,0)
            return False
        return True


def main():
    """Function de démarre de l'application"""
    simulateur = Application()

if __name__ == "__main__":
    main()