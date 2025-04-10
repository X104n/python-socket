import socket

# Server configuration
SERVER_IP = '10.0.3.4'
SERVER_PORT = 5555
BUFFER_SIZE = 1024

# Create socket (AF_INET = IPv4, SOCK_STREAM = TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow reuse of address
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the specified IP and port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Listen for connections (maximum 5 queued connections)
server_socket.listen(5)
print(f"Server listening on {SERVER_IP}:{SERVER_PORT}...")

try:
    while True:
        # Accept client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # Receive message from client
        message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        print(f"Message from client: {message}")
        
        # Send response
        response = f"Server received: {message}"
        client_socket.send(response.encode('utf-8'))
        
        # Close client connection
        client_socket.close()
        
except KeyboardInterrupt:
    print("Server shutting down...")
finally:
    server_socket.close()