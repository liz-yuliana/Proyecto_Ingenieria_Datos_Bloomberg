import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import ConsultasPython as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#-------------------------------------------------------------------------------------------------
# Hallar el promedio de las ganancias de cada una de las compañías que se encuentran dentro del S&P. 
con_2 = Connection()
con_2.openConnection()
query_2 = pd.read_sql_query(sql.promedio_ganancias_Empresas_SP(), con_2.connection)
con_2.closeConnection()
dfprom_gan_2 = pd.DataFrame(query_2, columns=["company", "average_revenue"])

# Grafico barras
figBarProm_gan_2 = px.bar(dfprom_gan_2.head(20), x="company", y="average_revenue",
                      height=1000,
                      title='Barras Verticales')
# Grafico barras horizontales
figBarProm_gan_2H = px.bar(dfprom_gan_2.head(30),  x="average_revenue", y="company", 
                      orientation = 'h',
                      height=1000,
                      title='Barras Horizontales')
#Grafico pie
figPieProm_gan_2 = px.pie(dfprom_gan_2.head(20), names="company", values="average_revenue")
#Grafico linea
figLineProm_gan_2 = px.line(dfprom_gan_2.head(20),  x="company", y="average_revenue")
#Mapa
figMapProm_gan_2 = px.choropleth(dfprom_gan_2, locations="company",
                            locationmode="country names",
                            color="average_revenue", 
                            hover_name="company", 
                            color_continuous_scale=["#99ccff", "#ff3333"])

# ------------------------------------------------------------------------
# Hallar el promedio del precio de cada una de las compañías que se encuentran dentro del S&P.
con_3 = Connection()
con_3.openConnection()
query_3 = pd.read_sql_query(sql.promedio_precio_Empresas_SP(), con_3.connection)
con_3.closeConnection()
dfprom_pre_3 = pd.DataFrame(query_3, columns=["company", "average_price"])

# Grafico barras
figBarProm_pre_3 = px.bar(dfprom_pre_3.head(20), x="company", y="average_price",
                      height=1000,
                      title='Barras Verticales')
# Grafico barras horizontales
figBarProm_pre_3H = px.bar(dfprom_pre_3.head(30),  x="average_price", y="company", 
                      orientation = 'h',
                      height=1000,
                      title='Barras Horizontales')
#Grafico pie
figPieProm_pre_3 = px.pie(dfprom_pre_3.head(20), names="company", values="average_price")
#Grafico linea
figLineProm_pre_3 = px.line(dfprom_pre_3.head(20),  x="company", y="average_price")
#Mapa
figMapProm_pre_3 = px.choropleth(dfprom_pre_3, locations="company",
                            locationmode="country names",
                            color="average_price", 
                            hover_name="company", 
                            color_continuous_scale=["#99ccff", "#ff3333"])

#--------------------------------------------------------------------------------
# Hallar el promedio del retorno de cada una de las compañías que se encuentran dentro del WLS.
con_4 = Connection()
con_4.openConnection()
query_4 = pd.read_sql_query(sql.promedio_retorno_Empresas_WLS(), con_4.connection)
con_4.closeConnection()
dfprom_ret_wls_4 = pd.DataFrame(query_4, columns=["company", "average_return"])

# Grafico barras
figBarProm_ret_wls_4 = px.bar(dfprom_ret_wls_4.head(20), x="company", y="average_return",
                      height=1000,
                      title='Barras Verticales')
# Grafico barras horizontales
figBarProm_ret_wls_4H = px.bar(dfprom_ret_wls_4.head(30),  x="average_return", y="company", 
                      orientation = 'h',
                      height=1000,
                      title='Barras Horizontales')
#Grafico pie
figPieProm_ret_wls_4 = px.pie(dfprom_ret_wls_4.head(20), names="company", values="average_return")
#Grafico linea
figLineProm_ret_wls_4 = px.line(dfprom_ret_wls_4.head(20),  x="company", y="average_return")
#Mapa
figMapProm_ret_wls_4 = px.choropleth(dfprom_ret_wls_4, locations="company",
                            locationmode="country names",
                            color="average_return", 
                            hover_name="company", 
                            color_continuous_scale=["#99ccff", "#ff3333"])                          

#---------------------------------------------------------------------
#Cantidad_Empresas_SWL()
con_5 = Connection()
con_5.openConnection()
query_5 = pd.read_sql_query(sql.Cantidad_Empresas_SWL(), con_5.connection)
con_5.closeConnection()
dfcant_swl_5 = pd.DataFrame(query_5, columns=["sector", "amount"])

