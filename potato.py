class PotatoLogger(object):
    def __init__(self, database_logger):
        self.logger = database_logger

    def receive(self, event):
        """
        :type event: sdk.eventlogger.StringEvent
        """
        if 'potato' not in event.msg.lower():
            return

        self.logger.receive(event)
