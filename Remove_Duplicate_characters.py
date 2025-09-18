s = "programming"

here = ''
for ch in s:
    if ch not in here:
        here += ch
print(here)
