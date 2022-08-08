from math import sin, cos, radians, pi


def read_model(path):
    try:
        file = open(path, "r")
    except FileNotFoundError:
        print("Couldn't open model file: " + path + ".")
        return None
    except Exception as e:
        print("An exception has occurred when opening model file.")
        return None
    m = []
    for line in file.readlines():
        if not line.startswith("("):
            continue
        p1, p2 = line.replace("(", "").replace(")", "").replace(" ", "").split(":")
        p1 = p1.split(",")
        p2 = p2.split(",")
        start, end = [], []
        for s in p1:
            start.append(int(s))
        for s in p2:
            end.append(int(s))
        m.append((start, end))

    return m

def rotate_x(m, a):
    m2 = []
    sin_a = sin(radians(a))
    cos_a = cos(radians(a))
    for p in m:
        y = p[1] * cos_a - p[2] * sin_a
        z = p[2] * cos_a + p[1] * sin_a
        m2.append((p[0], y, z))
    return m2

def rotate_y(m, a):
    m2 = []
    sin_a = sin(radians(a))
    cos_a = cos(radians(a))
    for p in m:
        x = p[0] * cos_a + p[2] * sin_a
        z = p[2] * cos_a - p[0] * sin_a
        m2.append((x, p[1], z))
    return m2

def rotate_z(m, a):
    m2 = []
    sin_a = sin(radians(a))
    cos_a = cos(radians(a))
    for p in m:
        x = p[0] * cos_a - p[1] * sin_a
        y = p[1] * cos_a + p[0] * sin_a
        m2.append((x, y, p[2]))
    return m2
