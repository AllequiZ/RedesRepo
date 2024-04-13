from scapy.all import ARP, rdpcap

def read_arp_packets(file_path):
    packets = rdpcap(file_path)
    arp_packets = [pkt for pkt in packets if pkt.haslayer(ARP)]
    return [{
        "Source IP": pkt[ARP].psrc,
        "Destination IP": pkt[ARP].pdst,
        "Operation": "request" if pkt[ARP].op == 1 else "reply"
    } for pkt in arp_packets]

# Exemplo de uso:
arp_data = read_arp_packets("caminho_para_seu_arquivo.pcap")
print(arp_data[:10])  # Imprime as primeiras 10 entradas


from fastapi import FastAPI

app = FastAPI()

@app.get("/arp-data")
async def get_arp_data():
    return read_arp_packets("caminho_para_seu_arquivo.pcap")
