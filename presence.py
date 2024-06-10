#!/usr/bin/env python3.11

import pypresence
import os
import time

client = os.getenv("DISCORD_APP_CLIENT")
RPC = pypresence.Presence(client)

RPC.connect()

starting_time=time.time()
RPC.update(state="WORKING...", party_size=[1,1], large_text="Coding!", details="Creating awesome projects!",
           start=int(starting_time))
print("ALR CONNECTED SUCCESSFULLY!")
while True:
    time.sleep(15)
