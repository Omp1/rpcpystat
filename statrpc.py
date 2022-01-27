import psutil; import time
from pypresence import Presence
from gpuinfo import GPUInfo

client_id = 'BRUH'  # Fake ID, put your real one here
RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop


while True:  # The presence will stay on as long as the program is running
    cpu_per = int(psutil.cpu_percent()) # Get CPU Usage
    gpu_per = GPUInfo.gpu_usage()[0][0]
    mem = psutil.virtual_memory()
    mem_per = int(psutil.virtual_memory().percent)
    print(RPC.update(details="RAM: " + str(mem_per) + "%,  " + "CPU: " + str(cpu_per) + "%,  " + "GPU: " + str(gpu_per) + "%" , state="Why did I even make this?"))  # Set the presence
    time.sleep(3) # Can only update rich presence every 15 seconds