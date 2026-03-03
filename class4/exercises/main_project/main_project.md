### Main Project

### Gaia API

Using the Gaia API and the Checkpoint SDK create an auditing script for your pod that checks the following.
    1. User checks (uses "show-users" endpont):
        * Only users configured are: admin and monitor
        * Should display "pass" in green for success and "fail" in red for failure.
    2. Password policy checks (uses "show-password-policy"):
        * Maximum failed login attempts is <= 10.
        * Minimum account lockout duration is >= 600s.
        * Maximum inactive days is <= 365.
        * Lock inactive accounts is set to True.
        * Minimum password character complexity is >= 3.
        * Minimum password length is >= 10.
        * Each check should display "pass" in green for success and "fail" in red for failure.

### Gaia SSH

Connect to your pod using Netmiko and SSH.

Using Netmiko configure the following three items:

```bash
set password-controls complexity 3
set password-controls deny-on-nonuse enable on
set password-controls min-password-length 10
```

Call the Netmiko .save_config() method to ensure that you properly save these changes.

Re-run your Gaia auditing script and see how the above changes modify the earlier failures in your auditing script.

