## Three Levels of Software Testing

There are a myriad of paradigms of code testing, some of which are more or less relevant to data science. But in most paradigms, tests come in three levels. Quick overview, in decreasing order of specificity:

- **Unit testing**: This is the most specific type of testing and focuses on particular lines of code. In the OOP paradigm, we often test code at the function level.
- **Integration testing**: This type of testing looks at how modules work together and ensures that there are no issues when modules are connected.
- **Systems testing:** This type of testing looks at the whole process and often requires running data through all the pipes.

Today we'll be focusing on **unit testing**, and testing functions.

Say I have this Python function:

```python
def power(x,y):
return x**y
```

But now a user tries to do this:

```python
print(power('Andy','Blake'))
```

What should happen in this case?

Unit testing is about finding and pushing **edge cases**. Never assume anything about how your user is going to interact with your code. Asked for some numbers? Assume a user will try to pass in strings!

### Unit testing paradigm

In unit tests, we start by writing tests that we know will fail, then we write functions to pass those tests. Seems counterintuitive, but this is a helpful paradigm for making sure we know our edge cases beforehand.

Again, you first write a simple test. Then you add to the function until it passes that test. Then you write more tests for more functionality, then add more code to the function until it passes the tests.

## Python's 'unittest' library

Python has a library specifically for unit testing. It allows us to create a class for testing a module. An example of this is given to you in `pair_unit_testing.py`. This module is designed to unit test a function called `j()` and you can see that it's called in every testing scenario.

The `unittest` module allows you to check for errors, check for equality, check types, and check for variable existence.

## Today's pair: unit testing Jaccard distance

Your job today is to write a function that passes all of these tests. I'm telling that there exists a function that will pass all these tests, and your job is to reverse engineer that function.

I'll give you a big hint: `j()` is a function specifically designed to compute the Jaccard distance between two groups. The Jaccard distance is a measure of similarity of sets of objects (see: Wikipedia). It's not a particularly challenging function to write, but I want you to get practice writing unit tests: so, add a little functionality at a time, and try to get it to pass one or two unit tests at a time.

To see if your function passes, write a correct `j()` function in an appropriately named module (in a file called `jaccard.py` in the same directory). Then from the terminal use:

```bash
python pair_unit_testing.py
```

to see the report on your module's behavior.