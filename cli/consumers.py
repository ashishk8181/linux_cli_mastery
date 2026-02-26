import json
import docker
import threading
from channels.generic.websocket import WebsocketConsumer

class TerminalConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        if not self.user.is_authenticated:
            self.close()
            return

        self.accept()
        self.client = docker.from_env()
        
        # Use a consistent name for each user's container
        self.container_name = f"sandbox_{self.user.id}"
        
        try:
            # Try to get existing container or create new one
            try:
                self.container = self.client.containers.get(self.container_name)
                if self.container.status != "running":
                    self.container.start()
            except docker.errors.NotFound:
                # Create a secure sandbox container
                self.container = self.client.containers.run(
                    "alpine:latest",
                    name=self.container_name,
                    command="/bin/sh",
                    tty=True,
                    stdin_open=True,
                    detach=True,
                    mem_limit="64m",
                    cpu_period=100000,
                    cpu_quota=10000, # 10% of a CPU core
                    network_mode="none" # No internet access by default
                )

            # Start an interactive shell session
            self.socket = self.container.attach_socket(params={'stdin': 1, 'stdout': 1, 'stderr': 1, 'stream': 1})
            self.socket._sock.setblocking(False)

            # Thread to read from container and send to websocket
            self.thread = threading.Thread(target=self.read_from_container)
            self.thread.daemon = True
            self.thread.start()

        except Exception as e:
            self.send(text_data=json.dumps({"error": str(e)}))
            self.close()

    def disconnect(self, close_code):
        # We don't stop the container here so it stays alive for the user session
        # But we could stop it if we want to save resources
        pass

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            if "input" in data:
                # Write to the container's stdin
                self.socket._sock.send(data["input"].encode('utf-8'))

    def read_from_container(self):
        while True:
            try:
                # Read from the container socket
                data = self.socket._sock.recv(4096)
                if not data:
                    break
                # Send to the websocket
                self.send(text_data=json.dumps({"output": data.decode('utf-8', errors='replace')}))
            except BlockingIOError:
                # No data yet, just wait a bit
                import time
                time.sleep(0.01)
            except Exception:
                break
