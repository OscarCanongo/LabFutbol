import pandas as pd

disparosApuertaApertura = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_apertura/2020/ranking/equipos/disparos-a-puerta/")
disparosApuertaClausura = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_clausura/2021/ranking/equipos/disparos-a-puerta/")
dfdisparosAPuertaApertura = pd.DataFrame(disparosApuertaApertura[0])
dfdisparosAPuertaClausura = pd.DataFrame(disparosApuertaClausura[0])

goles = pd.read_html("https://ligamx.net/cancha/tablas/tablaOfnsDfns/sp/8934b8c89a62e0")
dfgoles = pd.DataFrame(goles[0])

#limpiar datos
dfgoles = dfgoles.replace({"AmÃ©rica": "América", "Club AtlÃ©tico de San Luis": "Atlético San Luis",
                       "Gallos Blancos de QuerÃ©taro": "Gallos Blancos", "MazatlÃ¡n FC": "Mazatlán Fútbol Club",
                       "FC JuÃ¡rez": "Bravos", "LeÃ³n":"León FC"
                      })

#Componemos datos
dfgoles = dfgoles.replace({"Guadalajara": "Chivas", "Tijuana":"Xolos", "UANL":"Tigres", 
                           "Puebla F.C.": "Puebla", "PUMAS": "Pumas", "Monterrey":"Rayados"})
dfgoles = dfgoles.rename(columns = {'Club':'Equipo'})

dfdisparosAPuertaApertura['Equipo'] = dfdisparosAPuertaApertura['Equipo'].str.rstrip(' México')
dfdisparosAPuertaClausura['Equipo'] = dfdisparosAPuertaClausura['Equipo'].str.rstrip(' México')
dfdisparosAPuertaApertura['Total'] = dfdisparosAPuertaApertura['Total'].str.rstrip('Disparos a puerta').astype('int')
dfdisparosAPuertaClausura['Total'] = dfdisparosAPuertaClausura['Total'].str.rstrip('Disparos a puerta').astype('int')
dfdisparosAPuertaApertura = dfdisparosAPuertaApertura.drop(['Pos.'], axis = 1)
dfdisparosAPuertaClausura = dfdisparosAPuertaClausura.drop(['Pos.'], axis = 1)

#Unimos el año futbolistico
dfdisparosAPuerta = pd.concat([dfdisparosAPuertaApertura, dfdisparosAPuertaClausura]).groupby(['Equipo']).sum().reset_index()
dfdisparosAPuerta = dfdisparosAPuerta.rename(columns = {'Total':'DisparosAPuerta'})

#Inner Join dataframes
final = dfgoles.set_index('Equipo').join(dfdisparosAPuerta.set_index('Equipo'))

#InnerJoin de dataframes
print(final)