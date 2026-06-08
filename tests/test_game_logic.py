import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the swapped lower/higher hint bug ---
# The original bug returned the WRONG direction in the message:
# a too-high guess told the player to "Go HIGHER", and vice versa.

def test_too_high_guess_says_go_lower():
    # Guess (60) is above the secret (50), so the hint must tell
    # the player to go LOWER, not higher.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_guess_says_go_higher():
    # Guess (40) is below the secret (50), so the hint must tell
    # the player to go HIGHER, not lower.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


# --- Regression test for the swapped difficulty-range bug ---
# The original bug returned Normal -> (1, 100) and Hard -> (1, 50),
# so Hard was actually EASIER than Normal. The range must grow as
# difficulty increases.

def test_difficulty_range_grows_with_difficulty():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")

    # Each harder level must span a wider range than the easier one.
    assert easy_high < normal_high < hard_high
    # Hard specifically must not be easier than Normal (the original bug).
    assert hard_high > normal_high


# --- Regression test for the parse_guess decimal-truncation bug ---
# The original bug parsed decimals with int(float(raw)), so a guess
# like "3.9" was silently TRUNCATED to 3 and accepted as valid. A
# non-integer guess must instead be rejected as invalid input.

def test_decimal_guess_is_rejected():
    ok, value, error = parse_guess("3.9")
    assert ok is False
    assert value is None
    assert error is not None

def test_valid_integer_guess_is_parsed():
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None


# --- Regression tests for the update_score bugs ---

# Bug 1: the win formula was 100 - 10 * (attempt_number + 1), so a
# first-try win scored only 80 instead of the full 100.

def test_first_try_win_scores_full_100():
    # Winning on attempt 1 should award the maximum 100 points.
    assert update_score(0, "Win", 1) == 100

def test_win_loses_ten_points_per_extra_attempt():
    # Each attempt beyond the first costs 10 points.
    assert update_score(0, "Win", 2) == 90
    assert update_score(0, "Win", 3) == 80

# Bug 2: a "Too High" wrong guess ADDED 5 points on even attempts,
# letting players farm score. Both wrong-guess outcomes must penalize
# the player equally regardless of attempt parity.

def test_too_high_always_penalizes_regardless_of_parity():
    # Even attempt number used to (incorrectly) grant +5.
    assert update_score(100, "Too High", 2) == 95
    # Odd attempt number.
    assert update_score(100, "Too High", 3) == 95

def test_too_high_and_too_low_penalize_equally():
    assert update_score(100, "Too High", 2) == update_score(100, "Too Low", 2)
