# clasificar_vlan.py
vlan = int(input("Ingrese número de VLAN: "))

if 1 <= vlan <= 1005:
    print("VLAN Normal")
elif 1006 <= vlan <= 4094:
    print("VLAN Extendida")
else:
    print("VLAN fuera de rango")
