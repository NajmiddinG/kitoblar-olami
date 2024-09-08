import os
import sys
from glob import glob

ui_files = glob("ui/designer/*.ui")

os.makedirs("ui/ui_generated", exist_ok=True)

size = len(ui_files)
for index, ui_file in enumerate(ui_files):
    i = index + 1
    percent = int((i / size) * 100)
    percent_str = "["
    percent_str += "=" * percent
    percent_str += " " * (100 - percent)
    percent_str += "]"

    file_name = os.path.splitext(os.path.basename(ui_file))[0]

    output_file = f"ui/ui_generated/{file_name}_ui.py"

    os.system(f"pyside6-uic {ui_file} -o {output_file}")

    sys.stdout.write(
        "\r\033[92m" + f" {i}/{size} " + percent_str + f" {percent} % " + "\033[0m"
    )
    sys.stdout.flush()

resource_file = "resource.qrc"
if os.path.exists(resource_file):
    os.system("pyside6-rcc -o resource_rc.py resource.qrc ")
    print("\n\033[92m" + "Resource done!!!" + "\033[0m")
else:
    print("\n\033[91m" + "Resource file not found." + "\033[0m")
