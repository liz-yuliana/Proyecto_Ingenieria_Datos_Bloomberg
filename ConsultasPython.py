def Cantidad_Empresas_WLS():
    return """select count(ticker)
        from WLS_company
        order by country;
        """

def promedio_ganancias_Empresas_WLS():
    return """select avg(revenue)
        from WLS_company;
        """

def promedio_precio_Empresas_WLS():
    return """select avg(price)
        from WLS_company;
        """

def promedio_retorno_Empresas_WLS():
    return """select avg(total_return)
        from WLS_company;
        """
def ranking_sector():
    return """select *
        dense_rank() over(partition by sector_sector order by country desc)
        from WLS_company;"""

def Cantidad_Empresas_SP():
    return """select count(ticker)
        from S_and_P;
        """

def Cantidad_Empresas_SP_pais():
    return """select count(ticker)
        from S_and_P,
        order by COUNTRY;
        """

def Sect_SP():
    return """select s.name, sp.name
    from  sector s inner join S_and_P sp on (s.sector = sp.sector_company)
    group by s.name;
    """

def promedio_ganancias_Empresas_SP():
    return """select avg(revenue)
        from S_and_P;
        """

def promedio_precio_Empresas_SP():
    return """select avg(price)
        from S_and_P;
        """

def promedio_retorno_Empresas_WLS():
    return """select avg(total_return)
        from WLS_company;
        """

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
