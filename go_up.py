'''
This file moves you up by a given number of blocks.

python go_up.py -y <number=5>
'''

import argparse
from mcpi.minecraft import Minecraft

parser = argparse.ArgumentParser ()
parser.add_argument ( "-y", action='store', dest='y', type=int, default=5,
    help="How high you want to go. Defaults to 5" )
args = parser.parse_args ()

mc = Minecraft.create ()
pos = mc.player.getTilePos ()

x = pos.x
y = pos.y + args.y
z = pos.z

mc.player.setTilePos ( x, y, z )


