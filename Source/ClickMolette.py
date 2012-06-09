# -*-coding:Utf-8 -*

"""Simulateur de clique molette,
Version 0.2.0,
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
	
    def __init__(self, fenetre, **kwargs):
        """Méthode d'initialisation de l'interface graphique"""
        self.app = None
        
        Frame.__init__(self, fenetre, width=190, bg="white", **kwargs)
        self.pack(fill=BOTH, expand=False)
        
        # image d'en-tête
        self.img_souris = PhotoImage(file="souris.pgm")
        self.disp_img = Label(self, image=self.img_souris, bg="white")
        self.disp_img.pack(pady=5)
        
        # manuel
        self.cadre_help = Frame(self)
        self.cadre_help.pack(fill=X)
        
        txt_help = "Appuyez sur la touche \"Arrêt Défil\"" + \
            "\npour simuler un clique de molette."
        self.help = Label(self.cadre_help, bg="#c6dfff", width=27, 
            text=txt_help)
        self.help.pack(fill=X)
        
        # état du service
        self.cadre_info = Frame(self, bg="white")
        self.cadre_info.pack(fill=X, padx=10, pady=5)
        
        self.phrase = Label(self.cadre_info, bg="white", 
            text="Etat du service :")
        self.phrase.pack(side="left")
        self.etat = Label(self.cadre_info, bg="white", fg="#00bf00", 
            text="DEMARRÉ")
        self.etat.pack(side="right")
        
        # boutons
        self.cadre_boutons = Frame(self, bg="white")
        self.cadre_boutons.pack(padx=10, pady=5, fill=X)
        
        self.config_img = PhotoImage(file="config.pgm")
        self.config = Button(self.cadre_boutons, image=self.config_img, 
            relief="groove", bg="#dbdbdb", command=self.config)
        self.config.pack(side="right", ipadx=2, ipady=2)        
        
        self.onOff = Button(self.cadre_boutons, text="Arrêter le service", 
            relief="groove", bg="#dbdbdb", width=19, command=self.arreter)
        self.onOff.pack(side="left")

    def demarrer(self):
        """Méthode appelée lors de l'appui sur le bouton DEMARRER"""
        self.app.demarrer()
        self.onOff["text"] = "Arrêter le service"
        self.onOff["command"] = self.arreter
        self.etat["text"] = "DEMARRÉ"
        self.etat["fg"] = "#00bf00"

    def arreter(self):
        """Méthode appelée lors de l'appui sur le bouton ARRETER"""
        self.app.arreter()
        self.onOff["text"] = "Démarrer le service"
        self.onOff["command"] = self.demarrer
        self.etat["text"] = "ARRÊTÉ"
        self.etat["fg"] = "red"
        
    def config(self, retour=False):
        """Méthode appelée lors de l'appui sur le bouton config"""
        self.app.hm.KeyDown = self.app.config
            
    def config_retour(self):
        """Méthode appelée une fois la configuration terminée"""
        txt_help = "Appuyez sur la touche \"" + self.app.touche + \
            "\"\npour simuler un clique de molette."
        #self.help["text"] = txt_help

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
        self.UI = None
        
        self.hm = pyHook.HookManager()
        self.hm.KeyDown = self.OnKeyboardEvent
        
        # touche raccourci par défault
        self.touche = "Scroll"

        # demarre le hook
        self.demarrer()

    def demarrer(self):
        """Démarre le hook"""
        self.hm.HookKeyboard()

    def arreter(self):
        """Arrête le hook"""
        self.hm.UnhookKeyboard()
        
    def config(self, event):
        """Récupère la touche choisi par l'utilisateur"""
        self.touche = event.Key
        self.arreter()
        self.UI.config_retour()
        self.hm.KeyDown = self.OnKeyboardEvent
        self.demarrer()

    def OnKeyboardEvent(self, event):
        """Cette méthode reçoit en entrer l'ensemble des événements clavier.
        Elle s'occupe de renvoyer l'événement modifié ou non.
        """
        if event.Key == self.touche:
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,0,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,0,0,0)
            return False
        return True


def main():
    """Fonction de démarrage de l'application.
    Elle s'occupe d'initialiser l'interface graphique et de lancer la
    bloucle d'exécution.
    """
    fenetre = Tk()
    fenetre.title("ClickMolette")
    fenetre.iconbitmap(default='icone.ico')
    fenetre.resizable(False, False)
    
    interface = Interface(fenetre)
    application = Application()
    
    interface.app = application
    application.UI = interface
    
    interface.mainloop()

    
if __name__ == "__main__":
    main()