import psycopg2 as pg
import pandas as pd
import matplotlib.pyplot as plt
import pyautogui as pg1
import customtkinter
import tkinter as tk


class Recepti:

    def __init__(self):

        self.con = pg.connect(database='Recepti',
                              user='postgres',
                              password='admin',
                              host='localhost',
                              port='5432')

        self.namirnice_df = None
        self.recepti_df = None
        self.namirnica = None
        self.kalorije = None

    def import_from_sql(self):

        self.namirnice_df = pd.read_sql_query(
            'SELECT * FROM NAMIRNICA', self.con)
        self.recepti_df = pd.read_sql_query('SELECT * FROM RECEPT', self.con)

    def lista_svega(self):

        self.namirnica = self.namirnice_df.iloc[:, 0].to_list()
        self.kalorije = self.namirnice_df.iloc[:, 3].to_list()

    def list_box_recepti(self):

        cursor = self.con.cursor()
        cursor.execute('SELECT * FROM RECEPT')

        rows = cursor.fetchall()

        for row in rows:
            
            print(row)
            print(len(row))

    def dodaj_namirnicu(self, NazivNamirnice, JedinicaMere, Kolicina, Kalorije):

        cursor = self.con.cursor()
        nam = "INSERT INTO NAMIRNICA(NazivNamirnice,JedinicaMere,Kolicina,Kalorije) VALUES ('{}','{}',{},{})".format(
            NazivNamirnice.capitalize(), JedinicaMere.lower(), Kolicina, Kalorije)
        cursor.execute(nam)
        self.con.commit()
        cursor.close()

    def dodaj_recept(self, NazivRecepta, *values):

        cursor = self.con.cursor()
        rec = "INSERT INTO RECEPT(NazivRecepta) VALUES ('{}')".format(
            NazivRecepta)
        cursor.execute(rec)
        self.con.commit()

        attribute_names = ['Namirnica', 'JedinicaMere', 'Kolicina']

        for index, value in enumerate(values, start=1):
            attribute_name = attribute_names[index % len(
                attribute_names) - 1] + str((index + 2) // 3)
            update_query = "UPDATE RECEPT SET {} = '{}' WHERE NazivRecepta = '{}'".format(
                attribute_name, value, NazivRecepta)
            cursor.execute(update_query)
            self.con.commit()

        cursor.close()

        return "Recept uspesno dodat!"

    def obrisi_namirnicu(self, namirnica):

        cursor = self.con.cursor()
        del_nam = "DELETE FROM NAMIRNICA WHERE NazivNamirnice = '{}'".format(
            namirnica.capitalize())
        cursor.execute(del_nam)
        self.con.commit()
        cursor.close()

        return "Namirnica uspeno obrisana!"

    def obrisi_recept(self, NazivRecepta):

        cursor = self.con.cursor()
        del_rec = "DELETE FROM RECEPT WHERE NazivRecepta = '{}'".format(
            NazivRecepta)
        cursor.execute(del_rec)
        self.con.commit()
        cursor.close()
        return "Recept uspeno obrisan!"

    def ocitaj_kalorije_sve_namirnice(self):

        return self.namirnice_df.iloc[0:][["nazivnamirnice", "kalorije"]].to_string(index=False, header=False)

    def ocitaj_kalorije_namirnica(self, Namirnica):

        if Namirnica in self.namirnice_df.values:
            filtered_df = self.namirnice_df[self.namirnice_df["nazivnamirnice"] == Namirnica]
            kalorije = filtered_df["kalorije"].values[0]
            return("Kalorije za namirnicu {} iznose {} cal.".format(Namirnica.lower(), kalorije))
        else:
            return "Ne postoji odabrana namirnica"

    def ocitaj_kalorije_recept(self, recept):

        NamirnicaX = self.recepti_df.columns[1:len(
            self.recepti_df.columns):3].to_list()
        JedinicaMereX = self.recepti_df.columns[2:len(
            self.recepti_df.columns):3].to_list()
        KolicinaX = self.recepti_df.columns[3:len(
            self.recepti_df.columns):3].to_list()
        Kalorije = []
        Namirnica = []
        Kolicina = []
        JedinicaMere = []
        Kalorijska_vrednost_recepta = 0

        if recept in self.recepti_df["nazivrecepta"].values:

            filtered_row = self.recepti_df.loc[self.recepti_df["nazivrecepta"] == recept].dropna(
                axis=1)
            filtered_row = filtered_row.replace({pd.NA: ''})
            # print(filtered_row)

            for x in NamirnicaX:
                if x in filtered_row:

                    kalorija = (self.namirnice_df.loc[self.namirnice_df["nazivnamirnice"]
                                == filtered_row[x].values[0], "kalorije"]).values[0]
                    Kalorije.append(kalorija)

                    namirnica = filtered_row[x].values[0]
                    Namirnica.append(namirnica)

            for y in KolicinaX:
                if y in filtered_row:
                    kolicina = filtered_row[y].values[0]
                    Kolicina.append(kolicina)

            for z in JedinicaMereX:
                if z in filtered_row:
                    Mera = filtered_row[z].values[0]
                    JedinicaMere.append(Mera)

        vrednosti_df = pd.DataFrame(
            {"Namirnica": Namirnica, "Kolicina": Kolicina, "Kalorije": Kalorije, "Jedinica Mere": JedinicaMere})

        for index, row in vrednosti_df.iterrows():
            if row["Jedinica Mere"] == "komad":
                kalorijska_vrednost = row["Kolicina"] * row["Kalorije"]
                Kalorijska_vrednost_recepta = Kalorijska_vrednost_recepta + kalorijska_vrednost
            elif row["Jedinica Mere"] == "gr":
                kalorijska_vrednost = row["Kolicina"]/100 * row["Kalorije"]
                Kalorijska_vrednost_recepta = Kalorijska_vrednost_recepta + kalorijska_vrednost
        # print("Kalorijska vrednost recepta {} je {} cal.".format(recept.lower(),Kalorijska_vrednost_recepta))
        return Kalorijska_vrednost_recepta

    def ocitaj_kalorije_svi_recepti(self):

        recepti = self.recepti_df["nazivrecepta"]
        recept_list = []
        a = []

        for x in recepti:

            cal = self.ocitaj_kalorije_recept(x)
            a.append(cal)
            recept_list.append(x)

        spisak = pd.DataFrame(
            {"Naziv recepta": recept_list, "Kalorijska vrednost": a})
        return(spisak)

    def plot_kalorije_recepti(self):

        spisak = self.ocitaj_kalorije_svi_recepti()
        names = spisak["Naziv recepta"]
        values = spisak["Kalorijska vrednost"]
        autopct_labels = ["{} ({} cal)".format(name, value)
                          for name, value in zip(names, values)]

        plt.pie(values, labels=autopct_labels, autopct="%1.0f%%")
        plt.title("Kalorijska vrednost recepta")
        plt.show()

    def plot_kalorije_namirnice(self):

        names = self.namirnice_df["nazivnamirnice"]
        values = self.namirnice_df["kalorije"]

        plt.bar(names, values, width=0.2)
        plt.show()

    def export_to_xlsx_namirnice(self):

        columns = ["nazivnamirnice", "kalorije"]
        self.namirnice_df[columns].to_excel("namirnice.xlsx", index=False)

    def export_to_xlsx_recepti(self):

        columns = ["Naziv recepta", "Kalorijska vrednost"]
        self.ocitaj_kalorije_svi_recepti()[columns].to_excel(
            "recepti.xlsx", index=False)

    def auto_box_stampa(self, recept):

        pg1.alert("Kalorijska vrednost recepta {} je {} cal.".format(
            recept, self.ocitaj_kalorije_recept(recept)))

    def auto_box_comfirmation(self):

        return pg1.confirm("This is...")

    def potvrda(self):

        a = self.auto_box_comfirmation()
        if a == "OK":
            return ("Uspesno ste uradili operaciju.")

    def print(self):
        pass


rec = Recepti()
rec.import_from_sql()
rec.lista_svega()
# dffdf
# print(rec.namirnice_df)
# print(rec.kalorije)
# rec.dodaj_namirnicu('Čia Seme','gr',100,372)
# rec.dodaj_namirnicu('Laneno Seme','gr',100,543)
# print(rec.namirnica)
# print(rec.ocitaj_kalorije())

# print(rec.ocitaj_kalorije_recept("Krompir"))
# print(rec.recepti_df)
# print(rec.ocitaj_kalorije_svi_recepti())
# rec.plot_kalorije_recepti()
# # print(rec.ocitaj_kalorije_recept("Gulas"))
# rec.dodaj_recept("Buhtla","Jaja","komad",5,"Krompir","gr",900,"Jogurt","gr",400,"Beli pirinac","gr",1500)
# rec.obrisi_recept("Pihtije")

# rec.plot_kalorije_namirnice()
# rec.export_to_xlsx_recepti()

# rec.auto_box("Gulas")
# rec.auto_box_comfirmation()
# print(rec.potvrda())
rec.list_box_recepti()
print(rec.recepti_df)
