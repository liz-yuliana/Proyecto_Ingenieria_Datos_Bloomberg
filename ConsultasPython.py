def Cantidad_Empresas_WLS():
    return """SELECT c.name as country, COUNT(t.id_ticker) as quantity
        FROM ticker t INNER JOIN WLS_company w ON (t.id_ticker = w.id_ticker_company) INNER JOIN WLS_country c ON (w.country = c.id_country)
        GROUP BY c.name
        ORDER BY 1 """

def promedio_ganancias_Empresas_WLS():
    return """select name as company, avg(revenue) as average_revenue
        from WLS_company
        group by company
        """

def promedio_precio_Empresas_WLS():
    return """select name as company, avg(price) as average_price
        from WLS_company
        group by company
        """

def Cantidad_Empresas_SWL():
    return """SELECT s.sector as sector, Count(w.revenue) as amount
        FROM WLS_company w INNER JOIN sector s ON (w.sector = s.id_sector)
        GROUP BY s.sector"""

def Cantidad_Empresas_SP_pais():
    return """SELECT c.name as country, COUNT(t.ticker) as amount
        FROM ticker t INNER JOIN S_and_P sp ON (t.id_ticker = sp.id_ticker_sp) INNER JOIN WLS_country c ON (sp.id_country = c.id_country)
        GROUP BY c.name
        ORDER BY 1 """ 

def promedio_ganancias_Empresas_SP():
    return """SELECT name as company, avg(revenue) as average_revenue
        FROM S_and_P
	GROUP BY name"""

def promedio_precio_Empresas_SP():
    return """SELECT name as company, avg(price) as average_price
        FROM S_and_P
	GROUP BY name
        """

def promedio_retorno_Empresas_WLS():
    return """SELECT name as company, avg(total_return) as average_return
        FROM WLS_company
	GROUP BY name"""

# Revisión general de los datos

def SP5x_Index():
    return """select *
        from S_and_P;
        """

def WLS_Index():
    return """select *
        from WLS_company;
        """

def SEC():
    return """select *
        from sector;
    """
