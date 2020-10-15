# Standard Imports
import sqlite3
import sys
import os
import os
import sys

# Gets the OS running the program
osType = sys.platform
if osType.startswith('linux'):
    path = '/'
elif osType.startswith('win32') or osType.startswith('cygwin'):
    path = '\\'
elif osType.startswith('darwin'):
    path = '/'
else:
    sys.exit()

# Gets the actual WORKING directory
workingDirectory = os.getcwd()
dbPath = workingDirectory + path +'DB'
uiPath = workingDirectory + path +'UI'
accessPath = workingDirectory + path + 'Access'
sys.path.append(dbPath)
sys.path.append(uiPath)

# from commands_db import Query, Search


# Gets the OS running the program
osType = sys.platform
if osType.startswith('linux'):
    path = '/'
elif osType.startswith('win32') or osType.startswith('cygwin'):
    path = '\\'
elif osType.startswith('darwin'):
    path = '/'
else:
    sys.exit()

# Gets the actual WORKING directory
workingDirectory = os.getcwd()
dbPath = os.path.join(workingDirectory, 'project.db')

conn = sqlite3.connect(dbPath)
c = conn.cursor()

# Creates DB + Tables
def CreateDB():
    global c

    # Creates main tables
    c.execute('''CREATE TABLE Product
                (pro_id INTEGER PRIMARY KEY NOT NULL,
                pro_name TEXT NOT NULL)''')

    c.execute('''CREATE TABLE Category
				(cat_id INTEGER PRIMARY KEY NOT NULL,
			 	cat_name TEXT NOT NULL)''')

    c.execute('''CREATE TABLE Brand
				(bra_id INTEGER PRIMARY KEY NOT NULL,
				bra_name TEXT NOT NULL)''')

    c.execute('''CREATE TABLE Model
				(mod_id INTEGER PRIMARY KEY NOT NULL,
				mod_name TEXT NOT NULL,
                mod_factoryName TEXT,
                mod_startYear INTEGER NOT NULL,
                mod_finishYear INTEGER)''')

    c.execute('''CREATE TABLE Version
				(ver_id INTEGER PRIMARY KEY NOT NULL,
				ver_name TEXT NOT NULL,
				ver_fuel TEXT NOT NULL,
				ver_engineSize INTEGER NOT NULL,
				ver_doors INTEGER,
				ver_seats INTEGER NOT NULL,
				ver_horsepower INTEGER NOT NULL,
				ver_weigth INTEGER,
				ver_price REAL NOT NULL)''')

    # Creates middle tables
    c.execute('''CREATE TABLE ProCat
                (product_id INTEGER NOT NULL,
                category_id INTEGER NOT NULL,
                PRIMARY KEY(product_id, category_id))''')
    
    c.execute('''CREATE TABLE CatBra
                (category_id INTEGER NOT NULL,
                brand_id INTEGER NOT NULL,
                PRIMARY KEY(category_id, brand_id))''')

    c.execute('''CREATE TABLE BraMod
                (brand_id INTEGER NOT NULL,
                model_id INTEGER NOT NULL,
                PRIMARY KEY(brand_id, model_id))''')

    c.execute('''CREATE TABLE ModVer
                (model_id INTEGER NOT NULL,
                version_id INTEGER NOT NULL,
                PRIMARY KEY(model_id, version_id))''')

    c.execute('''CREATE TABLE CatMod
                (category_id INTEGER NOT NULL,
                model_id INTEGER NOT NULL,
                PRIMARY KEY(category_id, model_id))''')


def FillsProductDB():
    global c, conn
    
    c.execute("INSERT INTO Product(pro_name) VALUES ('AUTOM - AUTOMÓVEL')")
    c.execute("INSERT INTO Product(pro_name) VALUES ('AUT2R - AUTOMÓVEL 2 RODAS')")
    conn.commit()

def FillsCategoryDB():
    global c, conn

    # Fills 1 ROW of Category table
    c.execute("INSERT INTO Category(cat_name) VALUES ('Ambulância Ligeiro')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Ambulância Pesado')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Autocarro até 20 lugares')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Autocarro com mais de 20 lugares')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Auto-caravana/Vivenda-Ligeiro')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Camião até 20Ton.PB')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Camião com mais de 20Ton.PB')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Ciclomotor')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Empilhador Máquina Industrial')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Guindaste Automóvel')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Higiene Urbana')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Ligeiro Bombeiros')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Ligeiro Instrução')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Ligeiro Mercadorias')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Ligeiro Passageiros/Aluguer')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Máquina de Construção Cívil')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Motociclo')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Motociclo/Ciclomotor Instrução')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Motocult/Maq Agr/Trat Agr <25HP')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Nupcial e Funerário')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Pesado Bombeiros')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Pesado de Instrução')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Pronto Socorro Ligeiro')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Pronto Socorro Pesado')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Reboque Agricola')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Roboque Além de 2500KG/PB')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Reboque <300KG/PB ou s/Prémio')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Velocipede')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Veículo Articulado')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Táxi')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Tracção Animal')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Trator Industrial')")
    c.execute(
        "INSERT INTO Category(cat_name) VALUES ('Trator Agricola mais de 25 HP')")
    c.execute("INSERT INTO Category(cat_name) VALUES ('Turistico da Madeira')")

    conn.commit()


