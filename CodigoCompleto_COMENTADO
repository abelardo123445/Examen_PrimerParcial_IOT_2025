import network  # Módulo para manejar la conexión WiFi
import urequests  # Librería para realizar solicitudes HTTP
import utime  # Módulo para manejar tiempos y pausas
import machine  # Módulo para interactuar con hardware (pines, ADC, etc.)

# Configuración WiFi
SSID = "IZZI-998C"  # Nombre de la red WiFi
PASSWORD = "hq3HK2mp4hqHC2Cpyq"  # Contraseña de la red WiFi

# ThingSpeak API
THINGSPEAK_API_KEY = "TP4DC2T8VAILZCU2"  # Clave de API para enviar datos a ThingSpeak
THINGSPEAK_CHANNEL_ID = "2844617"  # ID del canal en ThingSpeak
THINGSPEAK_URL = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}"  # URL para enviar datos

# Configuración del sensor LM35
sensor = machine.ADC(26)  # LM35 conectado al pin GP26 (ADC0)
CONVERSION_FACTOR = 3.3 / 65535  # Factor de conversión de lectura ADC a voltios

# Configuración del LED interno de la Raspberry Pi Pico W
led = machine.Pin("LED", machine.Pin.OUT)  # LED de la placa como salida
led.value(1)  # Mantener el LED encendido mientras el programa está en ejecución

def conectar_wifi():
    """Función para conectar a la red WiFi."""
    wlan = network.WLAN(network.STA_IF)  # Configurar WiFi en modo estación
    wlan.active(True)  # Activar la interfaz WiFi
    
    if not wlan.isconnected():
        print("Conectando a WiFi...")
        wlan.connect(SSID, PASSWORD)  # Intentar conectar con SSID y contraseña
        
        tiempo_espera = 0
        while not wlan.isconnected() and tiempo_espera < 15:  # Esperar hasta 15 segundos
            utime.sleep(1)
            tiempo_espera += 1
        
        if wlan.isconnected():
            print("Conectado a WiFi:", wlan.ifconfig())  # Mostrar información de red
        else:
            print("Error: No se pudo conectar a WiFi")
    return wlan

def leer_temperatura():
    """Función para leer la temperatura del sensor LM35."""
    lectura = sensor.read_u16()  # Leer valor del ADC (0-65535)
    voltaje = lectura * CONVERSION_FACTOR  # Convertir lectura ADC a voltios
    temperatura = (voltaje * 1000) / 10  # Convertir voltaje a °C (LM35: 10mV/°C)
    return round(temperatura, 2)  # Redondear a 2 decimales

def enviar_datos():
    """Función para enviar la temperatura a ThingSpeak."""
    temperatura = leer_temperatura()
    print(f"Temperatura: {temperatura}°C")
    
    url = f"{THINGSPEAK_URL}&field1={temperatura}"  # URL con datos de temperatura
    try:
        print("Enviando datos... Parpadeando LED interno")
        for _ in range(5):  # Parpadeo del LED para indicar envío
            led.value(0)
            utime.sleep(0.2)
            led.value(1)
            utime.sleep(0.2)
        
        response = urequests.get(url)  # Enviar solicitud HTTP
        print("Respuesta HTTP:", response.text)  # Mostrar respuesta de ThingSpeak
        response.close()  # Cerrar conexión
    except Exception as e:
        print("Error enviando datos:", e)  # Manejo de errores

# Ejecutar el programa
wlan = conectar_wifi()  # Conectar a WiFi al inicio

while True:
    if not wlan.isconnected():  # Si se pierde la conexión, intentar reconectar
        wlan = conectar_wifi()
    
    enviar_datos()  # Leer y enviar temperatura a ThingSpeak
    utime.sleep(180)  # Esperar 180 segundos antes de la siguiente lectura
