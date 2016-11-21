'''
This file shows some block types and corresponding ids.

python blocks.py
'''

import os

with open ( os.path.join ( os.path.dirname ( __file__ ), 'data', 'blocks',
    'ids.txt' ), 'r' ) as f:
    
    for line in f:
        print ( line.strip () )
