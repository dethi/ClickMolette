# -*-coding:Utf-8 -*

"""Simulateur de clique molette,
Version 0.1.3,
Réalisé par Deutsch Thibault,
Plus d'info sur http://www.thionnux.fr/
"""

import time
from Tkinter import *

import win32api
import win32con
import pythoncom
import pyHook


APP = 'DEFINI PLUS TARD'


class Interface(Frame):
	def __init__(self, fenetre, **kwargs):
		Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
		self.pack(fill=BOTH)
		self.etat = True
		
		self.message = Label(self, text="Le simulateur de clique molette est démarré.")
		self.message.pack()
		
		cadre_info = Frame(fenetre, width=700, borderwidth=1)
		cadre_info.pack()
		
		message_info = Label(cadre_info, text="Appuyer sur le bouton 'arrêt défil' pour simuler un clique molette")
		message_info.pack(fill=X)
		
		self.bouton_demarrer = Button(self, text="Démarrer", command=self.demarrer)
		self.bouton_demarrer.pack()
		
		self.bouton_arreter = Button(self, text="Arrêter", command=self.arreter)
		self.bouton_arreter.pack()	
	def demarrer(self):
		global APP
		APP.demarrer()
		self.message["text"] = "Le simulateur de clique molette est démarré."
	def arreter(self):
		global APP
		APP.arreter()
		self.message["text"] = "Le simulateur de clique molette est arrêté."
		
		
class Application():
	def __init__(self):
		self.hm = pyHook.HookManager()
		self.hm.KeyDown = self.OnKeyboardEvent
	def demarrer(self):
		self.hm.HookKeyboard()
		return True
	def arreter(self):
		self.hm.UnhookKeyboard()
		return False
	def OnKeyboardEvent(self, event):
		"""Cette fonction reçoit en entrer l'ensemble des événements clavier.
		Elle s'occupe de renvoyer l'événement normal au système ou une touche modifié
		si l'on appuie sur 'Arret défil'
		"""
		if event.Key == "Scroll":
			win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,0,0,0)
			win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,0,0,0)
			return False
		return True
		
		
def main():
	global APP
	
	APP = Application()
	APP.demarrer()
	
	fenetre = Tk()
	interface = Interface(fenetre)
	interface.mainloop()

if __name__ == "__main__":
	main()