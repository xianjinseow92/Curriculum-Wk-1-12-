# Code Style Exercise

The pair problem today asked us to find the prime factors for a number.

I've taken the prime decomposition function from [Rosetta Code](https://www.rosettacode.org/wiki/Prime_decomposition#Python) and saved it here as `ugly.py`. We have two problems: The code doesn't run and the code is _ugly_.

The exercise is to:
1. Alter `ugly.py` so that it uses good style (pylint rates it 10/10 **and** the code speaks for itself). The code should still implement the same approach and algorithm in `ugly.py`.
2. Answer this morning's pair problem by importing the function into a Jupyter notebook and using the function to answer the question.


## More info

Specifically, when we run pylint we see the following:

```bash
pylint ugly.py
************* Module ugly
ugly.py:1:0: C0111: Missing module docstring (missing-docstring)
ugly.py:1:0: C0103: Argument name "n" doesn't conform to snake_case naming style (invalid-name)
ugly.py:1:0: C0111: Missing function docstring (missing-docstring)
ugly.py:3:11: E0602: Undefined variable 'long' (undefined-variable)
ugly.py:3:16: E0602: Undefined variable 'floor' (undefined-variable)
ugly.py:3:22: E0602: Undefined variable 'sqrt' (undefined-variable)
ugly.py:4:4: C0103: Variable name "d" doesn't conform to snake_case naming style (invalid-name)
ugly.py:5:4: R1706: Consider using ternary (2 if n % 2 == 0 else 3) (consider-using-ternary)
ugly.py:5:4: C0103: Variable name "q" doesn't conform to snake_case naming style (invalid-name)
ugly.py:7:8: C0103: Variable name "q" doesn't conform to snake_case naming style (invalid-name)
ugly.py:8:8: C0103: Variable name "d" doesn't conform to snake_case naming style (invalid-name)
ugly.py:9:4: R1706: Consider using ternary ([q] + fac(n // q) if q <= maxq else [n]) (consider-using-ternary)

----------------------------------------------------------------------
Your code has been rated at -16.67/10 (previous run: -16.67/10, +0.00)
```

This is what you'll want to get to 10/10.
