from tkinter import END, RAISED, Tk, Label, Entry, Button, Text

from rdflib import Graph
from rdflib import URIRef
from rdflib.namespace import RDF
from rdflib.namespace import FOAF


root = Tk()
root.geometry("1000x500")


# Entry 
label_source = Label(text="Fichier source : ", anchor='w')
##label_source.pack(anchor="w", fill='both')
label_source.grid(row=0, column=0)

entry_source = Entry(width=25)
entry_source.insert(END, "source.ttl")
entry_source.grid(row=1, column=0)

label_target = Label( text="Fichier cible : ", anchor='w')
label_target.grid(row=0, column=1)

entry_target = Entry(width=25)
entry_target.insert(END, "target.ttl")
entry_target.grid(row=1, column=1)

# Compare button function
def open_source(): 
    source = str(entry_source.get())
    g = Graph()
    source = g.parse(source, format="ttl")

    source_output.delete('1.0', END)
    #affichage(source)
    for subj, pred, obj in source:
        source_output.insert(END, "---------------------------------------------------\n")
        source_output.insert(END, "subj : " + subj) 
        source_output.insert(END, "pred : " + pred) 
        source_output.insert(END, "obj : " + obj) 

        if (subj, pred, obj) not in source:
            raise Exception("It better be!")

def open_target(): 
    # Recuperer le text des deux entry 
    target = str(entry_target.get())

    #pass
    g = Graph()
    target = g.parse(target, format="ttl")

    target_output.delete('1.0', END)
    #affichage(target)
    for subj, pred, obj in target:
        target_output.insert(END, "---------------------------------------------------\n")
        target_output.insert(END, "subj : " + subj) 
        target_output.insert(END, "pred : " + pred) 
        target_output.insert(END, "obj : " + obj) 

        if (subj, pred, obj) not in target:
            raise Exception("It better be!")

    
source_button = Button(root, text="Ouvrir", command=open_source)
source_button.grid(row=2, column=0)

target_button = Button(root, text="Ouvrir", command=open_target)
target_button.grid(row=2, column=1)

#Cerate text entry 
source_output = Text(width=60, height=30, border=4, relief=RAISED)
source_output.insert(END, "")
source_output.grid(row=3, column=0)

target_output = Text(width=60, height=30, border=4, relief=RAISED)
target_output.insert(END, "")
target_output.grid(row=3, column=1)


root.mainloop() 