# -*-coding:Utf-8 -*

"""Simulateur de clique molette,
Version 0.1.5,
Réalisé par Deutsch Thibault,
Plus d'info sur http://www.thionnux.fr/
"""

from Tkinter import *

import win32api
import win32con
import pythoncom
import pyHook


class Interface(Frame):

    """Cette classe gère l'ensemble de l'interface graphique.

    +-- Méthodes --
    | __init__(self, fenetre, application, **kwargs)
    | demarrer(self)
    | arreter(self)
    +-------------

    +-- Attributs --
    | self.application
    | self.img_souris
    | self.disp_img
    | self.cadre_info
    | self.phrase
    | self.etat
    | self.cadre_bouton
    | self.onOff
    +-------------- 
    """
	
    def __init__(self, fenetre, application, **kwargs):
        """Méthode d'initialisation de l'interface graphique"""
        self.application = application

        Frame.__init__(self, fenetre, width=190, bg="white", **kwargs)
        self.pack(fill=BOTH, expand=False)

        # image
        self.img_souris = PhotoImage(file="souris.gif")
        self.disp_img = Label(self, image=self.img_souris, bg="white")
        self.disp_img.pack()
        
        # manuel
        self.cadre_help = Frame(self)
        self.cadre_help.pack(fill=X)
        
        self.help = Label(self.cadre_help, bg="#c6dfff",
            text="Appuyez sur la touche \"Arrêt Défil\" \n" + \
            "pour simuler un clique de molette.")
        self.help.pack(ipadx=5)
        
        # état du service
        self.cadre_info = Frame(self, bg="white")
        self.cadre_info.pack(fill=X, padx=10, ipady=5)
        
        self.phrase = Label(self.cadre_info, bg="white", 
            text="Etat du service :")
        self.phrase.pack(side="left")
        self.etat = Label(self.cadre_info, bg="white", fg="#00bf00", 
            text="DEMARRER")
        self.etat.pack(side="right")
        
        # bouton on/off
        self.cadre_bouton = Frame(self, width=100, bg="white")
        self.cadre_bouton.pack(padx=10, ipady=5, fill=X)
        
        self.onOff = Button(self.cadre_bouton, text="Arrêter le service", 
            relief="groove", bg="#dbdbdb", command=self.arreter)
        self.onOff.pack(fill=X)

    def demarrer(self):
        """Méthode appelée lors de l'appui sur le bouton DEMARRER"""
        self.application.demarrer()
        self.onOff["text"] = "Arrêter le service"
        self.onOff["command"] = self.arreter
        self.etat["text"] = "DEMARRER"
        self.etat["fg"] = "#00bf00"

    def arreter(self):
        """Méthode appelée lors de l'appui sur le bouton ARRETER"""
        self.application.arreter()
        self.onOff["text"] = "Demarrer le service"
        self.onOff["command"] = self.demarrer
        self.etat["text"] = "ARRÊTER"
        self.etat["fg"] = "red"

		
class Application():

    """Cette classe gère le coeur de l'application

    +-- Méthodes --
    | __init__(self)
    | demarrer(self)
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
        fenetre.title("ClickMolette")
        fenetre.iconbitmap(default='icone.ico')
        fenetre.resizable(False, False)
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
    """Fonction de démarrage de l'application"""
    simulateur = Application()

if __name__ == "__main__":
    main()