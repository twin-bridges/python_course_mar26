### Function Exercise3

Construct a function named 'fw_func' that has three parameters: name, ip_addr, and os_version. The os_version parameter should have a default value of "R82".

The function body should use f-strings to print out the parameter name and corresponding value (for example, 'print(f"{name=}")' ).

The function body should also return the following string: f"{name}-{ipaddr}-{os_version}"

1. Call 'fw_func' using three positional arguments. Print out the function return value.
2. Call 'fw_func' using three named arguments. Print out the function return value.
3. Call 'fw_func' using two named arguments and the default os_version. Print out the function return value.
4. Call 'fw_func' using one positional argument and two named arguments. Print out the function return value.
on

Your program output should look similar to the following:

```bash
$ python func_ex3.py 

Function call with positional arguments
------------------------------
name='chkpnt-pod99'
ipaddr='3.77.44.109'
os_version='R81.20'

ret_val='chkpnt-pod99-3.77.44.109-R81.20'


Function call with named arguments
------------------------------
name='chkpnt-pod1'
ipaddr='3.77.44.100'
os_version='R82'

ret_val='chkpnt-pod1-3.77.44.100-R82'


Function call with named arguments and a default value
------------------------------
name='chkpnt-pod1'
ipaddr='3.77.44.100'
os_version='R82'

ret_val='chkpnt-pod1-3.77.44.100-R82'


Function call with both positional and named arguments
------------------------------
name='chkpnt-pod2'
ipaddr='3.77.44.9'
os_version='R82.10'

ret_val='chkpnt-pod2-3.77.44.9-R82.10'

```
