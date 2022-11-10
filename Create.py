import psycopg2
try:
    conexion = psycopg2.connect(user="usuario",
                                password="clave",
                                database="proyecto",
                                host="localhost",
                                port="5432")
    print("Conexión correcta!")

    conexion.autocommit = False   
    cursor = conexion.cursor()

    ticker = """CREATE TABLE ticker(id_ticker serial PRIMARY KEY,
	ticker varchar(50) NOT NULL);"""
    
    sector = """CREATE TABLE sector (
	id_sector serial NOT NULL PRIMARY KEY ,
	sector varchar(30);"""

    WLS_country = """CREATE TABLE WLS_country(
                    id_country integer NOT NULL,
                    name varchar(40) NOT NULL,
                    weight real NOT NULL,
                    shares real NOT NULL,
                    PRIMARY KEY (id_country));"""

    WLS_company = """CREATE TABLE WLS_company(
                id_ticker_company serial NOT NULL,
                name varchar(50) NOT NULL,
                country serial NOT NULL,
                weight real,
                shares real NOT NULL,
                price real,
                sector serial,
                revenue real,
                total_return real,
                PRIMARY KEY (id_ticker_company),
                FOREIGN KEY (sector) REFERENCES sector (id_sector),
                FOREIGN KEY (country) REFERENCES WLS_country (id_country),
                FOREIGN KEY (id_ticker_company) REFERENCES ticker (id_ticker));"""

    S_and_P  = """CREATE TABLE S_and_P(
	id_ticker_sp integer NOT NULL,
	name varchar(50) NOT NULL,
	id_country serial NOT NULL,
	price real NOT NULL,
	sector_company serial NOT NULL,
	revenue real NOT NULL,
	PRIMARY KEY (id_ticker_sp),
	FOREIGN KEY (sector_company) REFERENCES sector (id_sector),
	FOREIGN KEY (id_country) REFERENCES WLS_country (id_country),
	FOREIGN KEY (id_ticker_sp) REFERENCES ticker (id_ticker));"""

    cursor.executemany(ticker,sector, WLS_country, WLS_company, S_and_P)
    conexion.commit()
    print("Tablas creadas")

except psycopg2.Error as e:
    print("Ocurrió un error al crear: ", e)
    conexion.rollback();

finally:
    cursor.close()
    conexion.close()
