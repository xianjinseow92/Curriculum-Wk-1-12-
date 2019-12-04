# Pair Problem

**Generate the numbers 1 to 100**.

1. Do the above via list comprehension; then do it by using [`map`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.map.html) and `filter` (hint: use lambda functions):

   - Square the numbers.
   - Select just the squares that are odd.

2. (This part is outside the common use of the MapReduce paradigm). We’ve mostly used `reduce` to add values. But it can do a lot more! We might implement `reduce` like this:

```python
def reduce(combine, collection, start):
    # acc for "accumulator"
    acc = start
    for x in collection:
        acc = combine(acc, x)
    return acc
```

If `collection` is a list of `Int`s, maybe `start` is also an `Int`. But it could be a list, or a data frame, or even another function! This kind of thing is common in functional programming, where a `reduce` is usually called a “fold”.
`reduce` is more powerful than you may at first realize, and can even be used in place of `map` and `filter`. See if you can use Python’s built-in `reduce` in three very different ways:

- Add up the numbers 1 to 100
- Square the numbers 1 to 100 (returning a list of length 100, like `map`)
- Process the list of numbers 1 to 100, returning the list of only the odd ones (like `filter`)