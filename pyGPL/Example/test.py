import pyGPL

def f(x):
    # Convert integers to complex numbers
    G1 = pyGPL.GPL([complex(-4, 0), complex(4, 0), complex(0, 0)], x)
    G2 = pyGPL.GPL([complex(1, 0), complex(-1, 0), complex(-1, 0)], x)
    
    return G1 + G2

# Test at a few points
test_values = [0.5, 2.0, 10]
for x in test_values:
    result = f(x)
    print(f"f({x}) = {result}")

