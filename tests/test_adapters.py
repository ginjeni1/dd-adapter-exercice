
from adapters import WindowsGateway
from sdk.eventlogger import StringEvent


def test_windows_gateway_call_get_last_os_message(mocker):
    mocker.patch('adapters.time', mocker.Mock(return_value=10))
    windows_gateway = mocker.Mock()
    windows_gateway.last_os_message.return_value = "fubar"
    adapter = WindowsGateway(windows_gateway)

    message = adapter.get_message()

    expected_event = StringEvent("fubar", 10)
    assert expected_event.msg == message.msg
