from Klase import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Recepti")
root.geometry("400x220")

frame = customtkinter.CTkFrame(root,fg_color = "transparent")
frame.pack(side = "top", padx=30, pady=30)
# ------------------------------------------------------------------------------------------------------------------------------
b_1 = customtkinter.CTkButton(frame, text="Recepti",command=lambda:list_box_recept())
b_1.grid(row=0, column=0, padx=10, pady=10)

b_2 = customtkinter.CTkButton(frame, text="Namirnice")
b_2.grid(row=1, column=0, padx=10, pady=10)

b_3 = customtkinter.CTkButton(frame, text="Grafici")
b_3.grid(row=2, column=0, padx=10, pady=10)

# ------------------------------------------------------------------------------------------------------------------------------
def list_box_recept():

    t = customtkinter.CTkToplevel(root)
    t.geometry("650x350")

    frame1 = customtkinter.CTkFrame(t,fg_color = "transparent",width=20,height=20)
    frame1.place(relx = 0,rely = 0)

    frame2 = customtkinter.CTkFrame(t,fg_color = "transparent",width=200,height=200)
    frame2.place(relx = 0.45,rely=0)

    frame3 = customtkinter.CTkFrame(t,fg_color = "transparent",width=200,height=200)
    frame3.place(relx = 0,rely=0.5)

    listbox = tk.Listbox(frame1, selectmode=tk.MULTIPLE,width=20)

    for index,row in rec.recepti_df.iterrows():
        row_text = row[0]

        listbox.insert(tk.END, row_text)
# ------------------------------------------------------------------------------------------------------------------------------
    def delete_selected():
        selected_indices = listbox.curselection()
        if selected_indices:
            selected_recipe = selected_indices[0]  # Assuming only one item is selected
            selected_value = listbox.get(selected_recipe)
            print(selected_value)
            rec.obrisi_recept(selected_value)
# ------------------------------------------------------------------------------------------------------------------------------
    def info_recipe():
        selected_indices = listbox.curselection()
        print(selected_indices)

        if selected_indices:
            selected_recipe = selected_indices[0]  # Assuming only one item is selected
            selected_value = listbox.get(selected_recipe)
            celi_recept =(rec.recepti_df[rec.recepti_df["nazivrecepta"] == selected_value])
            celi_recept.dropna(axis = 1,inplace = True)
            return celi_recept.iloc[0]
# ------------------------------------------------------------------------------------------------------------------------------
    def dodaj_recept():
        t1 = customtkinter.CTkToplevel(root)
        t1.geometry("800x550")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
        frame4 = customtkinter.CTkFrame(t1,fg_color = "transparent")
        frame4.pack(side="top", padx=5, pady=5)

        frame5 = customtkinter.CTkFrame(t1,fg_color = "transparent")
        frame5.pack(side="top", padx=5, pady=5)

        frame6 = customtkinter.CTkFrame(t1,fg_color = "transparent")
        frame6.place(relx = 0.8,rely = 0.8)
 
        l_t1 = customtkinter.CTkLabel(frame4, text="Naziv recepta")
        l_t1.pack()
        e_t1 = customtkinter.CTkEntry(frame4, placeholder_text="")
        e_t1.pack()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
        add_entry_button = customtkinter.CTkButton(frame6, text="Dodaj novi sastojak", command=lambda:add_entry())
        add_entry_button.grid(row=1, column=0, padx=3, pady=3, sticky="ew")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
        b = customtkinter.CTkButton(frame5, text="Dodaj recept", command=lambda:rec.dodaj_recept(e_t1.get(),*[x.get() for x in entries]))
        b.grid(row=2, column=0, padx=3, pady=3, sticky="ew")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
        l1_t1 = customtkinter.CTkLabel(frame5, text="Ime sastojka")
        l1_t1.grid(row=0, column=0, padx=3, pady=3, sticky="ew")

        combobox_ingredient = customtkinter.CTkComboBox(frame5, values= rec.namirnice_df["nazivnamirnice"].to_list(), variable="", width=150)
        combobox_ingredient.grid(row=1, column=0 , padx=3, pady=3, sticky="ew")

        l3_t1 = customtkinter.CTkLabel(frame5, text="Jedinica mere")
        l3_t1.grid(row=0, column=1, padx=3, pady=3, sticky="ew")

        combobox_unit = customtkinter.CTkComboBox(frame5, values=list(set(rec.namirnice_df["jedinicamere"].to_list())), variable="", width=150)
        combobox_unit.grid(row=1, column=1, padx=3, pady=3, sticky="ew")

        l2_t1 = customtkinter.CTkLabel(frame5, text="Kolicina")
        l2_t1.grid(row=0, column=2, padx=3, pady=3, sticky="ew")

        e2_t1 = customtkinter.CTkEntry(frame5, placeholder_text="")
        e2_t1.grid(row=1, column=2, padx=3, pady=3, sticky="ew")

        entries = [combobox_ingredient,combobox_unit, e2_t1]

        # def get_widget_values():
        #     return [x.get() for x in entries]
# ------------------------------------------------------------------------------------------------------------------------------
        def add_entry():
            
            frame = customtkinter.CTkFrame(t1,fg_color = "transparent")
            frame.pack(side="top", padx=5, pady=5)

            new_combobox_ingredient = customtkinter.CTkComboBox(frame, values= rec.namirnice_df["nazivnamirnice"].to_list(), variable="", width=150)
            new_combobox_ingredient.grid(row=0, column=0, padx=3, pady=3, sticky="ew")

            new_combobox_unit = customtkinter.CTkComboBox(
                frame, values=list(set(rec.namirnice_df["jedinicamere"].to_list())), variable="", width=150)
            new_combobox_unit.grid(row=0, column=1, padx=3, pady=3, sticky="ew")

            new_e2_t = customtkinter.CTkEntry(frame, placeholder_text="")
            new_e2_t.grid(row=0, column=2, padx=3, pady=3, sticky="ew")

            entries.append(new_combobox_ingredient)
            entries.append(new_combobox_unit)
            entries.append(new_e2_t)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
    b_t = customtkinter.CTkButton(frame2,text = "Obrisi recept",command = lambda:rec.obrisi_recept(delete_selected()))
    b_t.pack(padx=5, pady=5)

    b_t1 = customtkinter.CTkButton(frame2,text = "Sastojci recepta",command = lambda:l_t.configure(text = info_recipe()))
    b_t1.pack(padx=5, pady=5)

    b_t2 = customtkinter.CTkButton(frame2,text = "Dodaj recept",command=lambda:dodaj_recept())
    b_t2.pack(padx=5, pady=5)

    l_t = customtkinter.CTkLabel(frame3,text = "")
    l_t.pack(padx=5, pady=5)
# ------------------------------------------------------------------------------------------------------------------------------



    
    # DODAJ DIREKTNI UPDATE SA SQL
    


    listbox.pack()

root.mainloop()