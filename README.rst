CopyFlag
=============================================================================
Introduction
-----------------------------------------------------------------------------

A package to search and copy a flag to the clipboard in the context of **CTFs**.

Import module locally
-----------------------------------------------------------------------------
in the folder where `setup.py` is located, with the shell type `pip install -e .`

Usage
-----------------------------------------------------------------------------

Fastest usage is

.. code-block:: python
  
  # first import all
  from copyflag import *

  # You will have CopyFirstFlag class that needs a flag regex when initializing
  # default is r'flag\{.*?\}'
  copyflag = CopyFirstFlag(flagRegex=r'flag\{.*?\}')



  # then when you have a text that (may) contain a flag
  r = requests.get('https://website/url')
  # this searches for the flag prints it and copies it to the clipboard
  flag = copyflag.copy(r.text) # flag will be the string found or None
  # this searches for the flag, and only copies it to the clipboard
  flag = copyflag.copy(r.text, printf=False) # flag will be the string found or None

  # if you have a logger or a print function you can pass it to the class
  flag = copyflag.copy(r.text, printf=logger.info)

  # or you can set the print function for the class
  copyflag.set_printf(logger.info)
  # or you can specify it at the class constructor first
  copyflag = CopyFirstFlag(printf=logger.info)
  # then you can just use copy method to print the flag with your custom print function
  flag = copyflag.copy(r.text)

  # only search the flag without copying to the clipboard nor printing it.
  flag = copyflag.search(r.text) # flag will be the string found or None



*Installation*
-----------------------------------------------------------------------------
This package is to be yet published