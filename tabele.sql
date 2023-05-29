CREATE TABLE NAMIRNICA (
    NazivNamirnice VARCHAR(20) NOT NULL,
    JedinicaMere VARCHAR(10) NOT NULL,
    KOLICINA INTEGER NOT NULL,
    KALORIJE INTEGER NOT NULL,
    PRIMARY KEY (NazivNamirnice, JedinicaMere)
);

SELECT * FROM NAMIRNICA
SELECT * FROM RECEPT
DROP TABLE RECEPT
DROP TABLE NAMIRNICA

INSERT INTO NAMIRNICA VALUES ('jaja','komad',1,95.1);
INSERT INTO NAMIRNICA VALUES ('Jogurt','gr',100,41);
INSERT INTO NAMIRNICA VALUES ('Feta sir','gr',100,220);
INSERT INTO NAMIRNICA VALUES ('Beli pirinac','gr',100,368);
INSERT INTO NAMIRNICA VALUES ('Žito','gr',100,335);
INSERT INTO NAMIRNICA VALUES ('Proso','gr',100,378);
INSERT INTO NAMIRNICA VALUES ('Krompir','gr',100,77);

CREATE TABLE RECEPT (
    NazivRecepta VARCHAR(20) PRIMARY KEY NOT NULL,
    Namirnica1 VARCHAR(20),
    JedinicaMere1 VARCHAR(10),
    Kolicina1 INTEGER,
    Namirnica2 VARCHAR(20),
    JedinicaMere2 VARCHAR(10),
    Kolicina2 INTEGER,
    Namirnica3 VARCHAR(20),
    JedinicaMere3 VARCHAR(10),
    Kolicina3 INTEGER,
    Namirnica4 VARCHAR(20),
    JedinicaMere4 VARCHAR(10),
    Kolicina4 INTEGER,
    Namirnica5 VARCHAR(20),
    JedinicaMere5 VARCHAR(10),
    Kolicina5 INTEGER,
    Namirnica6 VARCHAR(20),
    JedinicaMere6 VARCHAR(10),
    Kolicina6 INTEGER,
    Namirnica7 VARCHAR(20),
    JedinicaMere7 VARCHAR(10),
    Kolicina7 INTEGER,
    Namirnica8 VARCHAR(20),
    JedinicaMere8 VARCHAR(10),
    Kolicina8 INTEGER,
    Namirnica9 VARCHAR(20),
    JedinicaMere9 VARCHAR(10),
    Kolicina9 INTEGER,
    Namirnica10 VARCHAR(20),
    JedinicaMere10 VARCHAR(10),
    Kolicina10 INTEGER,
    FOREIGN KEY (Namirnica1, JedinicaMere1) REFERENCES NAMIRNICA(NazivNamirnice, JedinicaMere),
    FOREIGN KEY (Namirnica2, JedinicaMere2) REFERENCES NAMIRNICA(NazivNamirnice, JedinicaMere),
    FOREIGN KEY (Namirnica3, JedinicaMere3) REFERENCES NAMIRNICA(NazivNamirnice, JedinicaMere),
    FOREIGN KEY (Namirnica4, JedinicaMere4) REFERENCES NAMIRNICA(NazivNamirnice, JedinicaMere),
    FOREIGN KEY (Namirnica5, JedinicaMere5) REFERENCES NAMIRNICA(NazivNamirnice, JedinicaMere),
    FOREIGN KEY (Namirnica6, JedinicaMere6) REFERENCES NAMIRNICA(NazivNamirnice, JedinicaMere),
    FOREIGN KEY (Namirnica7, JedinicaMere7) REFERENCES NAMIRNICA(NazivNamirnice, JedinicaMere),
    FOREIGN KEY (Namirnica8, JedinicaMere8) REFERENCES NAMIRNICA(NazivNamirnice, JedinicaMere),
    FOREIGN KEY (Namirnica9, JedinicaMere9) REFERENCES NAMIRNICA(NazivNamirnice, JedinicaMere),
    FOREIGN KEY (Namirnica10, JedinicaMere10) REFERENCES NAMIRNICA(NazivNamirnice, JedinicaMere)
);