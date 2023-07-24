# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 08:12:59 2023

@author: Navi
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

# s.bind() # HostName and Port number (address) will be binded to server.

# s.listen() #Starts the Transmission Control Protocol listener.

# s.accept() # Accepts Client Connection

# s.send() #Send TCP message

# s.recv() # Recieve TCP message 

# s.close() # Close the socket




