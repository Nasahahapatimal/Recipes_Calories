import psycopg2 as pg
import pandas as pd

class Recepti:

    def __init__(self):
        
        self.con = pg.connect(database = 'Recepti',
                              user = 'postgres',
                              password = 'admin',
                              host = 'localhost',
                              port = '5432')
        
        self.namirnice_df = None
        self.recepti_df = None
        self.namirnica = None
        self.kalorije = None
        
    def import_from_sql (self):
        
        self.namirnice_df = pd.read_sql_query('SELECT * FROM NAMIRNICA',self.con)
        self.recepti_df = pd.read_sql_query('SELECT * FROM RECEPT',self.con)

    def lista_svega(self):
        
        self.namirnica = self.namirnice_df.iloc[:,0].to_list()
        self.kalorije = self.namirnice_df.iloc[:,3].to_list()
    
    def dodaj_namirnicu(self,NazivNamirnice,JedinicaMere,Kolicina,Kalorije):

        cursor = self.con.cursor()
        nam = "INSERT INTO NAMIRNICA(NazivNamirnice,JedinicaMere,Kolicina,Kalorije) VALUES ('{}','{}',{},{})".format(NazivNamirnice.capitalize(),JedinicaMere.lower(),Kolicina,Kalorije)
        cursor.execute(nam)
        self.con.commit()
        cursor.close()

    def dodaj_recept(self, NazivRecepta, *values):
        
        cursor = self.con.cursor()
        rec = "INSERT INTO RECEPT(NazivRecepta) VALUES ('{}')".format(NazivRecepta)
        cursor.execute(rec)
        self.con.commit()

        attribute_names = ['Namirnica', 'JedinicaMere', 'Kolicina']

        for index, value in enumerate(values, start=1):
            attribute_name = attribute_names[index % len(attribute_names) - 1] + str((index + 2) // 3)
            update_query = "UPDATE RECEPT SET {} = '{}' WHERE NazivRecepta = '{}'".format(attribute_name, value, NazivRecepta)
            cursor.execute(update_query)
            self.con.commit()

        cursor.close()

        return "Recept uspesno dodat!"

    def obrisi_namirnicu(self,namirnica):

        cursor = self.con.cursor()
        del_nam = "DELETE FROM NAMIRNICA WHERE NazivNamirnice = '{}'".format(namirnica.capitalize())
        cursor.execute(del_nam)
        self.con.commit()
        cursor.close()

        return "Namirnica uspeno obrisana!"
    
    def obrisi_recept(self,NazivRecepta):
        
        cursor = self.con.cursor()
        del_rec = "DELETE FROM RECEPT WHERE NazivRecepta = '{}'".format(NazivRecepta.capitalize())
        cursor.execute(del_rec)
        self.con.commit()
        cursor.close()
        return "Recept uspeno obrisan!"

    def ocitaj_kalorije_sve_namirnice(self):

        return self.namirnice_df.iloc[0:][["nazivnamirnice","kalorije"]].to_string(index=False,header=False)
    
    def ocitaj_kalorije_namirnica(self,Namirnica):

        if Namirnica in self.namirnice_df.values:
            filtered_df = self.namirnice_df[self.namirnice_df["nazivnamirnice"] == Namirnica]
            kalorije = filtered_df["kalorije"].values[0]
            return("Kalorije za namirnicu {} iznose {} cal.".format(Namirnica.lower(),kalorije))
        else:
            return "Ne postoji odabrana namirnica"
    
    def ocitaj_kalorije_recept(self,recept):

        NamirnicaX = self.recepti_df.columns[1:len(self.recepti_df.columns):3].to_list()
        KolicinaX = self.recepti_df.columns[3:len(self.recepti_df.columns):3].to_list()
        Kalorije = []

        if recept in self.recepti_df["nazivrecepta"].values:
            
            filtered_row = self.recepti_df.loc[self.recepti_df["nazivrecepta"] == recept].dropna(axis=1)
            filtered_row = filtered_row.replace({pd.NA: ''})
            print(filtered_row)

            for x in NamirnicaX:
                if x in filtered_row:
                        kalorija = (self.namirnice_df.loc[self.namirnice_df["nazivnamirnice"] == filtered_row[x].values[0],"kalorije"]).values[0]
                        Kalorije.append(kalorija)
                        #dodaj sada i za količinu i to sve stavi u jednu pandu i pomnoži.
                        #za sve ostale recepte umesto (self,recept) ---- (self,lista svih recepata - izvuci iz funkcije)

        return(Kalorije)


rec = Recepti()
rec.import_from_sql()
# rec.lista_svega()
#dffdf
# print(rec.namirnica)
# print(rec.kalorije)
# rec.dodaj_namirnicu('Čia Seme','gr',100,372)
# rec.dodaj_namirnicu('Laneno Seme','gr',100,543)
# print(rec.namirnica)
# print(rec.ocitaj_kalorije())

# print(rec.ocitaj_kalorije_recept("Krompir"))
# print(rec.recepti_df)
print(rec.ocitaj_kalorije_recept("Gulas"))
# rec.dodaj_recept("Gulas","Jaja","komad",10,"Krompir","gr",880)