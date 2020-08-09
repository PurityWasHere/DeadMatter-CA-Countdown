from pypresence import Presence
from datetime import datetime
from time import sleep

def GetTime():
    Datetill = str((datetime(2020, 8, 20, 0, 0, 0) - datetime.utcnow()))
    Days = Datetill.split("days")[0].strip(" ")
    Hours = Datetill.split(":")[0].split("days,")[1].strip(" ")
    Minutes = Datetill.split(":")[1]
    Seconds = Datetill.split(":")[2].split(".")[0]
    return('{}D {}H {}M {}S until launch'.format(Days,Hours,Minutes,Seconds))

client_id = "739833131862851596"
RPC = Presence(client_id=client_id)
RPC.connect()
print('Connected To Discord.')
while 1:
    RPC.update(large_image="dm" ,large_text="Using UTC Global Time",details = GetTime())
    sleep(30)