'''
This file asks you to go to two corners of a region to save it.

python save_building.py <name>
'''

import argparse, json, os
from mcpi.minecraft import Minecraft

parser = argparse.ArgumentParser ()
parser.add_argument ( "name", metavar='N', type=str,
    help="The name that you want to save this building as." )
args = parser.parse_args ()

mc = Minecraft.create ()

def sort_pair ( value1, value2 ):
    if value1 > value2:
        return value2, value1
    else:
        return value1, value2

def copy_structure ( x1, y1, z1, x2, y2, z2 ):

    x1, x2 = sort_pair ( x1, x2 )
    y1, y2 = sort_pair ( y1, y2 )
    z1, z2 = sort_pair ( z1, z2 )

    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    structure = []

    print ( "Please wait..." )

    for row in range ( height ):

        structure.append ( [] )

        for column in range ( width ):

            structure [row].append ( [] )

            for depth in range ( length ):
                block = mc.getBlock ( x1 + column, y1 + row, z1 + depth )
                structure [row] [column].append ( block )

    return structure

raw_input ( "Move to position 1 and press Enter" )

pos1 = mc.player.getTilePos ()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

raw_input ( "Move to position 2 and press Enter" )

pos2 = mc.player.getTilePos ()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

structure = copy_structure ( x1, y1, z1, x2, y2, z2 )

full_filename = os.path.join ( os.path.dirname ( __file__ ), 'data',
    'structures', args.name + '.json' )

with open ( full_filename, 'w' ) as o:
    o.write ( json.dumps ( structure ) )
