import sys
import scapy.all as scapy

def cesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            else:
                if shifted < ord('a'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def is_plausible(text):
    common_words = ["el", "la", "de", "en", "que", "no", "es", "un", "para", "se", "lo", "con", "como", "por", "pero", "más"]
    connectors = [ "pero", "sin embargo", "además", "por lo tanto"]
    
    words = text.split()
    for word in words:
        word = word.lower().strip(".,")
        if word in common_words or word in connectors:
            return True
    return False

def main(filename):
    try:
        packets = scapy.rdpcap(filename)
        icmp_payload = ""
        for packet in packets:
            if scapy.ICMP in packet and packet[scapy.ICMP].type == 8:  # ICMP Request
                payload = bytes(packet[scapy.Raw].load).decode("utf-8", errors="ignore")
                if payload:
                    icmp_payload += payload[0]  # Obtener el primer carácter

        print(f"Mensaje cifrado: {icmp_payload}\n")

        for shift in range(1, 26):
            decrypted_message = cesar_decrypt(icmp_payload, shift)
            if is_plausible(decrypted_message):
                print(f"Plausible (Shift {shift}): \033[92m{decrypted_message}\033[0m")
            else:
                print(f"No plausible (Shift {shift}): {decrypted_message}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python programa.py archivo.pcapng")
    else:
        filename = sys.argv[1]
        main(filename)



