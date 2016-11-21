'''
This file creates a saved building where you are.

python load_building.py -n <name>
'''

import argparse, json, os
from mcpi.minecraft import Minecraft


parser = argparse.ArgumentParser ()
parser.add_argument ( "-n", action='store', dest='name', type=str,
    help="The name of the building you want to recreate." )
args = parser.parse_args ()

mc = Minecraft.create ()

def build_structure ( x, y, z, structure ):

    x_start = x
    z_start = z

    for row in structure:

        for column in row:

            for block in column:
                mc.setBlock ( x, y, z, block )
                z += 1

            x += 1

            z = z_start

        y += 1

        x = x_start

full_filename = os.path.join ( os.path.dirname ( __file__ ), 'data',
    'structures', args.name + '.json' )

with open ( full_filename, 'r' ) as f:
    structure = json.loads ( f.read () )

pos = mc.player.getTilePos ()
x = pos.x
y = pos.y
z = pos.z

build_structure ( x, y, z, structure )
