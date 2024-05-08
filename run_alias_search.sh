# find all alias files and their orignal files.
# The results of the search will be a csv file that will
#   be saved to your home folder.

# To find all alias files on your computer:
# bash run_alias_search.sh

# To find all alias files starting from the folder my_folder_full_path:
# bash run_alias_search.sh --onlyin my_folder_full_path
#
# To find all alias files starting from the folder my_folder_full_path,
#   but put the results in this folder:
# bash run_alias_search.sh --onlyin my_folder_full_path --out_folder $(pwd)
# You need to use $(pwd), unless you use the full path of your folder

python3 mac_alias/notebooks/alias_search.py "$@"