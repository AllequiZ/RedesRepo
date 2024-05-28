from fastapi import FastAPI
from scapy.all import rdpcap, UDP
from typing import List, Dict

app = FastAPI()

# Função para ler o arquivo pcap e retornar informações sobre os pacotes UDP
def read_pcap(file_path: str) -> List[Dict[str, str]]:
    packets = rdpcap(file_path)
    udp_packets = [packet for packet in packets if UDP in packet]
    packet_info = []
    for packet in udp_packets:
        info = {
            'source_ip': packet[IP].src,
            'destination_ip': packet[IP].dst,
            'source_port': packet[UDP].sport,
            'destination_port': packet[UDP].dport,
        }
        packet_info.append(info)
    return packet_info

# Rota para obter informações sobre os pacotes UDP no arquivo pcap
@app.get("/udp_packets")
def get_udp_packets():
    packet_info = read_pcap('file/udp.pcap')
    return packet_info