def FillsBrandDB():
    global c, conn

    c.execute("INSERT INTO Brand(bra_name) VALUES ('Alfa Romeo')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Aston Martin')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Audi')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Bentley')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('BMW')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Bugatti')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Cadillac')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Chevrolet')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Chrysler')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Citroen')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Dodge')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Ferrari')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Fiat')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Ford')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Honda')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Hyundai')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Jaguar')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Jeep')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Kawasaki')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Kia')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Lamborghini')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Land Rover')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Lexus')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Maserati')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Mazda')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('McLaren')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Mercedes-Benz')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Mini')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Mitsubishi')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Nissa')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Peugeot')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Porsche')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Ram')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Renault')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Rolls Royce')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Saab')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Seat')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Subaru')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Tesla')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Toyota')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Volswagen')")
    c.execute("INSERT INTO Brand(bra_name) VALUES ('Volvo')")

    conn.commit()


def FillsModelDB():
    global c, conn

    modelsCarBMW = [('Serie-1', 'F40', 2019, None),
                    ('Serie-1 Diesel', 'F40', 2019, None)]

    modelsCarFerrari = [('488', None, 2015, None),
                        ('488 Spider', None, 2015, None),
                        ('LaFerrari', None, 2013, 2016),
                        ('LaFerrari Aperta', None, 2016, 2018),
                        ('F8 Tributo', None, 2020, None),
                        ('Portofino', None, 2017, None),
                        ('812 Superfast', None, 2017, None),
                        ('812 GTS', None, 2018, None),
                        ('GTC4Lusso T', None, 2016, None),
                        ('SF90 Stradale', None, 2019, None),
                        ('Roma', None, 2020, None),
                        ('458', None, 2009, 2015),
                        ('458 Spider', None, 2011, 2015),
                        ('FF', None, 2011, 2016),
                        ('F12 Berlinetta', None, 2012, 2017),
                        ('California', None, 2007, 2015),
                        ('California T', None, 2013, None),
                        ('F430', None, 2005, 2014),
                        ('F430 Spider', None, 2005, 2012),
                        ('599GTB', None, 2005, 2014),
                        ('599GTO', None, 2010, 2014),
                        ('Monza', None, 2019, None),
                        ('Enzo', None, 2002, 2004),
                        ('612 Scaglietii', None, 2004, 2014),
                        ('575M Maranello', None, 2002, 2009),
                        ('456', None, 1998, 2004),
                        ('550', None, 1996, 2004),
                        ('360 Modena', None, 1999, 2004),
                        ('360 Modena Spider', None, 1999, 2004),
                        ('360 Challange Stradale', None, 1999, 2004)]

    modelsCarLamborghini = [('Diablo', None, 1990, 2001),
                            ('Murciélago', None, 2001, 2006),
                            ('Murciélago Roadster', None, 2004, 2006),
                            ('Gallardo', None, 2003, 2013),
                            ('Gallardo Spyder', None, 2003, 2013),
                            ('Reventón', None, 2008, 2010),
                            ('Sesto Elemento', None, 2012, 2012),
                            ('Veneno', None, 2013, 2014),
                            ('Centenario', None, 2016, 2017),
                            ('Aventador', None, 2011, None),
                            ('Aventador Roadster', None, 2011, None),
                            ('Aventador Spyder', None, 2011, None),
                            ('Huracán', None, 2014, None),
                            ('Huracán Spyder', None, 2014, None),
                            ('Urus', None, 2018, None)]

    modelsCarRenault = [('Captur', None, 2013, None),
                        ('Captur Diesel', None, 2013, None),
                        ('Clio IV', None, 2012, 2019),
                        ('Clio IV Société Fase II Diesel', None, 2012, 2019)]

    modelsMotoBMW = [('C 650 GT', None, 2012, None),
                     ('F 700 GS', None, 2012, None),
                     ('G 310 R', None, 2018, None),
                     ('R 1200 R', None, 2006, None),
                     ('R 1200 RS', None, 2015, None),
                     ('R 1250 GS', None, 2019, None),
                     ('R 1250 GS Adventure', None, 2019, None),
                     ('R 1250 RT', None, 2019, None),
                     ('S 1000 R', None, 2014, None),
                     ('S 1000 RR', None, 2009, 2014),
                     ('S 1000 XR', None, 2015, None)]

    modelsMotoKawasaki = [('ZZR 1400 Performace', None, 2006, 2015),
                          ('GTR 1400 ABS', None, 2007, None)]

    modelsTratorLamborghini = [('Nitro 100', None, 2020, None),
                               ('Nitro 110', None, 2020, None),
                               ('Nitro 120', None, 2020, None),
                               ('Nitro 100 VRT', None, 2020, None),
                               ('Nitro 110 VRT', None, 2020, None),
                               ('Nitro 120 VRT', None, 2020, None),
                               ('Nitro 130 VRT', None, 2020, None)]

    c.executemany(
        'INSERT INTO Model(mod_name, mod_factoryName, mod_startYear, mod_finishYear) VALUES(?,?,?,?);', modelsCarBMW)
    c.executemany(
        'INSERT INTO Model(mod_name, mod_factoryName, mod_startYear, mod_finishYear) VALUES(?,?,?,?);', modelsCarFerrari)
    c.executemany(
        'INSERT INTO Model(mod_name, mod_factoryName, mod_startYear, mod_finishYear) VALUES(?,?,?,?);', modelsCarLamborghini)
    c.executemany(
        'INSERT INTO Model(mod_name, mod_factoryName, mod_startYear, mod_finishYear) VALUES(?,?,?,?);', modelsCarRenault)
    c.executemany(
        'INSERT INTO Model(mod_name, mod_factoryName, mod_startYear, mod_finishYear) VALUES(?,?,?,?);', modelsMotoBMW)
    c.executemany(
        'INSERT INTO Model(mod_name, mod_factoryName, mod_startYear, mod_finishYear) VALUES(?,?,?,?);', modelsMotoKawasaki)
    c.executemany(
        'INSERT INTO Model(mod_name, mod_factoryName, mod_startYear, mod_finishYear) VALUES(?,?,?,?);', modelsTratorLamborghini)

    conn.commit()


