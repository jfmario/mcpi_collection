
import os, sys
sys.path.append ( r'C:\Users\student\Documents\mc_server\Minecraft Tools\Minecraft Tools\minecraftPythonAPI\py3minepi-master' )

from mcpi.minecraft import Minecraft
mc = Minecraft.create ()

import pickle

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

filename = input ( "Structure Name:" )
full_filename = os.path.join ( os.path.dirname ( __file__ ), 'data',
    'structures', filename + '.mcbdg' )

with open ( full_filename, 'rb' ) as fb:
    structure = pickle.loads ( fb.read () )

pos = mc.player.getTilePos ()
x = pos.x
y = pos.y
z = pos.z

build_structure ( x, y, z, structure )
