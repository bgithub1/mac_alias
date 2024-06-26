#!/usr/bin/env python
# coding: utf-8

# ## Get all Alias files on a macOS system
# 
# ### Installation:
# Clone and create a Virtualenv using the requirements.txt file in the project root
# 
# ### Usage:
# When using the `alias_search.py` python module, the results will be placed in csv files in the folder `mac_alias/mac_alias/temp_folder`.
# #### To find all alias files on your macOS system, and their underlying paths:
# ```
# cd mac_alias/mac_alias/notebooks
# python3 alias_search.py
# ```
# 
# #### To find alias files that are limited to start from two folders up:
# ```
# cd mac_alias/mac_alias/notebooks
# python3 alias_search.py --onlyin  '../..'
# ```
# 
# After running either of these commands, open the folder `mac_alias/mac_alias/temp_folder` and find the csv folder whose name is:
# ```
# results_YYYYmmddHHMMSS.csv
# ```

# In[201]:


import xattr
import re
from Foundation import *
import mdfind
import os
import sys
import string
import pdb
import traceback
import pandas as pd
import datetime
import pathlib


# In[78]:


def get_bookmarkData(alias_path):
  alias_url = NSURL.fileURLWithPath_(alias_path)
  bookmarkData, error = NSURL.bookmarkDataWithContentsOfURL_error_(alias_url, None)
  return bookmarkData

def get_target_of_bookmarkData(bookmarkData):
  if bookmarkData is None:
    return None
  options = NSURLBookmarkResolutionWithoutUI | NSURLBookmarkResolutionWithoutMounting
  resolved_url, stale, error = \
    NSURL.URLByResolvingBookmarkData_options_relativeToURL_bookmarkDataIsStale_error_(
      bookmarkData, options, None, None, None)
  return resolved_url.path()


def create_bookmarkData(new_path):
  new_url = NSURL.fileURLWithPath_(new_path)
  options = NSURLBookmarkCreationSuitableForBookmarkFile
  new_bookmarkData, error = \
    new_url.bookmarkDataWithOptions_includingResourceValuesForKeys_relativeToURL_error_(
      options, None, None, None)
  return new_bookmarkData

    


# In[ ]:





# In[ ]:





# In[180]:


def main(onlyin=None):
    q = "kMDItemKind='Alias'" 
    if onlyin is not None:
        alias_paths = mdfind.mdfind(['-onlyin',os.path.abspath(onlyin),'kMDItemKind==Alias']).split('\n')
    else:
        alias_paths = mdfind.query(q)
    
    list_dict_bookmark_data = []
    for ap in alias_paths:
        bmd = get_bookmarkData(ap)
        tbmd = 'None'
        error = None
        if bmd is not None:
            try:
                tbmd = get_target_of_bookmarkData(bmd)
            except:
                error = traceback.format_exc()
        list_dict_bookmark_data.append({'alias':ap,'underlying':tbmd})
    return list_dict_bookmark_data  

# get bash command line args
#  each arg should be in the form:
#  --arg_name arg_value
# like:  --save_tax_curr_fiscal_year True --save_tax_all True
def get_arg(arg_id):
    arg_indices = [i for i,_ in enumerate(sys.argv) if sys.argv[i]==arg_id]
    if len(arg_indices) !=1:
        return None
    return sys.argv[arg_indices[0]+1]


# In[199]:


# main(onlyin='../../')
if __name__=='__main__':
    onlyin = get_arg('--onlyin')
    results = main(onlyin=onlyin)
    df = pd.DataFrame(results)
    max_width = max([len(v) for v in df.alias.values])
    pd.options.display.max_colwidth = max_width
    n = datetime.datetime.now()
    y = n.year
    mn = n.month
    d = n.day
    h = n.hour
    m = n.minute
    s = n.second
    t = n.strftime('%Y%m%d%H%M%S')
    out_folder = get_arg('--out_folder')
    if out_folder is None:
        out_folder = pathlib.Path.home()
        
    df.to_csv(f"{out_folder}/results_{t}.csv",index=False)
    # for alias,underlying in results.items():
    #     print(alias,underlying)


# In[161]:


# print(mdfind.mdfind(['-onlyin',os.path.abspath('../../../'),'kMDItemContentType==public.shell-script']))
# print(mdfind.mdfind(['-onlyin',os.path.abspath('..'),'kMDItemKind==Alias']))


# In[200]:


# !jupyter nbconvert --to script alias_search.ipynb


# In[ ]:





# In[ ]:




