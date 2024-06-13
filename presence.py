#!/usr/bin/env python3.11

# Importing libraries
import pypresence
import os 
import time
import psutil
import threading

# TODO: Maybe add some more functionality

# Declaring variables
client = os.getenv("DISCORD_APP_CLIENT")

# Creating functions
def is_discord_running() -> bool:
    for proc in psutil.process_iter(["pid","name"]):
        try:
            if proc.name().lower() == "discord":
                print("dis is running")
                return True
        except (psutil.NoSuchProcess, psutil.ZombieProcess, psutil.AccessDenied):
            pass
    print("discord is not running")
    return False

def run_discord():
    os.system("discord 1>/dev/null 2>/dev/null &")

def presence_connect():
    RPC=pypresence.Presence(client)
    RPC.connect()
    starting_time=time.time()
    RPC.update(state="WORKING...", party_size=[1,1], start=int(starting_time), large_text="Coding...",
               small_text="Creating awesome projects!!")

# Main function
def main():
    is_D_running = is_discord_running()
    if is_D_running == False:
        discord_thread = threading.Thread(target=run_discord)
        discord_thread.start()
        discord_thread.join()
    time.sleep(15)
    presence_thread = threading.Thread(target=presence_connect)
    presence_thread.start()
    while True:
        time.sleep(30)

# Main file entry
if __name__ == "__main__":
    main()


