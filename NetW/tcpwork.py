# TCP-like demo in Python
# This is NOT real TCP. It only simulates how TCP works.

class TCPDemo:
    def __init__(self):
        # Starting sequence number
        self.seq = 1000
        # Connection status
        self.connected = False

    def handshake(self):
        # Simulate the 3-way handshake
        print("Client -> Server: SYN")
        print("Server -> Client: SYN-ACK")
        print("Client -> Server: ACK")
        self.connected = True
        print("TCP connection established\n")

    def send_text(self, text):
        # Stop if connection is not open
        if not self.connected:
            print("Connection not established")
            return

        # Show original text
        print(f"User text: {text}")

        # Split text into small chunks like TCP segments
        print("Splitting text into TCP segments...")
        chunk_size = 5
        parts = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

        # Send each chunk one by one
        for i, part in enumerate(parts):
            # Create a fake TCP segment
            packet = {
                "seq": self.seq,          # Sequence number
                "ack": 0,                 # ACK number (simplified)
                "flags": "PSH, ACK",      # TCP flags
                "data": part              # Text data
            }

            # Print what is being sent
            print(f"\nSending segment {i + 1}: {packet}")

            # Simulate acknowledgment from server
            print(f"Server -> Client: ACK {self.seq + len(part)}")

            # Increase sequence number by number of bytes sent
            self.seq += len(part)

        print("\nAll text sent successfully")

    def close(self):
        # Simulate TCP connection closing
        print("\nClient -> Server: FIN")
        print("Server -> Client: FIN-ACK")
        print("Client -> Server: ACK")
        self.connected = False
        print("TCP connection closed")


# Get text input from user
text = input("Enter text: ")

# Create TCP demo object
tcp = TCPDemo()

# Open connection
tcp.handshake()

# Send user text
tcp.send_text(text)

# Close connection
tcp.close()
