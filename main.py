import sdk
import vendorapi
from adaptors import NetworkAdapter, WindowsAdapter


class MyApp(object):
    def __init__(self, gateways, event_log):
        self._gateways = gateways
        self._event_log = event_log

    def connect_and_log_messages(self):
        for gateway in self._gateways:
            self._event_log.receive(gateway.get_event())


if __name__ == '__main__':
    net_gateway = NetworkAdapter(vendorapi.NetworkMessageGateway("pttp://perdu.com"))
    windows_gateway = WindowsAdapter(vendorapi.WindowsMessageGateway())
    event_logger = sdk.EventLogger()

    app = MyApp([net_gateway, windows_gateway], event_logger)
    app.connect_and_log_messages()
