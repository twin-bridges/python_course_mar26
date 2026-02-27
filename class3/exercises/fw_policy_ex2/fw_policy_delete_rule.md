### Delete firewall rule exercise

Add an additional parameter to your 'cfg_fw_rule' function. This parameter should be named 'delete_rule' and should default to False.

If you call your cfg_fw_rule function and specify 'delete_rule=True', then function will delete the specified firewall rule.

Essentially re-create the code you created in the 'edit firewall rule' exercise except in this case, use your function to delete the specified firewall rule.

After the firewall rule has been deleted, publish your changes, and install your new firewall policy.

You should regression test your code from 'fw_policy_ex1' and from 'fw_policy_edit_rule' and ensure that your modifications to the 'cfg_fw_rule' function did not break the already existing code.
