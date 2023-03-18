# """
#     ==================================================================
#         Module Name:  logger.py
#         Program Desc: It logs the processes involved in validation.
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
from datetime import datetime
import os
from configparser import CONFIG

class logger:
    def __init__(self) -> None:
        self.log_dir = CONFIG['DIR']['LOG']
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.log_start_ts = datetime.now().strftime("%Y%m%d%H%M%S")
        self.log_path = os.path.join(self.log_dir, self.log_start_ts + ".log")
    
    def __enter__(self):
        print(os.path.abspath(os.curdir))
        self.log_file = open(self.log_path, 'w')
        return self
    
    def __exit__(self, exc_type, exc_value, tb): 
        self.log_file.close()
        
        if exc_type is not None:
            print(exc_type, exc_value, tb)
            return False
        
        return True
    
    def write(self, message):
        now = datetime.now()
        self.log_file.write(str(now))
        self.log_file.write(": ")
        self.log_file.write(message)
        self.log_file.write("\n")
        self.log_file.flush()

if __name__ == '__main__':
    with logger() as lg:
        lg.write('Hello')