# Grafico barras
figBarCant_swl_5 = px.bar(dfcant_swl_5.head(20), x="sector", y="amount",
                      height=1000,
                      title='Barras Verticales')
# Grafico barras horizontales
figBarCant_swl_5H = px.bar(dfcant_swl_5.head(30),  x="amount", y="sector", 
                      orientation = 'h',
                      height=1000,
                      title='Barras Horizontales')
#Grafico pie
figPieCant_swl_5 = px.pie(dfcant_swl_5.head(20), names="sector", values="amount")
#Grafico linea
figLineCant_swl_5 = px.line(dfcant_swl_5.head(20),  x="sector", y="amount")
 

#-----------------------------------------------------------------------
#Cantidad_Empresas_SP_pais()
con_6 = Connection()
con_6.openConnection()
query_6 = pd.read_sql_query(sql.Cantidad_Empresas_SP_pais(), con_6.connection)
con_6.closeConnection()
dfcant_sp_p_6 = pd.DataFrame(query_6, columns=["country", "amount"])

# Grafico barras
figBarCant_sp_p_6 = px.bar(dfcant_sp_p_6.head(20), x="country", y="amount",
                      height=1000,
                      title='Barras Verticales')
# Grafico barras horizontales
figBarCant_sp_p_6H = px.bar(dfcant_sp_p_6.head(30),  x="amount", y="country", 
                      orientation = 'h',
                      height=1000,
                      title='Barras Horizontales')
#Grafico pie
figPieCant_sp_p_6 = px.pie(dfcant_sp_p_6.head(20), names="country", values="amount")
#Grafico linea
figLineCant_sp_p_6 = px.line(dfcant_sp_p_6.head(20),  x="country", y="amount")
#Mapa
figMapCant_sp_p_6 = px.choropleth(dfcant_sp_p_6, locations="country",
                            locationmode="country names",
                            color="amount", 
                            hover_name="country", 
                            color_continuous_scale=["#99ccff", "#ff3333"])   

#-----------------------------------------------------------------------
# Consultamos la cantidad de empresas dentro del Indice
con_7 = Connection()
con_7.openConnection()
query_7 = pd.read_sql_query(sql.Cantidad_Empresas_WLS(), con_7.connection)
con_7.closeConnection()
dfcant_emp_in = pd.DataFrame(query_7, columns=["country", "quantity"])

# Grafico barras
figBarCant_emp_in = px.bar(dfcant_emp_in.head(20), x="country", y="quantity",
                      height=1000,
                      title='Barras Verticales')
# Grafico barras horizontales
figBarCant_emp_inH = px.bar(dfcant_emp_in.head(30),  x="quantity", y="country", 
                      orientation = 'h',
                      height=1000,
                      title='Barras Horizontales')
#Grafico pie
figPieCant_emp_in = px.pie(dfcant_emp_in.head(20), names="country", values="quantity")
#Grafico linea
figLineCant_emp_in = px.line(dfcant_emp_in.head(20),  x="country", y="quantity")
#Mapa
figMapCant_emp_in = px.choropleth(dfcant_emp_in, locations="country",
                            locationmode="country names",
                            color="quantity", 
                            hover_name="country", 
                            color_continuous_scale=["#99ccff", "#ff3333"])   

#-----------------------------------------------------------------------
# Hallar el promedio de las ganancias de cada una de las compañías que se encuentran dentro del WLS. 
con_8 = Connection()
con_8.openConnection()
query_8 = pd.read_sql_query(sql.promedio_ganancias_Empresas_WLS(), con_8.connection)
con_8.closeConnection()
dfprom_ganwls = pd.DataFrame(query_8, columns=["company", "average_revenue"])

#Grafico pie
figPieProm_ganwls = px.pie(dfprom_ganwls.head(20), names="company", values="average_revenue")
#Grafico linea
figLineProm_ganwls = px.line(dfprom_ganwls.head(20),  x="company", y="average_revenue")
#Mapa
figMapProm_ganwls = px.choropleth(dfprom_ganwls, locations="company",
                            locationmode="country names",
                            color="average_revenue", 
                            hover_name="company", 
                            color_continuous_scale=["#99ccff", "#ff3333"])  

#-----------------------------------------------------------------------
# Hallar el promedio de los precios ---- WLS. 
con_9 = Connection()
con_9.openConnection()
query_9 = pd.read_sql_query(sql.promedio_precio_Empresas_WLS(), con_9.connection)
con_9.closeConnection()
dfprom_prec = pd.DataFrame(query_9, columns=["company", "average_price"])

