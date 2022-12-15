# Instal·lem la biblioteca amb la següent comanda: pip install ipaddress
import ipaddress

# Creem l'objecta amb la funció com a paràmetre la xarxa d'on volem saber les IP's disponible
ip_network = ipaddress.IPv4Network('192.168.1.0/24')

# Amb hosts obtenim les ips disponibles.
available_ips = list(ip_network.hosts())

# Iterem amb un for la llista d'IP's disponibles.
for ip in available_ips:
    print(ip)
