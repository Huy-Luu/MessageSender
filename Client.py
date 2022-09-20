import socket
import time
from MessageSender import Sender
from Point import Point

client = Sender()

client.connect("127.0.0.1", 10000)

p = Point(2,3)

while(1):
    #client.sendMessage("Test tag", "Test message")
    client.sendCoordinates(p)
    time.sleep(1)
