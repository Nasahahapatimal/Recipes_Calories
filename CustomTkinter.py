from Klase import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Recepti")
root.geometry("400x220")

frame = customtkinter.CTkFrame(root,fg_color = "transparent")
frame.pack(side = "top", padx=30, pady=30)

b_1 = customtkinter.CTkButton(frame, text="Recepti",command=lambda:list_box_recept())
b_1.grid(row=0, column=0, padx=10, pady=10)

b_2 = customtkinter.CTkButton(frame, text="Namirnice")
b_2.grid(row=1, column=0, padx=10, pady=10)

b_3 = customtkinter.CTkButton(frame, text="Grafici")
b_3.grid(row=2, column=0, padx=10, pady=10)

def list_box_recept():

    t = customtkinter.CTkToplevel(root)
    t.geometry("1500x800")

    frame1 = customtkinter.CTkFrame(t,fg_color = "transparent",width=700,height=400)
    frame1.place(relx = 0,rely = 0)

    listbox = tk.Listbox(frame1, selectmode=tk.MULTIPLE,width=100)

    for index,row in rec.recepti_df.iterrows():
        row_text = '|'.join(str(value) for value in row if value is not None)

        listbox.insert(tk.END, row_text)

    frame2 = customtkinter.CTkFrame(t,fg_color = "transparent",width=200,height=200)
    frame2.place(relx = 0.45,rely=0)

    def delete_selected():
        selected_indices = listbox.curselection()
        if selected_indices:
            selected_recipe = selected_indices[0]  # Assuming only one item is selected
            selected_value = listbox.get(selected_recipe).split("|")[0]
            print(selected_value)
            rec.obrisi_recept(selected_value)

    b_t = customtkinter.CTkButton(frame2,text = "Obrisi recept",command = lambda:rec.obrisi_recept(delete_selected()))
    b_t.pack()

    
    # DODAJ DIREKTNI UPDATE SA SQL
    


    listbox.pack()

root.mainloop()