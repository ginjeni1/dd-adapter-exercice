import pytest

from sdk.stringdatabase import StringDatabaseLogger, StringDatabase


def test_logger_receive_call_open(mocker):
    database = mocker.Mock(spec=StringDatabase)
    logger = StringDatabaseLogger(database)

    logger.receive(mocker.Mock(msg="fubar", timestamp=42))

    database.open.assert_called_once()


def test_logger_receive_call_close(mocker):
    database = mocker.Mock(spec=StringDatabase)
    logger = StringDatabaseLogger(database)

    logger.receive(mocker.Mock(msg="fubar", timestamp=42))

    database.close.assert_called_once()


def test_logger_receive_call_insert(mocker):
    database = mocker.Mock(spec=StringDatabase)
    logger = StringDatabaseLogger(database)

    logger.receive(mocker.Mock(msg="fubar", timestamp=42))

    database.insert.assert_called_with("fubar")


def test_logger_receive_raise_when_time_is_not_int(mocker):
    database = mocker.Mock(spec=StringDatabase)
    logger = StringDatabaseLogger(database)

    with pytest.raises(ValueError):
        logger.receive(mocker.Mock(msg="fubar", timestamp="42"))


def test_logger_receive_raise_when_msg_is_not_str(mocker):
    database = mocker.Mock(spec=StringDatabase)
    logger = StringDatabaseLogger(database)

    with pytest.raises(ValueError):
        logger.receive(mocker.Mock(msg=42, timestamp=42))


def test_logger_with_different_format_call_insert(mocker):
    database = mocker.Mock(spec=StringDatabase)
    logger = StringDatabaseLogger(database)

    logger.receive(mocker.Mock(msg="fubar", timestamp=42), lambda event: "{}-{}".format(event.timestamp, event.msg))

    database.insert.assert_called_with("42-fubar")
