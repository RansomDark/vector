import math

class Vector:
    def __init__(self, *components):
        self.components = components
        self.dim = len(components)
    def __add__(self, other):
        if self.dim != other.dim:
            raise ValueError("Vectors must have same dimension")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    def __sub__(self, other):
        if self.dim != other.dim:
            raise ValueError("Vectors must have same dimension")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[other * x for x in self.components])
        if isinstance(other, Vector):
            if self.dim != other.dim:
                raise ValueError("Vectors must have same dimension")
            return sum([a * b for a, b in zip(self.components, other.components)])

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return sum([x * x for x in self.components]) ** 0.5

    def normalize(self):
        n = self.magnitude()
        if n == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(*[x / n for x in self.components])
    
    def __len__(self):
        return self.dim

    def pr(self):
        return f"({', '.join(map(str, self.components))})"
    def __len__(self):
        return self.dim

def get_angle(v, w, degrees=False):
    if v.dim != w.dim:
        raise ValueError("Vectors must have same dimension")

    dot_product = v * w
    magnitude_product = v.magnitude() * w.magnitude()

    if magnitude_product == 0:
        raise ValueError("Angle not defined")

    cos_theta = max(-1.0, min(1.0, dot_product / magnitude_product))
    angle_rad = math.acos(cos_theta)

    return math.degrees(angle_rad) if degrees else angle_rad

def cross(v, w):
    if v.dim != 3 or w.dim != 3:
        raise ValueError("vectors must have a third dimension")

    v1, v2, v3 = v.components
    w1, w2, w3 = w.components

    u1 = v2 * w3 - v3 * w2
    u2 = v3 * w1 - v1 * w3
    u3 = v1 * w2 - v2 * w1

    return Vector(*[u1, u2, u3])

def is_orthogonal(v, w):
    return w * v == 0

def is_collinear(v, w):
    theta = get_angle(v, w)
    return theta == 0

def get_orthogonal_basis(vec):
    basis = []
    for v in vec:
        w = v
        for b in basis:
            ui = (w * b) / (b * b)
            w = w - ui * b

        if w.magnitude() > 1e-10:
            basis.append(w)
        else:
            raise ValueError(f'Vector {v} depends linearly on the previous ones')
    return basis
  