def FillsVehicleDB():
    global c, conn

    vehicleCarBMW = [('118 i Auto', 'Gasolina', 1499, 5, 5, 140, 1870, 32395.00),
                     ('118 i Line Luxury Auto', 'Gasolina',
                      1499, 5, 5, 140, 1870, 35563.00),
                     ('118 i Line Sport Auto', ' Gasolina',
                      1499, 5, 5, 140, 1870, 34763.00),
                     ('118 i Pack M Auto', 'Gasolina',
                      1499, 5, 5, 140, 1870, 36263.00),
                     ('M135 i xDrive', 'Gasolina', 1998, 5, 5, 306, 2085, 60495.00),
                     ('116 d', 'Diesel', 1496, 5, 5, 116, 1940, 30495.00),
                     ('116 d Advantage', 'Diesel', 1496, 5, 5, 116, 1940, 31121.00),
                     ('116 d Advantage Auto', 'Diesel',
                      1496, 5, 5, 116, 1940, 33266.00),
                     ('116 d Auto', 'Diesel', 1496, 5, 5, 116, 1940, 32517.00),
                     ('116 d Line Luxury', 'Diesel',
                      1496, 5, 5, 116, 1940, 35047.00),
                     ('116 d Line Luxury Auto', 'Diesel',
                      1496, 5, 5, 116, 1940, 37254.00),
                     ('118 d Pack M', 'Diesel', 1995, 5, 5, 150, 1980, 42933.00)]

    vehicleCarFerrari = [('488 GTB', 'Gasolina', 3902, 2, 2, 670, 1475, 265733.00),
                         ('488 GTB', 'Gasolina', 3902, 2, 2, 670, 1475, 276673.00),
                         ('488 Pista', 'Gasolina', 3902,
                          2, 2, 720, 1460, 341469.00),
                         ('488 Pista Spider', 'Gasolina',
                          3902, 2, 2, 720, 1560, 373719.00),
                         ('488 Spider', 'Gasolina', 3902,
                          2, 2, 670, 1600, 302328.00),
                         ('488 Spider', 'Gasolina', 3902,
                          2, 2, 670, 1525, 290640.00),
                         ('La Ferrari', 'Gasolina', 6262,
                          2, 4, 963, 1400, 1271667.00),
                         ('F8 Tributo', 'Gasolina', 3902,
                          2, 2, 720, 1560, 284864.00),
                         ('Portofino', 'Gasolina', 3855,
                          2, 4, 600, 1740, 237216.00),
                         ('Monza SP1', 'Gasolina', 6496,
                          1, 1, 810, 1705, 1691824.00),
                         ('Monza SP2', 'Gasolina', 6496,
                          2, 2, 810, 1705, 1691824.00),
                         ('812 Superfast', 'Gasolina',
                          6496, 2, 2, 800, 1705, 380249.00),
                         ('California T', 'Gasolina', 3855,
                          2, 4, 560, 1730, 233319.00),
                         ('California T Hele', 'Gasolina',
                          3855, 2, 4, 560, 1730, 231347.00),
                         ('California', 'Gasolina', 4297,
                          2, 4, 490, 1735, 232755.00),
                         ('California Hele', 'Gasolina',
                          4297, 2, 4, 490, 1735, 227487.00),
                         ('F12 Hele', 'Gasolina', 6262,
                          2, 2, 740, 1630, 357551.00),
                         ('F12 tdf Hele', 'Gasolina', 6262,
                          2, 2, 780, 1520, 472583.00),
                         ('FF', 'Gasolina', 6262, 2, 4, 660, 1905, 343816.00),
                         ('FF Hele', 'Gasolina', 6262, 2, 4, 660, 1905, 348372.00),
                         ('GTC4Lusso', 'Gasolina', 6262,
                          2, 4, 690, 1920, 348755.00),
                         ('GTC4Lusso', 'Gasolina', 6262,
                          2, 4, 690, 1995, 348297.00),
                         ('GTC4Lusso T', 'Gasolina', 3855,
                          2, 4, 610, 1970, 277502.00),
                         ('GTC4Lusso T', 'Gasolina', 6262,
                          2, 4, 610, 1970, 280704.00),
                         ('458 Italia', 'Gasolina', 4497,
                          2, 2, 570, 1650, 260799.00),
                         ('458 Italia Hele', 'Gasolina',
                          4497, 2, 2, 570, 1650, 253793.00),
                         ('458 Speciale', 'Gasolina', 4497,
                          2, 2, 605, 1395, 244585.00),
                         ('458 Speciale A', 'Gasolina',
                          4497, 2, 2, 605, 1445, 320502.00),
                         ('458 Speciale A Hele', 'Gasolina',
                          4497, 2, 2, 605, 1445, 313496.00),
                         ('458 Speciale Hele', 'Gasolina',
                          4497, 2, 2, 605, 1395, 288258.00),
                         ('458 Spider', 'Gasolina', 4497,
                          2, 2, 570, 1535, 283955.00),
                         ('458 Spider Hele', 'Gasolina',
                          4497, 2, 2, 570, 1535, 276949.00),
                         ('599 GTB F1 Fiorano', 'Gasolina',
                          5999, 2, 2, 620, 1690, 339043.00),
                         ('599 GTB Fiorano', 'Gasolina',
                          5999, 2, 2, 620, 1690, 331540.00),
                         ('599 GTO F1', 'Gasolina', 5999,
                          2, 2, 670, 1605, 400525.00),
                         ('612 Scaglietti One To One', 'Gasolina',
                          5748, 2, 2, 540, 1875, 360353.00),
                         ('612 Scaglietti', 'Gasolina',
                          5748, 2, 2, 540, 1840, 298581.00),
                         ('612 Scaglietti F1', 'Gasolina',
                          5748, 2, 2, 540, 1840, 345650.00),
                         ('F430 Challenge F1', 'Gasolina',
                          4308, 2, 2, 490, 1720, 298317.00),
                         ('F430 Scuderia', 'Gasolina',
                          4308, 2, 2, 510, 1620, 270453.00),
                         ('F430 Spider', 'Gasolina', 4308,
                          2, 2, 490, 1720, 247213.00),
                         ('F430 Spider F1', 'Gasolina',
                          4308, 2, 2, 490, 1720, 254289.00),
                         ('F430 Spider Scuderia 16M', 'Gasolina',
                          4308, 2, 2, 510, 1640, 319902.00),
                         ('575M Maranello', 'Gasolina',
                          5748, 2, 2, 515, 1950, 249422.00),
                         ('575M Maranello F1', 'Gasolina',
                          5748, 2, 2, 515, 1950, 258403.00),
                         ('360 Challenge', 'Gasolina',
                          3586, 2, 2, 400, 1580, 199359.00),
                         ('360 Modena', 'Gasolina', 3586,
                          2, 2, 400, 1700, 161746.00),
                         ('360 Modena F1', 'Gasolina',
                          3586, 2, 2, 400, 1700, 170017.00),
                         ('360 Modena Spider', 'Gasolina',
                          3586, 2, 2, 400, 1700, 180295.00),
                         ('360 Modena Spider F1', 'Gasolina',
                          3586, 2, 2, 400, 1700, 188566.00),
                         ('550 Maranello', 'Gasolina',
                          5474, 2, 2, 485, 1950, 225027.00),
                         ('456 M GT', 'Gasolina', 5474,
                          2, 4, 442, 2200, 243664.00),
                         ('456 M GTA', 'Gasolina', 5474, 2, 4, 442, 2250, 255371.00)]

    vehicleCarLamborghini = [('Aventador 6.5 V12 LP740-4 S', 'Gasolina', 6498, 2, 2, 740, 2025, 450152.00),
                             ('Aventador S', 'Gasolina', 6498,
                              2, 2, 740, 2025, 509529.00),
                             ('Aventador 6.5 V12 LP740-4 S', 'Gasolina',
                              6498, 2, 2, 740, 2025, 491236.00),
                             ('Huracán 5.2 V10 LP Performance', 'Gasolina',
                              5204, 2, 2, 640, None, 292104.00),
                             ('Huracán 5.2 V10 LP580-2', 'Gasolina',
                              5204, 2, 2, 580, 1518, 245670.00),
                             ('Huracán 5.2 V10 LP610-4', 'Gasolina',
                              5204, 2, 2, 610, 1551, 273727.00),
                             ('Huracán EVO', 'Gasolina', 5204,
                              2, 2, 640, 2000, 298086.00),
                             ('Huracán 5.2 V10 LP580-2', 'Gasolina',
                              5204, 2, 2, 580, 1509, 265042.00),
                             ('Huracán 5.2 V10 LP610-4', 'Gasolina',
                              5204, 2, 2, 610, 1671, 295618.00),
                             ('Huracán EVO', 'Gasolina', 5204,
                              2, 2, 640, 2120, 323225.00),
                             ('Urus 4.0 V8', 'Gasolina', 3996,
                              5, 5, 650, 2200, 268570.00),
                             ('Urus 4.0 V8', 'Gasolina', 3996,
                              5, 5, 650, 2200, 272915.00),
                             ('Aventador 6.5 V12 LP700-4', 'Gasolina',
                              6498, 2, 2, 700, 2075, 417196.00),
                             ('Aventador 6.5 V12 LP700-4 Pire', 'Gasolina',
                              6498, 2, 2, 700, 2075, 431285.00),
                             ('Aventador 6.5 V12 LP750-4 SV', 'Gasolina',
                              6498, 2, 2, 750, 2025, 493303.00),
                             ('Aventador 6.5 V12 LP700-4', 'Gasolina',
                              6498, 2, 2, 700, 2125, 454935.00),
                             ('Aventador 6.5 V12 LP750-4 SV', 'Gasolina',
                              6498, 2, 2, 750, 2075, 531419.00),
                             ('Huracán 5.2 V10 LP610-4 Avio', 'Gasolina',
                              5204, 2, 2, 610, 1551, 271189.00),
                             ('Gallardo 5.2 V10 LP560-4', 'Gasolina',
                              5204, 2, 2, 560, 2000, 244693.00),
                             ('Aventador 6.5 V12 LP720-4', 'Gasolina',
                              6498, 2, 2, 720, 2075, 493825.00),
                             ('Aventador 6.5 V12 LP720-4', 'Gasolina',
                              6498, 2, 2, 720, 2125, 540621.00),
                             ('Gallardo 5.2 V10 LP550-2', 'Gasolina',
                              5204, 2, 2, 550, 1650, 214698.00),
                             ('Gallardo 5.2 V10 LP560-4 Bicol', 'Gasolina',
                              5204, 2, 2, 560, 1910, 244176.00),
                             ('Gallardo 5.2 V10 LP570-4 Strad', 'Gasolina',
                              5204, 2, 2, 570, 1840, 289504.00),
                             ('Gallardo 5.2 V10 LP570-4 Super', 'Gasolina',
                              5204, 2, 2, 570, 1840, 275667.00),
                             ('Gallardo Spyder 5.2 V10 LP550-', 'Gasolina',
                              5204, 2, 2, 550, 1790, 241953.00),
                             ('Gallardo Spyder 5.2 V10 LP560-', 'Gasolina',
                              5204, 2, 2, 560, 1770, 260333.00),
                             ('Gallardo Spyder 5.2 V10 LP570-', 'Gasolina',
                              5204, 2, 2, 570, 1985, 286569.00),
                             ('Gallardo 5.2 V10 LP550-2 Valen', 'Gasolina',
                              5204, 2, 2, 550, 1650, 249764.00),
                             ('Gallardo 5.0 V10 Superleggera', 'Gasolina',
                              4961, 2, 2, 530, 1830, 248475.00),
                             ('Gallardo Spyder 5.0 V10', 'Gasolina',
                              4961, 2, 2, 520, 1840, 237895.00),
                             ('Murciélago 6.5 V12 LP640', 'Gasolina',
                              6496, 2, 2, 640, 1950, 383979.00),
                             ('Murciélago Roadster 6.5 V12 LP', 'Gasolina',
                              6496, 2, 2, 640, 1950, 413232.00),
                             ('Gallardo 5.0 V10', 'Gasolina',
                              4961, 2, 2, 500, 1700, 210530.00),
                             ('Murciélago 6.2 V12', 'Gasolina',
                              6192, 2, 2, 580, 1950, 295711.00),
                             ('Murciélago Roadster 6.2 V12', 'Gasolina',
                              6192, 2, 2, 580, 1950, 319306.00),
                             ('Gallardo 5.0 V10 S6', 'Gasolina', 4961, 2, 2, 500, 1700, 200426.00)]

    vehicleCarRenault = [('Captur 0.9 TCE Helly Hansen', 'Gasolina', 898, 5, 5, 90, 1658, 19880.00),
                         ('Captur 0.9 TCe Exclusive', 'Gasolina',
                          898, 5, 5, 90, 1671, 20200.00),
                         ('Captur 1.2 TCe Initiale Paris', 'Gasolina',
                          1197, 5, 5, 120, 1727, 24400.00),
                         ('Captur 1.2 TCe Initiale Paris', 'Gasolina',
                          1197, 5, 5, 120, 1744, 25900.00),
                         ('Captur 1.5 dCi Zen', 'Diesel',
                          1461, 5, 5, 90, 1755, 22450.00),
                         ('Captur 1.5 dCi Sport EDC', 'Diesel',
                          1461, 5, 5, 90, 1763, 22800.0),
                         ('Captur 1.5 dCi Sport EDC', 'Diesel',
                          1461, 5, 5, 90, 1759, 23680.00),
                         ('Clio 0.9 TCE Confort', 'Gasolina',
                          898, 5, 5, 90, 1588, 14210.00),
                         ('Clio 0.9 TCE GT Line', 'Gasolina',
                          898, 5, 5, 90, 1600, 17280.00),
                         ('Clio 1.6 T RS EDC', 'Gasolina',
                          1618, 5, 5, 200, 1711, 29890.00),
                         ('Clio 1.6 T RS Trophy EDC', 'Gasolina',
                          1618, 5, 5, 220, 1711, 31550.00),
                         ('Clio 1.5 dCi Intens', 'Diesel',
                          1461, 5, 2, 90, 1670, 24592.00),
                         ('Clio 1.5 dCi Itens', 'Diesel',
                          1461, 5, 2, 90, 1700, 24848.00),
                         ('Clio 1.5 dCi Zen', 'Diesel',
                          1461, 5, 2, 75, 1670, 21898.00),
                         ('Clio 1.5 dCi Zen', 'Diesel', 1461, 5, 2, 75, 1683, 22139.00)]

    vehicleMotoBMW = [('C 650 GT Scooter', 'Gasolina', 647, None, 2, 60, 0, 12103.00),
                      ('G 310 R Utilitaria', 'Gasolina',
                       313, None, 2, 34, 0, 5520.00),
                      ('R 1200 R Utilitaria', 'Gasolina',
                       1170, None, 2, 125, 0, 14093.00),
                      ('R 1200 RS Utilitaria', 'Gasolina',
                       1170, None, 2, 125, 0, 14793.00),
                      ('R 1250 GS Trail', 'Gasolina',
                       1254, None, 2, 136, 0, 17746.00),
                      ('R 1250 GS Adventure Trail', 'Gasolina',
                       1254, None, 2, 136, 0, 19056.00),
                      ('R 1250 RT Turismo', 'Gasolina',
                       1254, None, 2, 136, 0, 19116.00),
                      ('S 1000 R Sport', 'Gasolina',
                       999, None, 2, 160, 0, 14248.00),
                      ('S 1000 RR Sport', 'Gasolina',
                       999, None, 2, 199, 0, 18400.00),
                      ('S 1000 XR', 'Gasolina', 999, None, 2, 160, 0, 16799.00)]

    vehicleMotoKawasaki = [('ZZR 1400 Sport', 'Gasolina', 1441, None, 2, 210, 0, 21590.00),
                           ('GTR 1400 ABS Turismo', 'Gasolina', 1352, None, 2, 160, 0, 17980.00)]

    vehicleTratorLamborghini = [('Nitro 100', ' Diesel', 3620, 2, 1, 99, 4500, 94600),
                                ('Nitro 110', 'Diesel', 3620,
                                 2, 1, 110, 4600, 94600),
                                ('Nitro 120', 'Diesel', 3620,
                                 2, 1, 118, 4900, 94600),
                                ('Nitro 100 VRT', 'Diesel',
                                 3620, 2, 1, 99, 4900, 146000),
                                ('Nitro 110 VRT', 'Diesel',
                                 3620, 2, 1, 110, 4350, 146000),
                                ('Nitro 120 VRT', 'Diesel',
                                 3620, 2, 1, 118, 4600, 146000),
                                ('Nitro 130 VRT', 'Diesel', 3620, 2, 1, 127, 4900, 146000)]

    c.executemany(
        'INSERT INTO Version(ver_name, ver_fuel, ver_engineSize, ver_doors, ver_seats, ver_horsepower, ver_weigth, ver_price) VALUES(?,?,?,?,?,?,?,?);', vehicleCarBMW)
    c.executemany(
        'INSERT INTO Version(ver_name, ver_fuel, ver_engineSize, ver_doors, ver_seats, ver_horsepower, ver_weigth, ver_price) VALUES(?,?,?,?,?,?,?,?);', vehicleCarFerrari)
    c.executemany(
        'INSERT INTO Version(ver_name, ver_fuel, ver_engineSize, ver_doors, ver_seats, ver_horsepower, ver_weigth, ver_price) VALUES(?,?,?,?,?,?,?,?);', vehicleCarLamborghini)
    c.executemany(
        'INSERT INTO Version(ver_name, ver_fuel, ver_engineSize, ver_doors, ver_seats, ver_horsepower, ver_weigth, ver_price) VALUES(?,?,?,?,?,?,?,?);', vehicleCarRenault)
    c.executemany(
        'INSERT INTO Version(ver_name, ver_fuel, ver_engineSize, ver_doors, ver_seats, ver_horsepower, ver_weigth, ver_price) VALUES(?,?,?,?,?,?,?,?);', vehicleMotoBMW)
    c.executemany(
        'INSERT INTO Version(ver_name, ver_fuel, ver_engineSize, ver_doors, ver_seats, ver_horsepower, ver_weigth, ver_price) VALUES(?,?,?,?,?,?,?,?);', vehicleMotoKawasaki)
    c.executemany(
        'INSERT INTO Version(ver_name, ver_fuel, ver_engineSize, ver_doors, ver_seats, ver_horsepower, ver_weigth, ver_price) VALUES(?,?,?,?,?,?,?,?);', vehicleTratorLamborghini)
    conn.commit()

