import random


class NotConnected(Exception):
    def __init__(self, *args, **kwargs):
        super(NotConnected, self).__init__(*args, **kwargs)


class OttpResponse(object):
    def __init__(self, payload, time):
        self.payload = payload
        self.time = time


class NetworkMessageGateway(object):
    """
    NetworkMessageGameway gateway connects to a random user!? on the
    internet and returns an response is ottp.
    """
    def __init__(self, url):
        self._is_connected = False
        self._url = url

    def connect(self):
        """call prior reading"""
        self._is_connected = True

    def read_from_random_user(self):
        if not self._is_connected:
            raise NotConnected("you are not connected")

        return OttpResponse(
            payload="I love bacon;",
            time=str(random.randint(42000000, 999999999))
        )

