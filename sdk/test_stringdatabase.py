from sdk.stringdatabase import StringDatabaseLogger, StringDatabase


def test_logger_receive_call_open(mocker):
    database = mocker.Mock(spec=StringDatabase)
    logger = StringDatabaseLogger(database)

    logger.receive(mocker.Mock())

    database.open.assert_called_once()
