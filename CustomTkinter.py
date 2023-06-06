from Klase import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Recepti")
root.geometry("400x220")

frame = customtkinter.CTkFrame(root,fg_color = "transparent")
frame.pack(side = "top", padx=30, pady=30)

b_1 = customtkinter.CTkButton(frame, text="Recepti",command=lambda:recept())
b_1.grid(row=0, column=0, padx=10, pady=10)

b_2 = customtkinter.CTkButton(frame, text="Namirnice")
b_2.grid(row=1, column=0, padx=10, pady=10)

b_3 = customtkinter.CTkButton(frame, text="Grafici")
b_3.grid(row=2, column=0, padx=10, pady=10)

def recept():

    t = customtkinter.CTkToplevel(root)
    t.geometry("900x500")

    frame1 = customtkinter.CTkFrame(t,fg_color = "blue")
    frame1.pack(side = "left",padx = 50,pady = 50)

    listbox = customtkinter.CTkLis(t)
    listbox.grid(row=0, column=0, padx=10, pady=10)
    #DODAJ LISTBOX KROZ TKINTER...

root.mainloop()