# ================================================
# pip install rich

import os
import subprocess

# ================================================
if os.name == 'nt':
    subprocess.run(args="cls", shell = True, check = False)
else:
    subprocess.run(args="clear", shell = True, check = False)


# ================================================
index = 1

while index <= 10:
    if index == 3:
        index = 6
        continue

    if index == 8:
        break

    print(index)
    index += 1
