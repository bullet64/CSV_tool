# -*- coding: utf-8 -*-
'''
Created on 24.02.2015
version: 0.0.1
@author: frank
'''

import time
import tkMessageBox
from tkFileDialog import *


def buttonBeendenClick():
    if tkMessageBox.askyesno('Beenden', 'Soll das Programm wirklich beendet werden?'):
        root.quit()
        root.destroy()


from Tkinter import *            ## Tkinter importieren
root=Tk()                        ## Wurzelfenster!
root.title('CSV-Datei: Kommas gegen Semikolons tauschen!')    ## Titel festlegen
textfenster = Text(root,background='grey')         ## Ein Textfenster erzeugen
textfenster.pack()               ## und anzeigen

labelHinweis = Label(master=root, text='Programm um eine .csv Datei von Google in eine\r.csv-Datei für den Import in myrcm vorzubereiten!', fg='white', bg='gray', font=('Arial', 12))
labelHinweis.place(x=80, y=0, width=420, height=120)



import tkMessageBox
tkMessageBox.showinfo('Quelldatei','Bitte die Quelldatei auswählen!')

# Datei zum Lesen oeffnen, mit Kontrolle ob Datei lesbar. Ansonsten exit()

myPath = askopenfilename(filetypes=[("Quelldatei", ".csv")])
try:
    fobj_in = open(str(myPath),"r")
except IOError:
    print "Error: can\'t find file or read data"
    tkMessageBox.showerror("Error", "Can't read file!")
    exit()
else:
    print "Written content in the file successfully"
    
    
import tkMessageBox
tkMessageBox.showinfo('Zieldatei','Bitte die Zieldatei auswaehlen!')


# Datei zum Schreiben oeffnen.

myPath2 = asksaveasfilename(filetypes=[("Zieldatei", ".csv")])
fobj_out = open(str(myPath2),"w")



# Variable i definieren
i = 1

# For-Schleife
for line in fobj_in:
    #print line.rstrip() #schreibt jede gefundene Zeile in die Konsole
    zeile = line.replace(",", ";")
    fobj_out.write(str(i) + ": " + zeile) # schreibt jede geaenderte Zeile in die neue Datei
    print zeile.rstrip() #schreibt jede geaenderte Zeile in die Konsole
    i = i + 1
    
# Dateien wieder schliessen
fobj_in.close()
fobj_out.close()

#import tkMessageBox
#tkMessageBox.showwarning('Programmende','Sie haben es geschafft!')
# Button Beenden
buttonBeenden = Button(master=root, bg='#FBD975', text='Programm beenden?',
                       command=buttonBeendenClick)
buttonBeenden.place(x=164, y=94, width=240, height=27)

root.mainloop()