def FillsProCatTable():
    global c, conn
    values = [(1,1),
    (1,2),
    (1,3),
    (1,4),
    (1,5),
    (1,6),
    (1,7),
    (1,9),
    (1,10),
    (1,11),
    (1,12),
    (1,13),
    (1,14),
    (1,15),
    (1,16),
    (1,20),
    (1,21),
    (1,22),
    (1,23),
    (1,24),
    (1,25),
    (1,26),
    (1,27),
    (1,29),
    (1,30),
    (1,31),
    (1,32),
    (1,33),
    (1,34),
    # Motos
    (2,8),
    (2,17),
    (2,18),
    (2,28)]

    c.executemany(
        'INSERT INTO ProCat(product_id, category_id) VALUES(?,?);', values)
    conn.commit()

def FillsCatBraTable():
    global c, conn
    values = [(13, 5),
              (13, 12),
              (13, 21),
              (13, 34),
              # LM
              (14, 34),
              # LP
              (15, 5),
              (15, 12),
              (15, 21),
              (15, 34),
              # MOTO
              (17, 5),
              (17, 19),
              # Moto de Instr
              (18, 5),
              (18, 19),
              # Táxi
              (30, 5),
              (30, 12),
              (30, 21),
              (30, 34),
              # Tractor
              (32, 21)]

    c.executemany(
        'INSERT INTO CatBra(category_id, brand_id) VALUES(?,?);', values)
    conn.commit()


