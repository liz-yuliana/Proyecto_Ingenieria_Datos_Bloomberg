def Cantidad_Empresas_WLS():
    return """select count(ticker)
        from "indice";
        """

def Cantidad_Empresas_WLS_pais():
    return """select count(ticker)
        from "indice"
        where codigo_pais = 1;
        """


def promedio_ganancias_Empresas_WLS():
    return """select avg(ganancias)
        from "indice";
        """

def promedio_precio_Empresas_WLS():
    return """select avg(precio_accion)
        from "indice";
        """

def promedio_retorno_Empresas_WLS():
    return """select avg(retorno_acion)
        from "indice";
        """
def ranking_sector():
    return """select *,
        dense_rank() over(partition by sector desc)
        from indice;"""

def Cantidad_Empresas_SP():
    return """select count(ticker)
        from "S&P";
        """

def Cantidad_Empresas_SP_pais():
    return """select count(ticker)
        from "S&P"
        where codigo_pais = 1;
        """


def promedio_ganancias_Empresas_SP():
    return """select avg(ganancias)
        from "S&P";
        """

def promedio_precio_Empresas_SP():
    return """select avg(precio_accion)
        from "indice";
        """

def promedio_retorno_Empresas_WLS():
    return """select avg(retorno_acion)
        from "S&P";
        """