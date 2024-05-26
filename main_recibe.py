from machine import UART, Pin
import time

# Pines de RS232 a ESP32
# VCC => 3V
# RXD => GPIO16 
# TXD => GPIO17
# GND => GND

# Configurar UART1 (cambia los pines según tu configuración)
uart1 = UART(1, baudrate=9600, tx=17, rx=16)

def read_uart():
    if uart1.any():
        data = uart1.read()
        if data:
            try:
                decoded_data = data.decode('utf-8')
                return decoded_data
            except UnicodeDecodeError:
                # Manejo de errores de decodificación si no es UTF-8
                return None
    return None

def main():
    print('inicio de app')
    while True:
        data = read_uart()
        if data:
            print("Recibido:", data)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
