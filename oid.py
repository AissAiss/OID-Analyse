from tkinter import RAISED, Tk, Label, Entry, Button, Text

root = Tk()
root.configure(bg='yellow')

# Titre 
title_label = Label(root, text="OID")
title_label.pack(anchor="n")

# Title entry 
title_entry = Entry(root, width=25)
title_entry.pack(anchor="nw")

#Save button function

def save(): 
    pass

save_button = Button(root, text="Save", command=save)
save_button.pack() 

#Cerate text entry 
text_entry = Text(width=40, height=30, border=4, relief=RAISED)
text_entry.pack() 

#root.configure(bg='yellow')
#root.configure(background='white')
#root["bg"] = "white"
#root['background']='white'

root.mainloop() 

