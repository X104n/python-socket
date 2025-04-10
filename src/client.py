import socket

# Server configuration (where to connect)
SERVER_IP = '10.0.3.4'
SERVER_PORT = 5555
BUFFER_SIZE = 1024

# Create socket (AF_INET = IPv4, SOCK_STREAM = TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")
    
    # Send message to server
    message = "Hello from client!"
    client_socket.send(message.encode('utf-8'))
    print(f"Sent message: {message}")
    
    # Receive response from server
    response = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    print(f"Response from server: {response}")
    
except ConnectionRefusedError:
    print(f"Connection to {SERVER_IP}:{SERVER_PORT} refused. Is the server running?")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close socket
    client_socket.close()