'''
This file teleports you to a location saved under a given name.

python goto_location.py -n <name>
'''

import argparse, json, os
from mcpi.minecraft import Minecraft

parser = argparse.ArgumentParser ()
parser.add_argument ( "-n", action='store', dest='name', type=str,
    help="The name of the location that you want to goto." )
    
args = parser.parse_args ()

mc = Minecraft.create ()

with open ( os.path.join ( os.path.dirname ( __file__ ), 'data', 'locations',
    args.name + '.json' ), 'r' ) as f:
        
    location = json.loads ( f.read () )
    
mc.player.setTilePos ( location ['x'], location ['y'], location ['z'] )