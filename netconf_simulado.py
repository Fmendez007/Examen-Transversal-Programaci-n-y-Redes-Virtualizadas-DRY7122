from ncclient import manager
from unittest.mock import MagicMock

# Simulamos los datos de conexión (pero no se ejecuta)
router = {
    "host": "198.18.134.11",
    "port": 830,
    "username": "admin",
    "password": "C1sco12345",
    "hostkey_verify": False
}

# Configuración XML de NETCONF para hostname y loopback
config_data = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Lemus-Mendez</hostname>
    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

print("🔧 Simulando conexión NETCONF...")

# Simular conexión usando MagicMock
fake_manager = MagicMock()
fake_manager.edit_config.return_value = "<ok/>"

print("🛰️ Conectado (simulado) al router CSR1000v")
print("📡 Enviando configuración NETCONF...")
print("🧾 Configuración:")
print(config_data)
print("✅ Resultado del envío:")
print(fake_manager.edit_config(target="running", config=config_data))
