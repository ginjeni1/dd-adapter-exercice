
class StringEvent(object):
    def __init__(self, msg, timestamp):
        """
        :param msg (string): A message that happened
        :param timestamp (int): The time at which this message happened
        """
        self.timestamp = timestamp
        self.msg = msg


class EventLogger(object):
    """
    EventLogger will write into the event buffer the events it receives.
    """
    def receive(self, event):
        if not isinstance(event.timestamp, int):
            raise ValueError("timestamp must be an integer")
        if not isinstance(event.msg, str):
            raise ValueError("msg must be an integer")

        print("Event : {} : {}".format(
            event.timestamp,
            event.msg)
        )

