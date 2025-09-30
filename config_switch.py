from netmiko import ConnectHandler

# Configuración del switch
switch = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.2',         # Cambia por la IP de tu switch
    'username': 'admin',           # Cambia por tu usuario
    'password': 'admin123',        # Cambia por tu contraseña
    'secret': 'admin123',          # Cambia por la enable password (si aplica)
}

# Comandos de configuración por defecto
config_commands = [
    'hostname SWITCH-DEFAULT',
    'no ip domain-lookup',
    'enable secret cisco',
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
]

# Conexión y configuración
print("Conectando al switch...")
connection = ConnectHandler(**switch)
connection.enable()
print("Aplicando configuración...")
connection.send_config_set(config_commands)
print("Guardando configuración...")
connection.save_config()
print("Configuración del switch completada.")
connection.disconnect()
