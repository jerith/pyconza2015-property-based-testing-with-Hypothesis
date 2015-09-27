import sys

in_header = False
in_traceback = False


def narrow(line):
    for thing in ["====", "----", "____"]:
        if line.startswith(thing) and line.endswith(thing):
            line = line[4:-4]
    return line


def emit(line):
    line = line.rstrip("\n")
    if line.strip() == "" or in_header or in_traceback:
        return
    line = narrow(line)
    sys.stdout.write(line + "\n")


for line in sys.stdin.readlines():
    if line.startswith("Traceback (most recent call last):"):
        emit("[Traceback elided]")
        in_traceback = True
    elif in_traceback and not line.startswith("  "):
        in_traceback = False

    emit(line)

    if "== test session starts ==" in line:
        in_header = True
    elif line.startswith("collected "):
        in_header = False
