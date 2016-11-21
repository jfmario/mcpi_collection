'''
This file saves your current location under a given name.

python save_location.py <name>
'''

import argparse, json, os
from mcpi.minecraft import Minecraft

parser = argparse.ArgumentParser ()
parser.add_argument ( "name", metavar='N', type=str,
    help="The name that you want to save this location as." )
    
args = parser.parse_args ()

mc = Minecraft.create ()
pos = mc.player.getTilePos ()

x = pos.x
y = pos.y
z = pos.z

location = { 'x': x, 'y': y, 'z': z }

with open ( os.path.join ( os.path.dirname ( __file__ ), 'data', 'locations',
    args.name + '.json' ), 'w' ) as o:
        
    o.write ( json.dumps ( location ) )
