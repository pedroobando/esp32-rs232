# Lee y escribe es RS232

Lectura y escritura del RS232 a ttl, conectado a un ESP32

Microcontrolador: _ESP32 DevkitC_v4_

Programa escrito en micropython, con ayuda de chatGPT

## Conexion Pines de RS232 a ESP32

```
  VCC => 3V
  RXD => GPIO16
  TXD => GPIO17
  GND => GND
```

## main_envia.py

Envia numeros aleatorios entre 8000 y 12500 por el puerto RS232, cadavez que envia un numero enciende un led en el GPIO32.

## main_recibe_enciende.py

Abre el puerto RS232 y recibe datos, cuando recibe "ENCENDER" enciende un led en el GPIO32 y cuando recibe "APAGAR" apaga el led.

## main_recibe.py

Simplemente recibe data por el RS232 y la escribe en la data recibida.