def FillsBraModTable():
    global c, conn
    values = [(5, 1),
              (5, 2),
              (5, 52),
              (5, 53),
              (5, 54),
              (5, 55),
              (5, 56),
              (5, 57),
              (5, 58),
              (5, 59),
              (5, 60),
              (5, 61),
              (5, 62),
              # Ferrari
              (12, 3),
              (12, 4),
              (12, 5),
              (12, 6),
              (12, 7),
              (12, 8),
              (12, 9),
              (12, 10),
              (12, 11),
              (12, 12),
              (12, 13),
              (12, 14),
              (12, 15),
              (12, 16),
              (12, 17),
              (12, 18),
              (12, 19),
              (12, 20),
              (12, 21),
              (12, 22),
              (12, 23),
              (12, 24),
              (12, 25),
              (12, 26),
              (12, 27),
              (12, 28),
              (12, 29),
              (12, 30),
              (12, 31),
              (12, 32),
              # Kawasaki
              (19, 63),
              (19, 64),
              # Lambo
              (21, 33),
              (21, 34),
              (21, 35),
              (21, 36),
              (21, 37),
              (21, 38),
              (21, 39),
              (21, 40),
              (21, 41),
              (21, 42),
              (21, 43),
              (21, 44),
              (21, 45),
              (21, 46),
              (21, 47),
              (21, 65),
              (21, 66),
              (21, 67),
              (21, 68),
              (21, 69),
              (21, 70),
              (21, 71),
              # Renault
              (34, 48),
              (34, 49),
              (34, 50),
              (34, 51)]

    c.executemany(
        'INSERT INTO BraMod(brand_id, model_id) VALUES(?,?);', values)
    conn.commit()


