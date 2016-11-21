'''
This file lifts the player into the sky above the center of the world.

python airlift.py
'''

from mcpi.minecraft import Minecraft
mc = Minecraft.create ()

mc.player.setTilePos ( 0, 120, 0 )