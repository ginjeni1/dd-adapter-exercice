import sdk
import vendorapi
from adapters import (
    NetworkGateway,
    WindowsGateway,
)


class MyApp(object):
    def __init__(self, gateways, event_logger):
        self._gateways = gateways
        self._event_logger = event_logger

    def connect_and_log_messages(self):
        for gateway in self._gateways:
            event_logger.receive(gateway.get_message())


if __name__ == '__main__':
    net_gateway = vendorapi.NetworkMessageGateway("pttp://perdu.com")
    windows_gateway = vendorapi.WindowsMessageGateway()
    event_logger = sdk.EventLogger()

    app = MyApp([NetworkGateway(net_gateway), WindowsGateway(windows_gateway)], event_logger)
    app.connect_and_log_messages()