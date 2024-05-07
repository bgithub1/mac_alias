#!/usr/bin/env python
# coding: utf-8

# ## Get all Alias files on a macOS system

# In[169]:


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





# In[171]:


def main(onlyin=None):
    q = "kMDItemKind='Alias'" 
    if onlyin is not None:
        alias_paths = mdfind.mdfind(['-onlyin',os.path.abspath(onlyin),'kMDItemKind==Alias']).split('\n')
    else:
        alias_paths = mdfind.query(q)
    
    list_dict_bookmark_data = []
    for ap in alias_paths:
        bmd = get_bookmarkData(ap)
        tbmd = None
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


# In[176]:


# main(onlyin='../../')
if __name__=='__main__':
    onlyin = get_arg('--onlyin')
    results = main(onlyin=onlyin)
    df = pd.DataFrame(results)
    max_width = max([len(v) for v in df.alias.values])
    pd.options.display.max_colwidth = max_width
    print(df)
    # for alias,underlying in results.items():
    #     print(alias,underlying)


# In[161]:


# print(mdfind.mdfind(['-onlyin',os.path.abspath('../../../'),'kMDItemContentType==public.shell-script']))
# print(mdfind.mdfind(['-onlyin',os.path.abspath('..'),'kMDItemKind==Alias']))


# In[162]:


# !jupyter nbconvert --to script alias_search.ipynb


# In[ ]:




