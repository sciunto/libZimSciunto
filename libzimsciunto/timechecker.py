#!/usr/bin/env python

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>


import shelve
from contextlib import closing
import os
import time

class TimeChecker():
    """
    Manage a time database to keep track of date of modifications

    :param timedb: time database filepath
    :param zimroot: filepath of the zim root directory
    """
    def __init__(self, timedb, zimroot):
        self.timedb = os.path.expanduser(timedb)
        self.zimroot = zimroot

    def set_time(self, filename):
        """
        Put the current time in the database for the filename
    
        :param filename: filename
        """
        with closing(shelve.open(self.timedb)) as database:
            database[filename] = time.time()
    
    
    def get_file_modif_status(self, filename):
        """ 
        Return the file status

        Check if the file changed
        True: The file changed in the mean time
        True: if we don't know
        False: The file is the same.
    
        :param filename: filename
        """
        with closing(shelve.open(self.timedb)) as database:
            try:
                previous_time = database[filename]
            except KeyError:
                #We don't know...
                return True
    
        if os.path.getmtime(os.path.join(self.zimroot, filename)) < previous_time:
            return False
        else:
            return True

if __name__ == '__main__':
    pass
