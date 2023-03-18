# """
#     ==================================================================
#         Module Name:  configparser.py
#         Program Desc: It exposes the configuration defined in the config file.
#     ==================================================================
#
#     ==================================================================
#         Author:      Sampanna Sharma
#         Created on:  2023-03-18
#     ==================================================================
#     Modification History
#     ==================================================================
#         Modified by               Modified on           Modifications
#         ------------              --------------        --------------
#
#     ==================================================================
# """

import yaml

def read_yalm(file_path):
    """parses the config file

    Parameters
    ----------
    file_path : string
        path of the config file

    Returns
    -------
    dict
        config content
    """
    try: 
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
        
    except FileNotFoundError:
        print("ERROR: env.yml doesn't exists !!!")
        raise

    except (yaml.scanner.ScannerError, yaml.parser.ParserError):
        print("ERROR: env.yml parsing failed")
        raise
 


CONFIG = read_yalm('config/env.yml')

if __name__ == '__main__':
    print(CONFIG)