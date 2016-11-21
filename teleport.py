'''
This file moves you to a specified location in x/y/z coordinates.
Note that the Y-coordinate is up and down.

python teleport.py -x X -y Y -z Z
'''

import argparse
from mcpi.minecraft import Minecraft

parser = argparse.ArgumentParser ()
parser.add_argument ( "-x", action='store', dest='x', type=int, default=0,
    help="The east-west coordinate that you want to go to. Defaults to 0." )
parser.add_argument ( "-y", action='store', dest='y', type=int, default=120,
    help="The vertical height that you want to go to. Defaults to 120 (high)." )
parser.add_argument ( "-z", action='store', dest='z', type=int, default=0,
    help="The north-south coordinate that you want to go to. Defaults to 0." )

args = parser.parse_args ()

mc = Minecraft.create ()
mc.player.setTilePos ( args.x, args.y, args.z )