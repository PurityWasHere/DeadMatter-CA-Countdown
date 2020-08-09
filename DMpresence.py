from pypresence import Presence
import datetime,time
def GetTime():
    delta = datetime.datetime(2020, 8, 20) - datetime.datetime.now()
    Days = str(delta).split(" ")[0]
    Hours = str(delta).split(",")[1].split(":")[0].strip(" ")
    Minutes = str(delta).split(",")[1].split(":")[1].strip(" ")
    Seconds = str(delta).split(",")[1].split(":")[2].strip(" ").split(".")[0]
    return(Days + "D " +Hours+"H " + Minutes + "M " + Seconds + "S Until Release")

client_id = "739833131862851596"
RPC = Presence(client_id=client_id)
RPC.connect()
print('Connected To Discord.')
while 1:
    RPC.update(large_image="dm" ,large_text="Waiting for Release",details = GetTime())
    time.sleep(30)