from sdk.stringdatabase import StringDatabaseLogger, StringDatabase


def test_logger_receive_call_open(mocker):
    database = mocker.Mock(spec=StringDatabase)
    logger = StringDatabaseLogger(database)

    logger.receive(mocker.Mock())

    database.open.assert_called_once()


def test_logger_receive_call_close(mocker):
    database = mocker.Mock(spec=StringDatabase)
    logger = StringDatabaseLogger(database)

    logger.receive(mocker.Mock())

    database.close.assert_called_once()


def test_logger_receive_call_insert(mocker):
    database = mocker.Mock(spec=StringDatabase)
    logger = StringDatabaseLogger(database)

    logger.receive(mocker.Mock(msg="fubar", timestamp=42))

    database.insert.assert_called_with("42-fubar")
