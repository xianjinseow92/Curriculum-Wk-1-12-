# Example Flask app

There is a _very_ simple Flask app. It provides one route:
* `/convert_temperature`: This is a POST route. When you send the object `{'temperature': XX, 'unit': Y}` it will send back a dictionary with that temperature converted into Kelvin (K), Fahrenheit (F), and Centigrade (C). It is up to the receiver to process the returned object.

To run the app:
```bash
cd post_only_flask
python temp_app.py
```
We will assume this opens on port 5000 on your local machine (the default port).


## Testing the post route

To test the post route, start up python somewhere else on your machine. Then run the following:
```python
import requests

r = requests.post('http://127.0.0.1:5000/convert_temperature', json={'temperature': 54, 'unit': 'F'})
print(r.json())
```
If successful, you should get
```python
{'C': 12.222222222222223, 'F': 54, 'K': 285.3722222222222}
```
returned.

This is an example of a _post_ request. In python, we asked the flask server to look up the route `/convert_temperature`. The `json` dictionary we passed in the request is accessible via `request.json`.

## The AJAX command

Now let's use a website that has nothing to do with our Flask app, and show that we can communicate with it.

1. Open the page `index.html` in Chrome
2. Open the javascript console (command + option + J)
3. Type "54"" into the text box
4. Note the console shows `{'C': 12.2222, 'F': 54, 'K': 285.3722}` is returned!

The "glue" that allows this to work is the `$.post` command included in jQuery. The format in this case is:
```js
$.post({
  url: 'http://localhost:5000/convert_temperature',
  contentType: 'application/json',
  data: JSON.stringify(features),
  success: (result) => metis_success(result),
  error: (result) => metis_error(result)
});
```
where `features` takes the form, for example, of `{'temperature': 54, 'unit': 'F'}`.

The basic idea is:
1. We convert `features` to a string, to allow passing.
2. We pass the string to the url `http://localhost:5000/convert_temperature`. Flask directs this route to `convert_temps()`
3. If the communication with Flask is successful, the returned value from `convert_temps()` is passed to `metis_success`
4. If the communication with Flask has an error, the error message is passed to `metis_error`

If you look in `functions.js` you can find the definitions of `metis_success`, `metis_error` and how we use jQuery selectors to get the values off the page.

### Your exercise (short, approx 10 mins):

At the moment, `metis_success(result)` prints the object (aka Python dictionary) to the console. Instead, use jQuery to write the temperature conversions into the div with id "result".

You should only have to modify `functions.js`

## Separation of concerns

Note that the webpage `my_test_page.html` didn't know anything about Flask. This means that your web development team, who are experts at Javascript, can use React, Angular, or any other framework to build the app, provided they know how to query your app, and what sort of object it returns.

This is just as well, otherwise as a data scientist you would have to help change the template every time we wanted to redesign the website!

Note that your model is also usable by mobile apps, plugins, etc. All anyone needs to do is know how to make a POST request.

#### During the bootcamp

During the bootcamp, you will typically be making prototypes, where the pages are served by Flask, as well as the POST requests. If you use POST requests, rather than forms, you can keep the _same_ API code while retiring your `render_template` code.

Examples of how you would make prototypes during the bootcamp can be found in the `predictor_app` directory. Note that we can also swap out the templates very easily.
