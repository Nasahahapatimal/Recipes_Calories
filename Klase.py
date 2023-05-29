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
        nam = "INSERT INTO NAMIRNICA(NazivNamirnice,JedinicaMere,Kolicina,Kalorije) VALUES ('{}','{}',{},{})".format(NazivNamirnice,JedinicaMere,Kolicina,Kalorije)
        cursor.execute(nam)
        self.con.commit()
        cursor.close()

    def dodaj_recept(self):
        pass

    def ocitaj_kalorije(self):
        return self.namirnice_df.iloc[0:][["nazivnamirnice","kalorije"]].to_string(index=False,header=False)


rec = Recepti()
rec.import_from_sql()

print(rec.namirnice_df)
# print(rec.recepti_df)
rec.lista_svega()
print(rec.namirnica)
print(rec.kalorije)
# rec.dodaj_namirnicu('Čia Seme','gr',100,372)
# rec.dodaj_namirnicu('Laneno Seme','gr',100,543)
print(rec.namirnica)
print(rec.ocitaj_kalorije())