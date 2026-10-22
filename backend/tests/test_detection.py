


from unittest.mock import Mock

from app.services.detection import detect_repeated_failed_logins


def test_detection_triggers_at_threshold():
    db = Mock()
    db.query.return_value.filter.return_value.count.return_value = 4

    result = detect_repeated_failed_logins(
        db=db,
        source_ip="192.0.2.88",
    )

    assert result is True


def test_detection_does_not_trigger_below_threshold():
    db = Mock()
    db.query.return_value.filter.return_value.count.return_value = 3

    result = detect_repeated_failed_logins(
        db=db,
        source_ip="192.0.2.88",
    )

    assert result is False