def FillsModVerTable():
    values = [(1, 1),
              (1, 2),
              (1, 3),
              (1, 4),
              (1, 5),
              (2, 6),
              (2, 7),
              (2, 8),
              (2, 9),
              (2, 10),
              (2, 11),
              (2, 12),
              (3, 13),
              (3, 14),
              (3, 15),
              (4, 16),
              (4, 17),
              (4, 18),
              (5, 19),
              (7, 20),
              (8, 21),
              (9, 24),
              (11, 33),
              (11, 34),
              (11, 35),
              (11, 36),
              (14, 37),
              (14, 38),
              (14, 39),
              (14, 40),
              (14, 41),
              (14, 42),
              (15, 43),
              (15, 44),
              (16, 31),
              (16, 32),
              (17, 29),
              (17, 30),
              (18, 27),
              (18, 28),
              (19, 25),
              (19, 26),
              (20, 51),
              (20, 52),
              (21, 53),
              (21, 54),
              (21, 55),
              (22, 45),
              (22, 46),
              (23, 47),
              (24, 22),
              (24, 23),
              (26, 48),
              (26, 49),
              (26, 50),
              (27, 56),
              (27, 57),
              (28, 64),
              (28, 65),
              (29, 63),
              (30, 58),
              (30, 59),
              (30, 60),
              (31, 61),
              (31, 62),
              (34, 97),
              (34, 100),
              (35, 98),
              (35, 101),
              (36, 84),
              (36, 87),
              (36, 88),
              (36, 89),
              (36, 90),
              (36, 94),
              (36, 95),
              (36, 99),
              (36, 102),
              (37, 91),
              (37, 92),
              (37, 96),
              (42, 66),
              (42, 67),
              (42, 68),
              (42, 78),
              (42, 79),
              (42, 80),
              (42, 81),
              (42, 82),
              (42, 85),
              (42, 86),
              (45, 69),
              (45, 70),
              (45, 71),
              (45, 72),
              (45, 73),
              (45, 74),
              (45, 75),
              (45, 83),
              (46, 69),
              (46, 70),
              (46, 71),
              (46, 72),
              (46, 73),
              (46, 74),
              (46, 75),
              (46, 83),
              (47, 76),
              (47, 77),
              (48, 103),
              (48, 104),
              (48, 105),
              (48, 106),
              (49, 107),
              (49, 108),
              (49, 109),
              (50, 110),
              (50, 111),
              (50, 112),
              (50, 113),
              (51, 114),
              (51, 115),
              (51, 116),
              (51, 117),
              (52, 118),
              (54, 119),
              (55, 120),
              (56, 121),
              (57, 122),
              (58, 123),
              (59, 124),
              (60, 125),
              (61, 126),
              (62, 127),
              (63, 128),
              (64, 129),
              (65, 130),
              (66, 131),
              (67, 132),
              (68, 133),
              (69, 134),
              (70, 135),
              (71, 136)]

    c.executemany(
        'INSERT INTO ModVer(model_id, version_id) VALUES(?,?);', values)
    conn.commit()


