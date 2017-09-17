import re
from . import github_api


# Initiaize git hub interface
REPO_URL = ''
github_interface = github_api.GitHubInterface(REPO_URL)


def get_preceding_function(file_pointer):
    """
    Get the enclosing function for the current position in file
    @file_pointer: (File) Pointer to file in which the code resides, 
                    seeked to the exact line of the code for which the enclosed function needs to be fetched
    """

    pass


def fetch_file(file_path, line_no):
    """
    Get the file from git hub and seek to the given line number's end
    @file_path: (String) Relative path of the file to the root directory of the repo
    @line_no: (Integer) Line no in file to which the pointer needs to point
    """

    file = github_interface.get_file_from_repo(file_path)
    file.seek(line_no)



def __main__():
    
    file_path = ''
    line_no = 0
    owner = ''

    file = fetch_file(file_path, 0)

    enclosing_function = get_preceding_function(file)

    save_owner(enclosing_function, owner)


    


