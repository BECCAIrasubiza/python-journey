
from log_parser import parse_line, mask_mrn


def test_good_line():
    result = parse_line("2026-10-19 08:15 | ADMIT | MRN10234 | triage 2\n")
    assert result == {
        "date": "2026-10-19",
        "time": "08:15",
        "event": "ADMIT",
        "mrn": "MRN10234",
        "triage": 2,
    }


def test_lowercase_event_is_accepted():
    result = parse_line("2026-10-19 10:30 | admit | MRN11236 | triage 3")
    assert result["event"] == "ADMIT"


def test_bad_lines():
    assert parse_line("system restarted by admin") == None
    assert parse_line("2026-10-19 10:10 | ADMIT | MRN1100 | triage 3") == None    # 4-digit MRN
    assert parse_line("2026-10-19 12:05 | ADMIT | MRN11302 | triage 7") == None   # triage 7
    assert parse_line("2026-10-19 12:05 | VISIT | MRN11302 | triage 2") == None   # unknown event
    assert parse_line("") == None


def test_mask_mrn():
    assert mask_mrn("MRN10234") == "MRN***34"
    assert mask_mrn("A MRN10234 then MRN11005") == "A MRN***34 then MRN***05"
    assert mask_mrn("no mrn here") == "no mrn here"
