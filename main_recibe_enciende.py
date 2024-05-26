from machine import UART, Pin
import time

# Configurar el LED en GPIO32
led = Pin(32, Pin.OUT)

# Configurar UART1 (puedes cambiar los pines según tu configuración)
uart1 = UART(1, baudrate=9600, tx=17, rx=16)

def read_uart():
    if uart1.any():
        data = uart1.read().decode('utf-8')
        return data
    return None

def main():
    while True:
        data = read_uart()
        if data:
            print("Recibido:", data)
            if "ENCENDER" in data:
                led.on()
            elif "APAGAR" in data:
                led.off()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
