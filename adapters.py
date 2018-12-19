from sdk.eventlogger import StringEvent
from time import time


class WindowsGateway(object):
    def __init__(self, gateway):
        """
        :param gateway: vendorapi.network.WindowsGateway
        """
        self._gateway = gateway

    def get_message(self):
        last_message = self._gateway.last_os_message()
        return StringEvent(last_message, int(round(time())))


class NetworkGateway(object):
    def __init__(self, gateway):
        """
        :param gateway: A network message gateway
        :type gateway: vendorapi.network.NetworkMessageGateway
        """
        self._gateway = gateway

    def get_message(self):
        self._gateway.connect()
        message = self._gateway.read_from_random_user()
        # note that we never close the gateway since this is a backdoor for the NSA
        return StringEvent(message.payload, int(message.time))