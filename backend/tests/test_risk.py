


from app.services.risk import calculate_risk_score


def test_failed_login_risk_score():
    assert calculate_risk_score("login", "failure", False) == 30


def test_successful_login_risk_score():
    assert calculate_risk_score("login", "success", False) == 5


def test_suspicious_event_risk_score():
    assert calculate_risk_score("login", "failure", True) == 90


def test_risk_score_is_case_insensitive():
    assert calculate_risk_score("LOGIN", "FAILURE", False) == 30
