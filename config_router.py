from netmiko import ConnectHandler

# Configuración del router
router = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',         # Cambia por la IP de tu router
    'username': 'admin',           # Cambia por tu usuario
    'password': 'admin123',        # Cambia por tu contraseña
    'secret': 'admin123',          # Cambia por la enable password (si aplica)
}

# Comandos de configuración por defecto
config_commands = [
    'hostname ROUTER-DEFAULT',
    'no ip domain-lookup',
    'enable secret cisco',
    'interface GigabitEthernet0/0',
    'ip address 192.168.1.1 255.255.255.0',
    'no shutdown',
    'exit',
    'line console 0',
    'password cisco',
    'login',
    'exit',
    'line vty 0 4',
    'password cisco',
    'login',
    'transport input ssh',
    'exit',
    'service password-encryption',
    'banner motd #Acceso no autorizado está prohibido#',
    'ip routing'
]

# Conexión y configuración
print("Conectando al router...")
connection = ConnectHandler(**router)
connection.enable()
print("Aplicando configuración...")
connection.send_config_set(config_commands)
print("Guardando configuración...")
connection.save_config()
print("Configuración del router completada.")
connection.disconnect()
