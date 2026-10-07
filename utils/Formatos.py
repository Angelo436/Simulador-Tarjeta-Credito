# Función para formatear el número estilo ES: 1.250,50
formato_espanol = lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")