import socket
from Point import Point

class Sender:
    def __init__(self):
        self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        print("Initiated a sender")
        self.toSend = ""

    def connect(self, host, port):
        self.sock.connect((host, port))

    def sendMessage(self, tag, message):
        self.toSend = tag + "," + message
        self.sock.send(str.encode(self.toSend))

    def sendCoordinates(self, Point):
        self.toSend = str(Point.x) + " " + str(Point.y)
        self.sock.send(str.encode(self.toSend))

    def sendWayPointStatus(self):
        self.toSend =""
        #send out if that waypoint reached or not