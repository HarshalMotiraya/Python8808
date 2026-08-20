class TCPConnection:
    def __init__(self):
        self.sequence_number = 0
        self.ack_number = 0
        self.connected = False

    def connect(self):
        print("SYN ->")
        print("<- SYN-ACK")
        print("ACK ->")
        self.connected = True
        print("Connection established")

    def send_data(self, data):
        if not self.connected:
            print("Not connected")
            return

        packet = {
            "seq": self.sequence_number,
            "data": data
        }

        print(f"Sending packet: {packet}")
        print(f"Waiting for ACK for seq {self.sequence_number}")
        print(f"ACK received for seq {self.sequence_number}")

        self.sequence_number += len(data)

    def close(self):
        if self.connected:
            print("FIN ->")
            print("<- FIN-ACK")
            print("ACK ->")
            self.connected = False
            print("Connection closed")


tcp = TCPConnection()
tcp.connect()
tcp.send_data("Hello")
tcp.send_data("World")
tcp.close()
