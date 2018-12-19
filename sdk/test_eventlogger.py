import pytest

from sdk.eventlogger import StringEvent, EventLogger


def test_receive_raise_when_timestamp_is_not_int():
    logger = EventLogger()
    event = StringEvent("", "str")

    with pytest.raises(ValueError):
        logger.receive(event)


def test_receive_raise_when_msg_is_not_str():
    logger = EventLogger()
    event = StringEvent(1, "")

    with pytest.raises(ValueError):
        logger.receive(event)
