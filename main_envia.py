
from machine import Pin, UART, sleep
import urandom

# Configuración del LED en el GPIO32
led = Pin(32, Pin.OUT)

# Configuración del UART para RS232
uart = UART(1, baudrate=9600, tx=17, rx=16)  # Ajusta los pines tx y rx según tu conexión

def enviar_numero_aleatorio():
    numero = urandom.randint(8000, 12500)
    uart.write(str(numero) + '\n')
    print("Número enviado:", numero)

while True:
    led.value(1)  # Enciende el LED
    enviar_numero_aleatorio()
    sleep(0.5)  # Anti-rebote
    led.value(0)  # Apaga el LED
    
    sleep(2)  # Pequeño retraso para evitar rebotes del botón



