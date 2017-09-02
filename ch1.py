"""
https://bartoszmilewski.com/2014/11/04/category-the-essence-of-composition/
"""

"""
Notes:
1. Category is simply collection of objects and arrows that go between them
2. Arrows could be understood as functions or morphisms.
3. Composition: g(f(A)) or g.f if f: A->B and g: B->C
4. Proerties of Composition:
    A. Associative: h.g.f == (h.g).f == h.(g.f)
    B. There exists identity function: f.id = id.f = f
5. TIP: Your composition should be such that its Surface Area increases slower than its volume.
(SA: the information we need in order to compose chunks, Vol: the information we need in order to implement them)
The Idea being that once implemented, we should not be looking inside the object, only think as to how to compose them.
"""

"""
Challenges

1. Implement, as best as you can, the identity function in your favorite language (or the second favorite, if your favorite language happens to be Haskell).
2. Implement the composition function in your favorite language. It takes two functions as arguments and returns a function that is their composition.
3. Write a program that tries to test that your composition function respects identity.
4. Is the world-wide web a category in any sense? Are links morphisms?
5. Is Facebook a category, with people as objects and friendships as morphisms?
6. When is a directed graph a category?
""" 


# Test functions. One defined by lambda and one simply
double = lambda x: x*2
def inc_1(x): 
    return x+1

# Compose: func2.func1
def composition(func1, func2):
    return lambda x: func2(func1(x))

# test
double_then_inc = composition(double, inc_1)
assert double_then_inc(4) == 9
assert composition(double_then_inc, lambda x: x*x)(2) == 25


# Identity
identity = lambda x: x

# Test
assert composition(double, identity)(6) == composition(identity, double)(6) == double(6)
