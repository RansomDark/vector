# vector
Simple python library for working with vectors

# Usage 
```python
>>> from vector import *
>>> v1 = Vector(1, 2, 3, 4)
>>> v2 = Vector(0, -5, 2, -5)
>>> u = v1 + v2
>>> print(u.pr())
(1, -3, 5, -1)
```

### Magnitude
```python
>>> v1 = Vector(1, 2, 3, 4, 5)
>>> print(v1.magnitude())
7.416198487095663
```

### Normalize
```python
>>> v1 = Vector(1, 2, 3, 4, 5)
>>> print(v1.normalize().pr())
(0.13483997249264842, 0.26967994498529685, 0.40451991747794525, 0.5393598899705937, 0.674199862463242)
```

### Angle between vectors
```python
>>> v1 = Vector(1, 2, 3)
>>> v2 = Vector(0, -5, 2)
>>> print(get_angle(v1, v2, degrees=True))
1.7706405602431485
```

### Cross product
```python
>>> v1 = Vector(1, 2, 3)
>>> v2 = Vector(-5, 20, 100)
>>> print(cross(v1, v2).pr())
(140, -115, 30)
```

### Get orthogonal basis
```python
>>> v1 = Vector(10, 20)
>>> v2 = Vector(30, 40)
>>> u1, u2 = get_orthogonal_basis([v1, v2])
>>> print(u1.pr(), u2.pr())
(10, 20) (8.0, -4.0)
```
