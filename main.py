import sdk
import vendorapi


class MyApp(object):
    def __init__(self, gateways, event_logger):
        self._gateways = gateways
        self._event_logger = event_logger

    def connect_and_log_messages(self):
        for gateway in self._gateways:
            # !? They all have distinct interface...
            # TODO : Send the information to the event_logger somehow
            pass


if __name__ == '__main__':
    net_gateway = vendorapi.NetworkMessageGateway("pttp://perdu.com")
    windows_gateway = vendorapi.WindowsMessageGateway()
    event_logger = sdk.EventLogger()

    app = MyApp([net_gateway, windows_gateway], event_logger)
    app.connect_and_log_messages()