def FillsCatModTable():
    global c, conn
    values = [(13, 1),
              (13, 2),
              (13, 3),
              (13, 4),
              (13, 5),
              (13, 6),
              (13, 7),
              (13, 8),
              (13, 9),
              (13, 10),
              (13, 11),
              (13, 12),
              (13, 13),
              (13, 14),
              (13, 15),
              (13, 16),
              (13, 17),
              (13, 18),
              (13, 19),
              (13, 20),
              (13, 21),
              (13, 22),
              (13, 23),
              (13, 24),
              (13, 25),
              (13, 26),
              (13, 27),
              (13, 28),
              (13, 29),
              (13, 30),
              (13, 31),
              (13, 32),
              (13, 33),
              (13, 34),
              (13, 35),
              (13, 36),
              (13, 37),
              (13, 38),
              (13, 39),
              (13, 40),
              (13, 41),
              (13, 42),
              (13, 43),
              (13, 44),
              (13, 45),
              (13, 46),
              (13, 47),
              (13, 48),
              (13, 49),
              (13, 50),
              # Lig. Mercadorias
              (14, 51),
              # Lig. passageiros
              (15, 1),
              (15, 2),
              (15, 3),
              (15, 4),
              (15, 5),
              (15, 6),
              (15, 7),
              (15, 8),
              (15, 9),
              (15, 10),
              (15, 11),
              (15, 12),
              (15, 13),
              (15, 14),
              (15, 15),
              (15, 16),
              (15, 17),
              (15, 18),
              (15, 19),
              (15, 20),
              (15, 21),
              (15, 22),
              (15, 23),
              (15, 24),
              (15, 25),
              (15, 26),
              (15, 27),
              (15, 28),
              (15, 29),
              (15, 30),
              (15, 31),
              (15, 32),
              (15, 33),
              (15, 34),
              (15, 35),
              (15, 36),
              (15, 37),
              (15, 38),
              (15, 39),
              (15, 40),
              (15, 41),
              (15, 42),
              (15, 43),
              (15, 44),
              (15, 45),
              (15, 46),
              (15, 47),
              (15, 48),
              (15, 49),
              (15, 50),
              # Motociclo
              (17, 52),
              (17, 53),
              (17, 54),
              (17, 55),
              (17, 56),
              (17, 57),
              (17, 58),
              (17, 59),
              (17, 60),
              (17, 61),
              (17, 62),
              (17, 63),
              (17, 64),
              # Motociclo instr
              (18, 52),
              (18, 53),
              (18, 54),
              (18, 55),
              (18, 56),
              (18, 57),
              (18, 58),
              (18, 59),
              (18, 60),
              (18, 61),
              (18, 62),
              (18, 63),
              (18, 64),
              # Táxi
              (30, 1),
              (30, 2),
              (30, 3),
              (30, 4),
              (30, 5),
              (30, 6),
              (30, 7),
              (30, 8),
              (30, 9),
              (30, 10),
              (30, 11),
              (30, 12),
              (30, 13),
              (30, 14),
              (30, 15),
              (30, 16),
              (30, 17),
              (30, 18),
              (30, 19),
              (30, 20),
              (30, 21),
              (30, 22),
              (30, 23),
              (30, 24),
              (30, 25),
              (30, 26),
              (30, 27),
              (30, 28),
              (30, 29),
              (30, 30),
              (30, 31),
              (30, 32),
              (30, 33),
              (30, 34),
              (30, 35),
              (30, 36),
              (30, 37),
              (30, 38),
              (30, 39),
              (30, 40),
              (30, 41),
              (30, 42),
              (30, 43),
              (30, 44),
              (30, 45),
              (30, 46),
              (30, 47),
              (30, 48),
              (30, 49),
              (30, 50),
              # Trator
              (32, 65),
              (32, 66),
              (32, 67),
              (32, 68),
              (32, 69),
              (32, 70),
              (32, 71)]
    c.executemany(
        'INSERT INTO CatMod(category_id, model_id) VALUES(?,?);', values)
    conn.commit()


