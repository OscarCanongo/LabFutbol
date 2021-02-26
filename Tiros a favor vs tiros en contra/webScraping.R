library(rvest)

disparos <- read_html("https://mexico.as.com/resultados/futbol/mexico_clausura/2021/ranking/equipos/disparos/")
tables <- disparos %>% html_table
write.csv(tables,"disparos.csv", row.names = FALSE)

disparosAPuerta <- read_html("https://mexico.as.com/resultados/futbol/mexico_clausura/2021/ranking/equipos/disparos-a-puerta/")
tables1 <- disparosAPuerta %>% html_table(fill = TRUE)
write.csv(tables1,"disparosAPuerta.csv", row.names = FALSE)

goles <- read_html("https://mexico.as.com/resultados/futbol/mexico_clausura/2021/ranking/equipos/goles/")
tables2 <- goles %>% html_table(fill = TRUE)
write.csv(tables2,"goles.csv", row.names = FALSE)

disparosRecibidos <- read_html("https://mexico.as.com/resultados/futbol/mexico_clausura/2021/ranking/equipos/disparos-recibidos/")
tables3 <- disparosRecibidos %>% html_table(fill = TRUE)
write.csv(tables3,"disparosRecibidos.csv", row.names = FALSE)


