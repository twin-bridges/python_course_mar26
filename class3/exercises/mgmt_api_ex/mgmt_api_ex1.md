### Mgmt API Exercise

Reusing the code you created for the Gaia API authentication exercise (with slight modifications of the base_url), connect and authentication to the Mgmt API of your pod.

After authenticating connect to the "show-gateway-capabilities" endpoint and retrieve the JSON payload from this reponse.

From the returned data structure extract and print out the Supported OS Versions and also extract and print out the LightSpeed supported hardware.

Your output should look similar to the following:

```bash
$ python mgmt_api_ex1.py 

R81 Supported OS Versions: 
--------------------
['R81', 'R81.10', 'R81.20']


LightSpeed Supported Hardware: 
--------------------
[
    'QLS250 Quantum LightSpeed',
    'QLS450 Quantum LightSpeed',
    'QLS650 Quantum LightSpeed',
    'QLS800 Quantum LightSpeed',
    'MLS200 Maestro LightSpeed',
    'MLS400 Maestro LightSpeed'
]

```
