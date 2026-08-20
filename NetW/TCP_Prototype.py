class TCPDemo:
    def __init__(self):
        self.seq = 1000
        self.connected = False

    def handshake(self):
        print("Client -> Server: SYN")
        print("Server -> Client: SYN-ACK")
        print("Client -> Server: ACK")
        self.connected = True
        print("TCP connection established\n")

    def send_text(self, text):
        if not self.connected:
            print("Connection not established")
            return

        print(f"User text: {text}")
        print("Splitting text into TCP segments...")

        chunk_size = 5
        parts = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

        for i, part in enumerate(parts):
            packet = {
                "seq": self.seq,
                "ack": 0,
                "flags": "PSH, ACK",
                "data": part
            }
            print(f"\nSending segment {i+1}: {packet}")
            print(f"Server -> Client: ACK {self.seq + len(part)}")
            self.seq += len(part)

        print("\nAll text sent successfully")

    def close(self):
        print("\nClient -> Server: FIN")
        print("Server -> Client: FIN-ACK")
        print("Client -> Server: ACK")
        self.connected = False
        print("TCP connection closed")


text = input("Enter text: ")

tcp = TCPDemo()
tcp.handshake()
tcp.send_text(text)
tcp.close()
