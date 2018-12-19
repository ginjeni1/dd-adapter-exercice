
class NotConnected(Exception):
    def __init__(self, *args, **kwargs):
        super(NotConnected, self).__init__(*args, **kwargs)


class StringDatabase(object):
    """
    StringDataBase store strings in a file, one per lines. If the file
    doesn't exist, it's created, if not, content is added to it.
    """

    def __init__(self, database_file):
        """
        :param database_file: (string) name of the file to write in
        """
        self._database_file = database_file
        self._file_handle = None

    def open(self):
        """open the database file for append"""
        self._file_handle = open(self._database_file, "a")

    def insert(self, string):
        """
        :param string: string to insert in the database
        """
        if not self._file_handle:
            raise NotConnected("call open() prior insertion")
        self._file_handle.write(string + "\n")

    def close(self):
        self._file_handle.close()

    def __delete__(self, instance):
        print("database closed")
        self.close()


class StringDatabaseLogger(object):
    def __init__(self, database):
        """
        :type database: StringDatabase
        """
        self.database = database

    def receive(self, event):
        """
        :type event: sdk.eventlogger.StringEvent
        """
        # composed_event = event.msg + event.timestamp
        self.database.open()
