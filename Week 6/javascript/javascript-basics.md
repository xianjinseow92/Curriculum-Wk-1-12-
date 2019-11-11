# Javascript (JS) Basics

### Setup
We are going to start by looking at two files in `exercise_set_01`: `index.html` and `functions.js`. Load both these files in your text editor, and open `index.html` in Google Chrome.

 * Using the JavaScript developer console in Google Chrome (option+command+j on Macs)
     * Clearing the javascript console is control+l
     * You can also pull up what you last entered, using the UP button
 * You can use the JavaScript console like a calculator!

---

## Functions

Everything Javascript needs to live in the `<script>` tag. It can be placed in any section, but the bottom of `<body>` is usually best because HTML runs code top to bottom, and loading scripts should wait till the basic site is created for optimized user experience.

Scripts can and should be placed in external `.js` files, especially when multiple sites or pages want to use the script. To load the script file, use `src="path/to/file.js"` inside the script tag.

When loaded, the code will behave exactly as if it were written inside the HTML file. The separation allows easier read and maintenance, along with faster page loading using cached JS files.


## Variables

Like Python, we can declare and reuse variables. However, JS must explicitly state variables using "let" or "const". Arrays and other data types can be variables, like `let Data = [1,2,3,4,5];`.

---

## Translating from Python to Javascript

Here are a collection of functions that are useful javascript (where you will mostly be converting strings), and their Python equivalents.

### printing
```python
# Python, raw string
print("Hello world")

# Python, using variables
answer = 42
print(f"The value of answer is {answer}")
```
This prints to the terminal.

```javascript
// Javascript, raw string
console.log("Hello world")

// Javascript, using variables. Note quotes are backticks!
const answer = 42;
console.log(`The value of answer is ${answer}`);
```
This prints to the console. Try typing these commands into the console.

### functions
```python
# Python
def add_two(n):
  return n + 2
```

```javascript
// Javascript
function addTwo(n){
  return n + 2;
}
```

### lambda functions
```python
# Python, usually you use this within an
# apply.
lambda num, to_add: num + to_add
```

```javascript
// javascript. Short function. Used within a lot of functions!
(num, toAdd) => num + to_add;

// javascript, longer function
(num, toAdd) => {
  //maybe do some stuff
  console.log('calling the lambda function');
  return num + toAdd;
}
```
### list comprehensions
```python
# Python, first_letters is ['a', 'b', 'c']
words = ['alpha', 'beta', 'gamma']
first_letters = [word[0] for word in words]
```

```javascript
// Javascript, firstLetters is ['a', 'b', 'c']. Note use of lambda function!
let words = ['alpha', 'beta', 'gamma'];
let firstLetters = words.map( (word) => word[0] );
```

### list comprehensions with index
```python
# Python: Get (letter, index) pair, so pairs = [('c', 0), ('a', 1), ('t', 2)]
pairs = [(letter, index) for index, letter in enumerate('cat')]
```

```javascript
// Javascript: Get (letter, index) pair, so pairs = [['c', 0], ['a', 1], ['t', 2]]
let pairs = 'cat'.split('').map( (letter, index) => [letter, index]);
```

### add to lists/arrays
```python
# Python: add to end of a list
L = [1, 2, 3]
L.append(4)  # L is now [1, 2, 3, 4]
```

```javascript
// Javascript: add to end of a list
let L = [1, 2, 3];
L.push(4)  // L is now [1, 2, 3, 4]
```

### range(n)
```python
# Python
some_numbers = range(n)
```

```javascript
// Javascript. This isn't built in!
let someNumbers = Array(n).fill(0).map( (value, index) => index);
```
Notice how `range` in javascript uses the `index` of map.

### Ternaries

This might seem oddly specific in an overview of a language, but for manipulating webpages it comes up a lot. Consider the following code (Python) for determining a message:
```python
# What should the message be?
if (probability > 0.5):
  message = "You will survive"
else:
  message = "You sink on the titanic"
```

In Python, we can rewrite this as
```python
# Python, "ternary" (i.e. if /else) style
message = "You will survive" if (probability > 0.5) else "You sink on the titanic"
```

In Javascript, we can write ternary style with `(condition) ? (do if true) : (do if false)`:
```javascript
// Same thing in javascript
const message = (probability > 0.5) ? "You will survive" : "You will sink on the titanic";
// print that message onto the page
$('#result').html(message);
```

### Convert string to float
```python
# Python
float('3.14')
```

```javascript
// Javascript, method 1 (explicit)
parseFloat('3.14');

// Javascript, method 2 (quick, but difficult to understand)
+'3.14';
```

### Joining lists of words
```python
# Python, prints "not in Kansas anymore"
message = ' '.join(['not', 'in', 'Kansas', 'anymore'])
print(message)
```

```javascript
// Javascript, prints "not in Kansas anymore"
let message = ['not', 'in', 'Kansas', 'anymore'].join(' ')
console.log(message)
```

### Math Functions: power
```python
# Python, returns 16
2 ** 4
```

```javascript
// Javascript, return 16
Math.pow(2, 4)
```

### Math Functions: random number from 0 to 1
```python
# Python, random number from 0 to 1
import random
random.random()
```

```javascript
// Javascript, random number from 0 to 1
Math.random()
```
