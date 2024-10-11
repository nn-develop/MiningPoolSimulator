import requests
import os
import time
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get the server URL from the environment variable
server_url = os.getenv("SERVER_URL")

if server_url is None:
    raise ValueError("SERVER_URL is not set in the .env file")

# Function to check server availability
# def wait_for_server(url, timeout=60):
#     print(f"Waiting for the server to be available at: {url}")
#     start_time = time.time()
#     while True:
#         try:
#             response = requests.get(f"{url}/connect")
#             if response.status_code == 200:
#                 print("Server is available!")
#                 break
#         except requests.exceptions.ConnectionError:
#             pass
        
#         if time.time() - start_time > timeout:
#             raise TimeoutError(f"Server at {url} is not available after {timeout} seconds.")
        
#         print("Server not available, retrying...")
#         time.sleep(5)

# # Wait for the server to be available
# wait_for_server(server_url)

# Send request to the server
# response = requests.get(f"{server_url}/connect")

# Print the response
# print(response.json())
