## Get all Alias files on a macOS system

### Installation:
Clone and create a Virtualenv using the requirements.txt file in the project root

### Usage:
When using the `alias_search.py` python module, the results will be placed in csv files in the folder `mac_alias/mac_alias/temp_folder`.
#### To find all alias files on your macOS system, and their underlying paths:
```
cd mac_alias/notebooks
python3 alias_search.py
```

#### To find alias files that are limited to start from two folders up:
```
cd mac_alias/notebooks
python3 alias_search.py --onlyin  '../..'
```

After running either of these commands, open the folder `mac_alias/mac_alias/temp_folder` and find the csv folder whose name is:
```
results_YYYYmmddHHMMSS.csv
```