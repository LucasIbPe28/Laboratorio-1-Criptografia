import sys
import socket
import struct
from scapy.all import IP, ICMP, send

def generate_icmp_packets(destination_ip, message):
    # Convierte el mensaje en una lista de bytes
    message_bytes = message.encode()

    # Largo de la lista de bytes
    message_length = len(message_bytes)

    # Construye paquetes ICMP
    packets = []
    for i in range(message_length):
        # Crea un paquete ICMP con el formato deseado
        icmp_packet = IP(dst=destination_ip, ttl=64) / ICMP(
            type=8,   # Tipo 8 para ICMP Request
            code=0,   # Código 0
            id=0x1337,  # ID arbitrario
            seq=i,    # Número de secuencia
        )

        # Agrega datos al paquete ICMP
        icmp_packet = icmp_packet / (message_bytes[i:i+1] + b'\x00' * 7 + bytes(range(0x10, 0x38)))

        # Agrega el paquete a la lista
        packets.append(icmp_packet)

    return packets

if len(sys.argv) != 2:
    print("Uso: python3 icmp_sender.py 'mensaje'")
    sys.exit(1)

destination_ip = "8.8.8.8"  # IP de destino (Google DNS)
message = sys.argv[1]  # Mensaje a enviar

# Genera paquetes ICMP
icmp_packets = generate_icmp_packets(destination_ip, message)

# Envía los paquetes
for packet in icmp_packets:
    send(packet, verbose=False)
    print(f"Enviando ICMP request: {packet[ICMP].seq}")

print("Mensajes ICMP enviados con éxito.")



