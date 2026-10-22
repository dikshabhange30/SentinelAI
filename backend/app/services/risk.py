


def calculate_risk_score(
    event_type: str,
    event_status: str,
    is_suspicious: bool,
) -> int:
    """Calculate a basic rule-based risk score from 0 to 100."""

    score = 10

    if event_type.lower() == "login" and event_status.lower() == "failure":
        score = 30

    if event_type.lower() == "login" and event_status.lower() == "success":
        score = 5

    if is_suspicious:
        score = 90

    return min(max(score, 0), 100)
