IDclientes = ["01","02","03","04","05"]
nombresClientes = ["lionel messi", "diego armando maradona", "martin palermo", "juan Roman Riqueleme", "clemente rodriguez"]

clientes = dict(zip(IDclientes, nombresClientes))
for IDclientes, nombresClientes in clientes.items():
    print(f"{IDclientes:10} {nombresClientes:4}")
