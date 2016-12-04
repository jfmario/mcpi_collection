# MCPI Collection #

A collection of `mcpi` demo files.

## `chat.py` #

```
python chat.py
```

This program will prompt you for a message that will post to the game chat.

## `airlift.py` #

```
python airlift.py
```

This program will teleport you to way up in the sky above the middle of the 
game map.

## `go_up.py` #

```
python go_up.py -y <n>
```

This program will teleport you up *n* number of spaces up from your current
location.

Example:


```
python go_up.py -y 10
```

This will teleport you up 10 spaces from wherever you are.

## `teleport.py` #

```
python teleport.py -x <x> -y <y> -z <z>
```

This program will teleport you to the given coordinates.

Example:

```
python teleport.py -x 120 -y 20 -z 120
```


## `save_location.py` #

```
python save_location.py -n <name>
```

This program saves your current location under a given name.
Please note that the name should not contain any spaces.

It will appear as a JSON file under `data/locations/`.

Example:

```
python save_location.py -n myhome
```

## `goto_location.py` #

```
python goto_location.py -n <name>
```

This program teleports you to a saved location.

Example:

```
python goto_location.py myhome
```

## `save_building.py` #

```
python save_building.py -n <name>
```

This program will prompt you to go one corner of a region and hit ENTER,
then go to the opposite corner and hit ENTER. When you do everything in between
those two corders will be saved to a JSON file under `data/structures/`.

## `load_building.py` #

```
python load_building.py -n <name>
```

This program will recreate a saved building starting from your current location.

## `blocks.py` #

```
python blocks.py
```

For your convenience, this program prints out block types associated with ids.
