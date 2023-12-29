import pyperclip
import re
from copyflag.known import default

class CopyFirstFlag:
    """
    Class to copy to clipboard the first flag found from a text.
    """

    # default flag regex
    flag_regex = default
    printf = print

    # constructor
    def __init__(self, flag_regex=flag_regex, printf=printf):
        """
        Constructor for CopyFirstFlag.
    
        Parameters:
        - flag_regex (str)[optional]: The regex to search for the flag. default is `r'flag\{.*?\}'`.
        - printf (function)[optional]: The custom print function to use to print the flag. default is `print`.
        """
        # function body

        if (flag_regex != None):
            self.flag_regex = flag_regex
        if (printf != None and printf != print):
            self.printf = printf

    # set printf function
    def set_printf(self, printf:any):
        """
        Set the custom print function to use to print the flag.

        Parameters:
        - printf (function): The custom print function to use to print the flag.
        """
        # function body
        self.printf = printf
  
    # search for flag in text
    def search(self, text:str):
        """
        Search for the flag in the text.

        Parameters:
        - text (str): The text to search in.

        Returns:
        str|None: The flag if found, None otherwise.
        """
        # function body
        match = re.search(self.flag_regex, text)
        if match is not None:
            flag = match.group(0)
            return flag
        return None
        
    # copy flag to clipboard
    def copy(self, text:str, printf=printf):
        """
        Copy the flag to the clipboard, and eventually prints it.

        Parameters:
        - text (str): The text to search in.
        - printf (bool|function)[optional]: If `True` or a valid print function, print the flag with standard print function, if `None` or `False` pass. Default is `print`.
          You can pass your custom print function also.

        Returns:
        str|None: The flag if found, None otherwise.
        """
        # function body
        flag = self.search(text)
        if (flag):
            pyperclip.copy(flag)
            try:
                if (printf is False or printf is None):
                    pass
                elif (printf is True):
                    self.printf(flag)
                else:
                    printf(flag)
            except:
                # if printf or self.printf is not a function
                # we assume the user wants to print the flag anyway
                print(flag)
            return flag
        return None