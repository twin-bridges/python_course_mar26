### Main Project

1. Using the Gaia API and the Checkpoint SDK, create an auditing script for your pod that checks the following.
    1. User checks (uses "show-users" endpont):
        * Only users configured are: admin and monitor
        * Should display "pass" in green for success and "fail" in red for failure.
    2. Password policy checks (uses "show-password-policy"):
        * Maximum failed login attemps is <= 10.
        * Minimum account lockout duration is >= 600s.
        * Maximum inactive days is <= 365.
        * Lock inactive accounts is set to True.
        * Minimum password character complexity is >= 3.
        * Minimum password length is >= 10.
        * Each check should display "pass" in green for success and "fail" in red for failure.

