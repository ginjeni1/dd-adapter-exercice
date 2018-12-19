import sdk
import vendorapi
from adapters import (
    NetworkGateway,
    WindowsGateway,
)


class MyApp(object):
    def __init__(self, gateways, loggers):
        self._gateways = gateways
        self._loggers = loggers

    def connect_and_log_messages(self):
        for gateway in self._gateways:
            for logger in self._loggers:
                logger.receive(gateway.get_message())


if __name__ == '__main__':
    net_gateway = vendorapi.NetworkMessageGateway("pttp://perdu.com")
    windows_gateway = vendorapi.WindowsMessageGateway()

    terminal_logger = sdk.EventLogger()

    string_database = sdk.StringDatabase('log.db')
    database_logger = sdk.StringDatabaseLogger(string_database)

    app = MyApp([NetworkGateway(net_gateway), WindowsGateway(windows_gateway)], [terminal_logger, database_logger])
    app.connect_and_log_messages()
