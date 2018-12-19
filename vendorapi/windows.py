class WindowsMessageGateway(object):
    """
    WindowsMessageGateway reads messages from the operating system.
    """
    def last_os_message(self):
        """
        :return: the last message from your beloved OS.
        """
        return ("You have 5 minutes to finish your work before I install "
               "updates. You can't postpone")
