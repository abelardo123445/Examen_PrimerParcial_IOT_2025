import network
import urequests
import utime
import machine

# Configuración WiFi
SSID = "IZZI-998C"
PASSWORD = "hq3HK2mp4hqHC2Cpyq"

# ThingSpeak API
THINGSPEAK_API_KEY = "TP4DC2T8VAILZCU2"
THINGSPEAK_CHANNEL_ID = "2844617"
THINGSPEAK_URL = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}"

# Configuración del sensor LM35
sensor = machine.ADC(26)  # LM35 conectado a GP26 (ADC0)
CONVERSION_FACTOR = 3.3 / 65535  # Conversión ADC a Voltios

# Configuración del LED interno de la Raspberry Pi Pico W
led = machine.Pin("LED", machine.Pin.OUT)
led.value(1)  # Mantener el LED encendido mientras el programa está en ejecución

def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando a WiFi...")
        wlan.connect(SSID, PASSWORD)
        
        tiempo_espera = 0
        while not wlan.isconnected() and tiempo_espera < 15:  # Esperar 15 segundos máximo
            utime.sleep(1)
            tiempo_espera += 1
        
        if wlan.isconnected():
            print("Conectado a WiFi:", wlan.ifconfig())
        else:
            print("Error: No se pudo conectar a WiFi")
    return wlan

def leer_temperatura():
    lectura = sensor.read_u16()  # Leer ADC (0-65535)
    voltaje = lectura * CONVERSION_FACTOR  # Convertir a Voltios
    temperatura = (voltaje * 1000) / 10  # Convertir a °C (LM35: 10mV/°C)
    return round(temperatura, 2)

def enviar_datos():
    temperatura = leer_temperatura()
    print(f"Temperatura: {temperatura}°C")
    
    url = f"{THINGSPEAK_URL}&field1={temperatura}"
    try:
        print("Enviando datos... Parpadeando LED interno")
        for _ in range(5):  # Parpadear 5 veces para indicar envío de datos
            led.value(0)
            utime.sleep(0.2)
            led.value(1)
            utime.sleep(0.2)
        response = urequests.get(url)
        print("Respuesta HTTP:", response.text)
        response.close()
    except Exception as e:
        print("Error enviando datos:", e)

# Ejecutar
wlan = conectar_wifi()

while True:
    if not wlan.isconnected():  # Reintentar conexión si se pierde
        wlan = conectar_wifi()
    
    enviar_datos()
    utime.sleep(180)  # Esperar 180 segundos
