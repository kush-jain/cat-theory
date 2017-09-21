"""
https://bartoszmilewski.com/2014/11/24/types-and-functions/

Notes:
    1. Author seemed to be in favor of strongly typed language
    2. Functions
        Pure functions are those which has no side effect and always give same output for same input,
        We will be focusing exclusively on those
        Pure functions are easier to represent mathematically and model them using categorical theory
        [ Author asserts that impure functions can be converted to pure functions using monads, which will be seen later]
    3. Types
        Types are simply set of values. (For example Boolean type consists of True and False).
        Integer type is simply set of all integer value, and here set consists of infinite values
        Thus, sets can be finite or infinite.
        So, we can simply treat types as Sets, and functions as morphisms between these sets.
        (This has few caveats, which I am ignoring for now)
    4. Example of Types
        A. Type representing empty set?
            C++ does not have any type for this. Haskell as Void.
            While you can define a function with empty set, you cannot ever call it.
            (Since you cannot pass correct argument to it)
        B. Types representing singleton?
            C++ has void, Haskell as () to represent it.

            Function which take such inputs are:
            For example:
                Python:
                    def a44():
                        return 44
                C++:
                    int a44() {
                        return 44;
                    }
                Haskell:
                    a44 :: () -> Integer
                    a44 () = 44

            What about functions which returns singleton?
            Usually such functions are not pure, and  have side effect since they are discarding their inputs
            They are parametrically polymorphic, that is not dependent on input type
            But some examples are (for functions with single input):
                Python:
                    def unit(arg):
                        pass
                C++:
                    template <class T>
                    void unit(T) {}
                Haskell:
                    unit :: a -> ()
                    unit _ = ()
        C. Types representing two element set
            Simplest example is Boolean, which is 2-element set of True and False
            Functions returning Boolean are called predicates.
            Some predicate examples might be isAlpha (in Haskell), isinstance (in Python) etc.
"""

import time
import random

"""
Challenges

1.
Define a higher-order function (or a function object) memoize in your favorite language.
This function takes a pure function f as an argument and returns a function that behaves almost exactly like f, 
    except that it only calls the original function once for every argument, stores the result internally, 
    and subsequently returns this stored result every time it's called with the same argument.
You can tell the memoized function from the original by watching its performance.
For instance, try to memoize a function that takes a long time to evaluate.
You'll have to wait for the result the first time you call it, 
    but on subsequent calls, with the same argument, you should get the result immediately.

2.
Try to memoize a function from your standard library that you normally use to produce random numbers. Does it work?

3.
Most random number generators can be initialized with a seed.
Implement a function that takes a seed, calls the random number generator with that seed, and returns the result.
Memoize that function. Does it work?

4.
Which of these C++ functions are pure?
Try to memoize them and observe what happens when you call them multiple times: memoized and not.

    A.
    int fact(int n) {
        int i;
        int result = 1;
        for (i = 2; i <= n; ++i)
            result *= i;
        return result;
    }

    B.
    std::getchar()

    C.
    bool f() {
        std::cout << "Hello!" << std::endl;
        return true;
    }

    D.
    int f(int x)
    {
        static int y = 0;
        y += x;
        return y;
    }

5.
How many different functions are there from Bool to Bool? Can you implement them all?

6.
Draw a picture of a category whose only objects are the types Void, () (unit), and Bool; 
    with arrows corresponding to all possible functions between these types.
Label the arrows with the names of the functions.
"""


def memoize(func):

    prev_args = dict()

    def inner(*args):

        memoize_value = prev_args.get(args)
        if memoize_value:
            return memoize_value
        else:
            val = func(*args)
            prev_args[args] = val
            return val

    return inner


# Test function
@memoize
def large_sum(limit):
    return sum(range(limit))

# Checking that memoize works as expected
assert large_sum(3) == 3

t00 = time.time()
large_sum(10 ** 6)
t01 = time.time()

t10 = time.time()
large_sum(10 ** 6)
t11 = time.time()

t20 = time.time()
large_sum(10 ** 6 + 1)
t21 = time.time()

print "First Iteration {:.2E}, Memoized {:.2E}, Not Memoized {:.2E} ".format(t01-t00, t11-t10, t21-t20)


def large_sum_2(limit):
    return sum(range(limit))

# Checking that memoize works as expected
assert memoize(large_sum)(3) == 3

t00 = time.time()
memoize(large_sum)(10 ** 6 + 3)
t01 = time.time()

t10 = time.time()
memoize(large_sum)(10 ** 6 + 3)
t11 = time.time()

t20 = time.time()
memoize(large_sum)(10 ** 6 + 4)
t21 = time.time()

print "Second Iteration {:.2E}, Memoized {:.2E}, Not Memoized {:.2E} ".format(t01-t00, t11-t10, t21-t20)


# Random numbers With Memoization
rand1 = memoize(random.random)()
rand2 = memoize(random.random)()
print rand1 == rand2, "Random Memoization Attempt #1"


rand1 = memoize(random.randint)(1, 1000)
rand2 = memoize(random.randint)(1, 1000)
print rand1 == rand2, "Random Memoization Attempt #2"


random.seed(5)
t00 = time.time()
rand1 = memoize(random.random)()
t01 = time.time()

random.seed(5)
t10 = time.time()
rand2 = memoize(random.random)()
t11 = time.time()

print rand1 == rand2, "Seeded Random Memoization Attempt"
print "Random Memoization results {:.2E}, Memoized {:.2E}".format(t01-t00, t11-t10)


# Bool-Bool functions
# 1. Identity, 2. Reverse 3. Always True 4. Always False


# Function mappings (Using Haskell notation of Void, () and Bool)
# Absurd Types 1. Void -> Void, 2. Void -> Bool (T) 3. Void -> Bool (F) 4. Void -> ()
# Discard Types 5. () -> Void 6. Bool -> Void
# 7. () -> Bool (True) 8. () -> Bool (False)
# 9. Bool -> () 10. () -> () (Identity)
# 11-14: 4 Types of Bool-Bool defined above


"""
Observations

1. Memoization only works with positional arguments since dict requires Hashable types. Any idea on extending it to keyword args?
2. Memoization and Problem #4 is really helpful in arguing about whether function has side effect or not.
"""
