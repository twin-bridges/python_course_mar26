### Main Project

# NEEDS more to be done
# mgmt_cli session mgmt?
# more configure work gaia DNS settings via API, DNS domain via SSH
# FW policy, add Blocked IPs, to policy via mgmt API. If I reset the    XXXX
# FW you would also need to add the host objects for mgmt itself.
# Use main Python script and subprocess to coordinate actions  XXXXX

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

### Mgmt API
TODO: add pathlib for blocked IPs file?
TODO: explain sets

Using Python connect to the management API of your pod. Create a function that uses the management API and the 'show-group' API endpoint to retrieve the current group membership of the "Blocked IPs" group.

If the "Blocked IPs" group does not exist, then your function should return an empty list or an empty set.

Create a function that reads in the "blocked_ips.txt" file.

Compare the current blocked IPs (in other words the current members of "Blocked IPs" group) to the new blocked IPs (the blocked IPs read in from the file). Note, you probably will want to use sets for this comparison.

If the sets are different, determine the blocked IPs that need to be added (blocked IPs that are in the file, but not currently specified as group members) and the blocked IPs that need to be removed (current members of the Blocked IPs group that do not exist in the "blocked_ips.txt" file).

Create a function that configures host objects for each of the new blocked IPs (blocked IPs to be added).

Create a function that configures the group object and updates the membership to match the "blocked_ips.txt" file.

Create a function that removes all of the host objects that used to be members, but are no longer in the Blocked IPs group and are no longer in the blocked_ips.txt file.

Publish your changes via the mgmt API.

