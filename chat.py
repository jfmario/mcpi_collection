'''
This file asks you to type something to send to the chat.

python chat.py
'''

from mcpi.minecraft import Minecraft

mc = Minecraft.create ()

message = input ( "Message: " )
mc.postToChat ( message )

