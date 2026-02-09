"""
Character 	Unicode (Hex)	Description
ä	00E4	a-umlaut (small)
ö	00F6	o-umlaut (small)
ü	00FC	u-umlaut (small)
Ä	00C4	A-umlaut (capital)
Ö	00D6	O-umlaut (capital)
Ü	00DC	U-umlaut (capital)
ß	00DF	Eszett / Sharp s
ẞ	1E9E	Capital Sharp S
"""

print("\u00e4")
print("\u00c4")

print("\u00f6")
print("\u00d6")

print("\u00fc")
print("\u00dc")

print("\u00df")
print("\u1e9e")

some_str = """
ä
Ä
ö
Ö
ü
Ü
ß
ẞ
"""
print(some_str)
