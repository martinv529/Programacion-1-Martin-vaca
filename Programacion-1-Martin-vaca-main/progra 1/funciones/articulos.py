matriz_productos =[ 
    ["01", "silla", "10000"], 
    ["02","mesa","30000"],
    ["03","escritorio","25000"],
    ["04","sillon","50000"],
    ["05","mesa de luz","20000"]
    ]

encabezado = ["IDarticulo", "articulo", "precio"]

for fila in matriz_productos:
    id_, articulo, precio = fila
    print(f"{id_:<5} {articulo:<15} {precio:>10}")

productos = [dict(zip(encabezado,fila))for fila in matriz_productos]

for producto in productos:
    print(producto)