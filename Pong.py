#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from tkinter import *
from random import randrange

def jouer():

	def deplacement_balle():

		global dx, dy
		canevas.move(balle, dx, dy)
		Fenetre.after(30, deplacement_balle)
		x0_balle,y0_balle,x1_balle,y1_balle = canevas.coords(balle)
		x0_1,y0_1,x1_1,y1_1 = canevas.coords(raquette1)
		x0_2,y0_2,x1_2,y1_2 = canevas.coords(raquette2)

		#Test de la colision à la raquette
		if x0_balle <= 0:
			canevas.coords(balle,338, 238, 362, 262)
			canevas.pack_forget()
			menu()
		elif x0_balle < x1_1 and y0_balle > y0_1 and y1_balle < y1_1:
			dx = dx * -1
		elif y0_balle < 0:
			dy = dy * -1

		if x1_balle >= 700:
			canevas.coords(balle,338, 238, 362, 262)
			canevas.pack_forget()
			menu()
		elif x1_balle > x0_2 and y0_balle > y0_2 and y1_balle < y1_2:
			dx = dx * -1
		elif y1_balle > 500:
			dy = dy * -1

	def deplacement_raquette(event):

		x0_1,y0_1,x1_1,y1_1 = canevas.coords(raquette1)
		x0_2,y0_2,x1_2,y1_2 = canevas.coords(raquette2)
		touche = event.keysym
		if touche == "Up" and y0_2 > 0:
			y0_2=y0_2-10
			y1_2=y1_2-10
			canevas.coords(raquette2,x0_2,y0_2,x1_2,y1_2)
		elif touche == "Down" and y1_2 < 500:
			y0_2=y0_2+10
			y1_2=y1_2+10
			canevas.coords(raquette2,x0_2,y0_2,x1_2,y1_2)

		if touche == "z" and y0_1 > 0:
			y0_1=y0_1-10
			y1_1=y1_1-10
			canevas.coords(raquette1,x0_1,y0_1,x1_1,y1_1)
		elif touche == "s" and y1_1 < 500:
			y0_1=y0_1+10
			y1_1=y1_1+10
			canevas.coords(raquette1,x0_1,y0_1,x1_1,y1_1)

	#Fenetre graphique
	Fenetre.title("Jeu du Pong")
	canevas = Canvas(Fenetre,width=700,height=500,bg='#000000',cursor="none")

	#Initialisation du terrain
	canevas.create_line(350, 0, 350, 500, fill='white')
	Bord1 = canevas.create_rectangle(0, 3, 4, 497, fill='white')
	Bord2 = canevas.create_rectangle(696, 3, 700, 497, fill='white')
	Bord3 = canevas.create_rectangle(0, 0, 700, 4, fill='white')
	Bord4 = canevas.create_rectangle(0, 496, 700, 500, fill='white')

	#Initialisation des Modules
	balle = canevas.create_oval((338, 238, 362, 262),fill='white')
	raquette1 = canevas.create_rectangle(20,200,30,300,fill='white')
	raquette2 = canevas.create_rectangle(670,200,680,300,fill='white')


	canevas.focus_set()
	canevas.bind("<Key>", deplacement_raquette)
	canevas.pack()

	deplacement_balle()

	Fenetre.mainloop()
	Fenetre.destroy()

def menu():

	#Initialisation du menu et des boutons
	Fenetre.title('Menu')
	Debut = Button(Fenetre, text='Débuter', command=lambda:[Debut.grid_forget(),Quitter.grid_forget(),jouer()])
	Debut.grid(row=1, column=1)
	Quitter = Button(Fenetre, text='Quitter', command=Fenetre.destroy)
	Quitter.grid(row=1, column=2)

	Fenetre.mainloop()
	Fenetre.destroy()

Fenetre = Tk()
#Direction de la Balle aléatoire
dx = randrange(-8, 8)
dy = randrange(-8, 8)

menu()