#Grafico pie
figPieProm_PWLS = px.pie(dfprom_prec.head(20), names="company", values="average_price")
#Grafico linea
figLineProm_PWLS = px.line(dfprom_prec.head(20),  x="company", y="average_price")
#Mapa
figMapProm_PWLS = px.choropleth(dfprom_prec, locations="company",
                            locationmode="country names",
                            color="average_price", 
                            hover_name="company", 
                            color_continuous_scale=["#99ccff", "#ff3333"])  

#------------------------------------------------------------LAYOUT
#LAYOUT
app.layout = html.Div(style={'background':'linear-gradient(black, #112D4E)'}, children=[
    html.Div(className="container", style={'padding':'25px', 'color':'#fff'}, children=[
        html.H1(children='Dashboard Proyecto Ingenieria de Datos', style={'textAlign':'center'}), # genera <h1>Dashboard</h1>
    ]),

    #Cant_emp_WLS 
    html.Div(className= "container", children=[
        # Row for cases
        html.Div(className= "row", style={'marginBottom': '20px'}, children=[
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", style={'marginBottom': '20px'}, children=[
                html.Div(className= "card border-info border-dark",  style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barCant_emp_in',
                                    figure=figBarCant_emp_in
                                ),    
                    ]),    
                    
                ]),
            ]),
            # Col for horizontal bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barHCant_emp_in',
                                    figure=figBarCant_emp_inH
                                ),   
                    ]),    
                    
                ]),
            ]),
            
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieCant_emp_in',
                                    figure=figPieCant_emp_in
                                ), 
                    ]),    
                    
                ]),
            ]),
            
            # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='lineCant_emp_in',
                                    figure=figLineCant_emp_in
                                ),
                    ]),    
                    
                ]),
            ]),
        ]), 
    ]),     
            
    #Prom_gan_wls
    html.Div(className= "container", children=[
        # Row for cases
        html.Div(className= "row", style={'marginBottom': '20px'}, children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                        html.H2(children='Promedio Ganancias (WLS)', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieProm_ganwls',
                                    figure=figPieProm_ganwls
                                ), 
                    ]),
                    
                ]),
            ]),
            
            # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Promedio Ganancias (WLS)', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='lineProm_ganwls',
                                    figure=figLineProm_ganwls
                                ),
                    ]),    
                    
                ]),
            ]),
        ]),
    ]),
    #Prom_precio (WLS)
    html.Div(className= "container", children=[
        # Row for cases
        html.Div(className= "row", style={'marginBottom': '20px'}, children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#93329E'}, children=[
                            html.H2(children='Promedio Precio (WLS)', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieProm_PWLS',
                                    figure=figPieProm_PWLS
                                ), 
                    ]),    
                    
                ]),
            ]),
            
            # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#93329E'}, children=[
                            html.H2(children='Promedio Precio (WLS)', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='lineProm_PWLS',
                                    figure=figLineProm_PWLS
                                ),
                    ]),    
                    
                ]),
            ]),
        ]),
    ]),
    #prom_gan
    html.Div(className= "container", children=[
        # Row for cases
        html.Div(className= "row", style={'marginBottom': '20px'}, children=[
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", style={'marginBottom': '20px'}, children=[
                html.Div(className= "card border-info border-dark",  style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Promedio Ganancias', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barProm_gan_2',
                                    figure=figBarProm_gan_2
                                ),    
                    ]),    
                    
                ]),
            ]),
            # Col for horizontal bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Promedio Ganancias', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barHProm_gan_2',
                                    figure=figBarProm_gan_2H
                                ),   
                    ]),    
                    
                ]),
            ]),
            
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Promedio Ganancias', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieProm_gan_2',
                                    figure=figPieProm_gan_2
                                ), 
                    ]),    
                    
                ]),
            ]),
            
            # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Promedio Ganancias', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='lineProm_gan_2',
                                    figure=figLineProm_gan_2
                                ),
                    ]),    
                    
                ]),
            ]),
        ]),
    ]),

    #prom_precio
    html.Div(className= "container", children=[
        # Row for cases
        html.Div(className= "row", style={'marginBottom': '20px'}, children=[
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", style={'marginBottom': '20px'}, children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#93329E'}, children=[
                            html.H2(children='Promedio Precio', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barProm_pre_3',
                                    figure=figBarProm_pre_3
                                ),    
                    ]),    
                    
                ]),
            ]),
            # Col for horizontal bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#93329E'}, children=[
                            html.H2(children='Promedio Precio', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barHProm_pre_3',
                                    figure=figBarProm_pre_3H
                                ),   
                    ]),    
                    
                ]),
            ]),
            
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#93329E'}, children=[
                            html.H2(children='Promedio Precio', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieProm_pre_3',
                                    figure=figPieProm_pre_3
                                ), 
                    ]),    
                    
                ]),
            ]),
            
            # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#93329E'}, children=[
                            html.H2(children='Promedio Precio', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='lineProm_pre_3',
                                    figure=figLineProm_pre_3
                                ),
                    ]),    
                    
                ]),
            ]),
        ]),
    ]),

    #prom_ret
    html.Div(className= "container", children=[
        html.Div(className= "row", style={'marginBottom': '20px'}, children=[
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", style={'marginBottom': '20px'}, children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#C62A88'}, children=[
                            html.H2(children='Promedio Retorno', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barProm_ret_wls_4',
                                    figure=figBarProm_ret_wls_4
                                ),    
                    ]),    
                    
                ]),
            ]),
            # Col for horizontal bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#C62A88'}, children=[
                            html.H2(children='Promedio Retorno', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barHProm_ret_wls_4',
                                    figure=figBarProm_ret_wls_4H
                                ),   
                    ]),    
                    
                ]),
            ]),
            
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#C62A88'}, children=[
                            html.H2(children='Promedio Retorno', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieProm_ret_wls_4',
                                    figure=figPieProm_ret_wls_4
                                ), 
                    ]),    
                    
                ]),
            ]),
            
            # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#C62A88'}, children=[
                            html.H2(children='Promedio Retorno', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='lineProm_ret_wls_4',
                                    figure=figLineProm_ret_wls_4
                                ),
                    ]),    
                    
                ]),
            ]),
        ]),
    ]), 

    #Cantidad_Empresas_SWL()
    html.Div(className= "container", children=[
        # Row for cases
        html.Div(className= "row", style={'marginBottom': '20px'}, children=[
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", style={'marginBottom': '20px'}, children=[
                html.Div(className= "card border-info border-dark",  style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas - Sector', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barCant_swl_5',
                                    figure=figBarCant_swl_5
                                ),    
                    ]),    
                    
                ]),
            ]),
            # Col for horizontal bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas - Sector', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barHCant_swl_5',
                                    figure=figBarCant_swl_5H
                                ),   
                    ]),    
                    
                ]),
            ]),
            
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas - Sector', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieCant_swl_5',
                                    figure=figPieCant_swl_5
                                ), 
                    ]),    
                    
                ]),
            ]),
            
            # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas - Sector', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='lineCant_swl_5',
                                    figure=figLineCant_swl_5
                                ),
                    ]),    
                    
                ]),
            ]),
        ]),
    ]),

    #Cantidad_Empresas_SP_pais()
    html.Div(className= "container", children=[
        # Row for cases
        html.Div(className= "row", style={'marginBottom': '20px'}, children=[
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", style={'marginBottom': '20px'}, children=[
                html.Div(className= "card border-info border-dark",  style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas (S_and_P)', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barCant_sp_p_6',
                                    figure=figBarCant_sp_p_6
                                ),    
                    ]),    
                    
                ]),
            ]),
            # Col for horizontal bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas (S_and_P)', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barHCant_sp_p_6',
                                    figure=figBarCant_sp_p_6H
                                ),   
                    ]),    
                    
                ]),
            ]),
            
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas (S_and_P)', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieCant_sp_p_6',
                                    figure=figPieCant_sp_p_6
                                ), 
                    ]),    
                    
                ]),
            ]),
            
            # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info border-dark", style={'backgroundColor':'#292C6D', 'color':'#fff'}, children=[
                    html.Div(className= "card-header", style={'backgroundColor':'#EC255A'}, children=[
                            html.H2(children='Cantidad Empresas (S_and_P)', style={'textAlign': 'center'}),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='lineCant_sp_p_6',
                                    figure=figLineCant_sp_p_6
                                ),
                    ]),    
                    
                ]),
            ]),
        ]),
    ]),

    #Mapas
    html.Div(className= "col-12 col-xl-6", style={'position':'relative', 'left':'25%', 'right':'25%', 'marginBottom':'20px'}, children=[
        html.Div(className= "card border-info border-dark", style={'color':'#fff'}, children=[
                html.Div(className="card-header", style={'backgroundColor':'#03C4A1'}, children=[
                    html.H2(children='Promedio Ganancias', style={'textAlign': 'center', 'color':'#fff'}),
                ]),   
        ]),
        html.Div(className="card-body", style={'backgroundColor':'#292C6D'}, children=[
                dcc.Graph(
                id='mapCasesProm_gan_2',
                figure=figMapProm_gan_2
                ),
        ]),    
    ]),    
    html.Div(className= "col-12 col-xl-6", style={'position':'relative', 'left':'25%', 'right':'25%', 'marginBottom':'20px'}, children=[
        html.Div(className= "card border-info border-dark", style={'color':'#fff'}, children=[
                html.Div(className="card-header", style={'backgroundColor':'#03C4A1'}, children=[
                    html.H2(children='Promedio Precio', style={'textAlign': 'center', 'color':'#fff'}),
                ]),   
        ]),
        html.Div(className="card-body", style={'backgroundColor':'#292C6D'}, children=[
            dcc.Graph(
                id='mapCasesProm_pre_3',
                figure=figMapProm_pre_3
            ),
        ]),    
    ]), 
    html.Div(className= "col-12 col-xl-6", style={'position':'relative', 'left':'25%', 'right':'25%', 'marginBottom':'20px'}, children=[
        html.Div(className= "card border-info border-dark", style={'color':'#fff'}, children=[
                html.Div(className="card-header", style={'backgroundColor':'#03C4A1'}, children=[
                    html.H2(children='Promedio Retorno', style={'textAlign': 'center', 'color':'#fff'}),
                ]),   
        ]),
        html.Div(className="card-body", style={'backgroundColor':'#292C6D'}, children=[
            dcc.Graph(
                id='mapCasesProm_ret_wls_4',
                figure=figMapProm_ret_wls_4
            ),
        ]),    
    ]),
    html.Div(className= "col-12 col-xl-6", style={'position':'relative', 'left':'25%', 'right':'25%', 'marginBottom':'20px'}, children=[
        html.Div(className= "card border-info border-dark", style={'color':'#fff'}, children=[
                html.Div(className="card-header", style={'backgroundColor':'#03C4A1'}, children=[
                    html.H2(children='Cantidad Empresas (S_and_P)', style={'textAlign': 'center', 'color':'#fff'}),
                ]),   
        ]),
        html.Div(className="card-body", style={'backgroundColor':'#292C6D'}, children=[
            dcc.Graph(
                id='mapCant_sp_p_6',
                figure=figMapCant_sp_p_6
            ),
        ]),    
    ]),
    html.Div(className= "col-12 col-xl-6", style={'position':'relative', 'left':'25%', 'right':'25%', 'marginBottom':'20px'}, children=[
        html.Div(className= "card border-info border-dark", style={'color':'#fff'}, children=[
                html.Div(className="card-header", style={'backgroundColor':'#03C4A1'}, children=[
                    html.H2(children='Cantidad Empresas (WLS)', style={'textAlign': 'center', 'color':'#fff'}),
                ]),   
        ]),
        html.Div(className="card-body", style={'backgroundColor':'#292C6D'}, children=[
            dcc.Graph(
                id='mapCasesCant_emp_incd',
                figure=figMapCant_emp_in
            ),
        ]),    
    ]),
    html.Div(className= "col-12 col-xl-6", style={'position':'relative', 'left':'25%', 'right':'25%', 'marginBottom':'20px'}, children=[
        html.Div(className= "card border-info border-dark", style={'color':'#fff'}, children=[
                html.Div(className="card-header", style={'backgroundColor':'#03C4A1'}, children=[
                    html.H2(children='Promedio Ganancias (WLS)', style={'textAlign': 'center', 'color':'#fff'}),
                ]),   
        ]),
        html.Div(className="card-body", style={'backgroundColor':'#292C6D'}, children=[
            dcc.Graph(
                id='mapCant_Prom_ganwls',
                figure=figMapProm_ganwls
            ),
        ]),    
    ]),
    html.Div(className= "col-12 col-xl-6", style={'position':'relative', 'left':'25%', 'right':'25%', 'marginBottom':'20px'}, children=[
        html.Div(className= "card border-info border-dark", style={'color':'#fff'}, children=[
                html.Div(className="card-header", style={'backgroundColor':'#03C4A1'}, children=[
                    html.H2(children='Promedio Precio (WLS)', style={'textAlign': 'center', 'color':'#fff'}),
                ]),   
        ]),
        html.Div(className="card-body", style={'backgroundColor':'#292C6D'}, children=[
            dcc.Graph(
                id='mapProm_PWLS',
                figure=figMapProm_PWLS
            ),
        ]),    
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
