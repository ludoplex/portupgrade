import os

class PkgDBTools:
    def __init__(self):
        self.db_dir = None
        self.db_driver = None

    def remove_lock(self, file_name, force=False):
        if file_name is not None and os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            with open(file_name, 'r') as file:
                pid, mode = file.readline().split(' ')
            if int(pid) == os.getpid() or force:
                os.unlink(file_name)

    def get_db_dir(self):
        if self.db_dir is None:
            self.set_db_dir(None)
        return self.db_dir

    def get_db_driver(self):
        if self.db_driver is None:
            self.set_db_driver(None)
        return self.db_driver

    def set_db_driver(self, new_db_driver):
        self.db_driver = new_db_driver
