# 📡 Proyecto de Monitoreo de Temperatura con Raspberry Pi Pico W y ThingSpeak

Este proyecto utiliza una **Raspberry Pi Pico W** y un **sensor LM35** para medir la temperatura ambiente y enviarla a **ThingSpeak** para su monitoreo y análisis. 📊🌡️

## 🛠️ Componentes Utilizados
- 🖥️ **Raspberry Pi Pico W**
- 🌡️ **Sensor LM35**
- 🔌 **Jumpers y cables de conexión**
- 📡 **Conexión WiFi**
- ☁️ **Plataforma ThingSpeak**

## 🚀 Instalación y Configuración

### 1️⃣ Conectar los Componentes
Conectar el **LM35** a la Raspberry Pi Pico W:
- **VCC** (LM35) ➡️ **3.3V** (Raspberry Pi Pico W)
- **GND** (LM35) ➡️ **GND** (Raspberry Pi Pico W)
- **OUT** (LM35) ➡️ **GP26 (ADC0)** (Raspberry Pi Pico W)

### 2️⃣ Subir el Código a la Raspberry Pi Pico W
1. Instalar **Thonny IDE** (https://thonny.org/)
2. Copiar el código del repositorio en un nuevo archivo `main.py`
3. Configurar el **SSID** y **contraseña** del WiFi en el código.
4. Guardar y ejecutar el script en la Raspberry Pi Pico W.

### 3️⃣ Configurar ThingSpeak
1. Crear una cuenta en [ThingSpeak](https://thingspeak.com/)
2. Crear un **nuevo canal** y agregar un **campo** para la temperatura.
3. Copiar el **API Key** y el **Channel ID** en el código de la Raspberry Pi Pico W.
4. Ver los datos enviados en la plataforma.

## 📈 Funcionamiento del Código

### 🔗 Conexión a WiFi
El código se conecta a la red WiFi utilizando las credenciales proporcionadas y verifica la conexión antes de continuar.

### 📊 Lectura y Conversión de Datos
- Se lee la señal analógica del **LM35** utilizando el **ADC**.
- Se convierte la señal a **Voltios** y luego a **grados Celsius**.
- La temperatura se redondea a **2 decimales** para mayor precisión.

### ☁️ Envío de Datos a ThingSpeak
- La temperatura se envía a **ThingSpeak** mediante una solicitud HTTP.
- Se usa la API Key para autenticar la solicitud.
- Se registra la respuesta para verificar que los datos se envían correctamente.

### 🔄 Reintentos y Control de Errores
- Si la conexión a WiFi se pierde, el código intenta reconectar.
- Si hay errores en el envío de datos, se muestra un mensaje en la consola.

## 🔥 Problema Detectado y Sustento Técnico
Se observó una **alta variabilidad en las lecturas del sensor**, mientras que otros equipos obtenían valores más estables. Esto podría deberse a:
- **Ruido eléctrico** en la señal del ADC.
- **Conexión inestable** o mal contacto en los jumpers.
- **Fallos esporádicos** en la medición del LM35.
- **Errores de lectura intermitente**, provocando valores de **0°C** en momentos aleatorios.

Para mantener la validez del experimento y evitar afectar los **3 días de lecturas**, se optó por no reiniciar el sistema, sino analizar el comportamiento y buscar soluciones basadas en filtrado de datos y corrección de mediciones erráticas.

## 📬 Contacto
Si tienes dudas o quieres mejorar el código, ¡abre un issue o un pull request! 🚀😃
