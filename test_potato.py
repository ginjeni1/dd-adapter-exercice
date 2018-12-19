from potato import PotatoLogger, potato_formatter


def test_receive_without_potato_do_not_call_logger(mocker):
    event = mocker.Mock(msg="No forbidden vegetable", timestamp=42)
    logger = mocker.Mock()
    potato_logger = PotatoLogger(logger)

    potato_logger.receive(event)

    logger.receive.assert_not_called()


def test_receive_with_potato_call_logger(mocker):
    event = mocker.Mock(msg="Hooo, potato", timestamp=42)
    logger = mocker.Mock()
    potato_logger = PotatoLogger(logger)

    potato_logger.receive(event)

    logger.receive.assert_called_once()


def test_receive_with_potato_call_logger_with_formatter(mocker):
    event = mocker.Mock(msg="Hooo, potato", timestamp=42)
    logger = mocker.Mock()
    potato_logger = PotatoLogger(logger)

    potato_logger.receive(event)

    logger.receive.assert_called_with(event, potato_formatter)