# Tests
def Test():
    print('Categorias')
    for row in c.execute('SELECT * FROM Category'):
        print(row)
    print('Marcas')
    for row in c.execute('SELECT * FROM Brand'):
        print(row)
    print('Modelos')
    for row in c.execute('SELECT * FROM Model'):
        print(row)
    print('Versões')
    for row in c.execute('SELECT * FROM Version'):
        print(row)

    yolo = 'SELECT bra_name FROM Brand WHERE bra_id = '
    x = [12, 20, 23]
    for value in x:
        if value == 23:
            yolo = yolo + str(value)
        else:
            yolo = yolo + str(value) + ' OR bra_id = '
    for row in c.execute(yolo):
        print(row)
    print('Tabelas Intermédias')
    for row in c.execute('SELECT * FROM ModVer WHERE model_id = 1'):
        print(row)

    # Test commands to DB
    carModels = Search(5, 'brand_id')
    print(Query('mod_name', 'Model', carModels, 'mod_id', 'OR'))
    Search(14, 'category_id')
    Search(33, 'brand_id')



    Query('cat_id', 'Category', [' ','Ligeiro Mercadorias'], 'cat_name', '')
    Search(123, 'oaskdpa')
    Query('mod_name', 'Model', ['', '2000', '2015'], 'mod_startYear', 'OR')
    Query('ver_name', 'Version', ['', '1250', '6000'], 'ver_engineSize', 'OR')
    Query('*', 'Model', ['', '2015'], 'mod_startYear', '')
    print(c.execute('SELECT * FROM Model JOIN category_id = 1 ON  '))
    print(Query('bra_id', 'Brand', ['', 'Ferrari', 'Lamborghini'], 'bra_name', 'OR'))

    # Close the connection
    conn.close()

# Calls the functions


def main(choice):
    print(conn)
    if int(choice) == 1:
        CreateDB()
        FillsProductDB()
        FillsCategoryDB()
        FillsBrandDB()
        FillsModelDB()
        FillsVehicleDB()
        FillsProCatTable()
        FillsCatBraTable()
        FillsBraModTable()
        FillsModVerTable()
        FillsCatModTable()
    elif int(choice) == 2:
        Test()
    else:
        print(-1)

    conn.close()


main(sys.argv[1])
