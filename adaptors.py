import time

import sdk


class WindowsAdapter(object):
    def __init__(self, window_message_gateway):
        self._delegated = window_message_gateway

    def get_event(self):
        msg = self._delegated.last_os_message()
        return sdk.StringEvent(msg, int(time.time()))


class NetworkAdapter(object):
    def __init__(self, network_gateway):
        self._delegate = network_gateway

    def get_event(self):
        self._delegate.connect()
        pttp = self._delegate.read_from_random_user()
        return sdk.StringEvent(pttp.payload, int(pttp.time))
