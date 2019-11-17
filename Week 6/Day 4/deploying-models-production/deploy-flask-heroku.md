# Deploying Flask Apps on Heroku

Heroku is a cloud-based "platform-as-a-service" provider where you can easily deploy your own Python apps and share them with anyone on the Internet. Their pitch to developers is 

> _Invest in apps, not ops. Heroku handles the hard stuff — patching and upgrading, 24/7 ops and security, build systems, failovers, and more — so your developers can stay focused on building great apps._ 

In this lab, we're going to cover the steps needed to deploy our iris predictor Flask app to Heroku. 

## 0. Run Your App With Gunicorn

From Wikipedia, _The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server. It is a pre-fork worker model, ported from Ruby's Unicorn project. The Gunicorn server is broadly compatible with a number of web frameworks, simply implemented, light on server resources and fairly fast._

There are a number of reasons why we may want to run our flask apps using gunicorn instead of just launching them with Python, but the reason we care about today is that Heroku isn't going to let us run the app from Python.

You can install Gunicorn with `conda install gunicorn`

Now, from your flask app's directory, if you are using the flask app solution from last week's lecture, you can launch your app on a local server with the command

`$ gunicorn predictor_app:app`

This syntax (`gunicorn app_file:app_object`) is the simplest way to run a flask app using gunicorn. Note that the `.py` extension is dropped!

## 1. Create a Free Heroku Account

First, head to [Heroku.com](https://signup.heroku.com/) and sign up for a free account. Choose student or hobbyist for your Role on the signup form. You may have to wait a minute or two for a confirmation email, and then you can create a password and log in to your account. 

## 2. Install the Heroku CLI tool

Install the Heroku CLI tool. You can do this on macOS with homebrew using the command `brew install heroku/brew/heroku`, or on Linux with `sudo snap install heroku --classic`

The Heroku CLI tool includes an implementation of Git and is integrated with Heroku's platform so that you can deploy your app from the command line.

## 3. Create Your Flask App

We've already done this, so just create a new directory wherever you keep your source code repos and copy over the files from the  `project-03/flask-web-apps/solution` directory. We will need to add some new files to get this to work on Heroku.

**DO NOT attempt to do this without copying the files to a new directory!** We are toing to create a new git repo inside of our webapp directory and it's a very bad idea to create git repos inside of folders that are part of another repository.

First we need to create a `requirements.txt` file so that Heroku knows what Python libraries it needs to build your app. Create `requirements.txt` in your app's top level directory and fill it with this text:

```python
flask
gunicorn
numpy
scikit-learn
```

These are the libraries we need to install in order to run our flask app. Note that `scikit-learn` is not explicitly imported in our code, but we do load a pickled sklearn model to make our predictions. On our local machines this will also import `scikit-learn` into our namespace but this code will crash in environments that do not have sklearn installed. 

We do not need to include `pickle` in our requirements file, since that library is included in all python installations. 

We are going to tell Heroku to use `gunicorn` to set up the HTTP server for our flask app. We give it this instruction in the `Procfile`. In your top level directory, create a file called `Procfile`, and fill it with the following text:

```
web: gunicorn predictor_app:app
```

The `web: ` command tells Heroku to run this code at the command line in the environment that it creates to host our web app.

Let's also give our flask app a more useful landing page. Open `html/index.html` and replace its contents with the following:

```html
<!DOCTYPE html>
<html>
<head>
	<title> Heroku Flask App Demo </title>
    <link rel="stylesheet" type="text/css"  href="/static/css/main.css">
</head>
<body>
	<h1> Hello Heroku World </h1>
	<p>
		This is a bare bones flask app.
		All we're doing here is showing how to use Flask
		to share working demos of our scikit-learn models online.
	</p>

<a href="/predict">Take a look at our Iris classifier.</a>

<img src="/static/images/iris_coefs.png" alt="My charts" >

</body>
</html>
```

This provides a basic description of what we're doing here, and includes the chart with our estimated Iris classifier coefficients from the notebook we used to train our model. That chart lives in a subdirectory `/static/images`. There is nothing special about the directory name `static`, but Heroku (or gunicorn or flask) did not seem to like it when I put an `images` directory at the top level. The reason why is left as an exercise for the reader.

## 4. Deploy Your App to Heroku

Open a terminal window inside your new directory and create your Heroku app:

`$ heroku create`

Heroku will generate a random app name for you, unless you give it a name you would like to use. But app names must be unique among all other Heroku apps, and you will get an error message if your app name is already taken. If you don't want to use a random app name, you'll just have to use trial and error to find something that's available.

This command worked for me:

```bash
$ heroku create whats-that-pretty-flower
```



Now you'll want to initialize a git repository and create a remote repo on Heroku. Run these commands in your terminal

```
$ git init
$ heroku git:remote -a <your-app-name>
$ git add .
$ git commit -am "first commit"
$ git push heroku master
```

When you push your git repo to Heroku, it will detect (from your requirements file) that this is a Python app, and download and install the required libraries to the environment where Heroku will be hosting your app. Heroku then executes the commands in your Procfile to run your app on its platform in the environment it just built. Once all of the installation messages are finished running, and assuming there are no errors, your app should be accessible at the url printed under the `Launching...` comment in the build output.

```
cliffclive@conxn-mac:~/src/whats-that-pretty-flower$ git push heroku master
Counting objects: 14, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (13/13), done.
Writing objects: 100% (14/14), 30.19 KiB | 10.06 MiB/s, done.
Total 14 (delta 3), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing requirements with pip
remote: 
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 98.4M
remote: -----> Launching...
remote:        Released v5
remote:        https://whats-that-pretty-flower.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/whats-that-pretty-flower.git
   582272d..da77ce1  master -> master

```

Congratulations! Your app has been pushed to Heroku. However, before it can be accessed from the web, you'll need to tell Heroku how many processes it will need to dedicate to serving your app. Since this is just a small demo, we'll start it out with just one. Enter this at your command line:

```bash
$ heroku ps:scale web=1
```

And now it's up and running. You can find it at the url in the end of the text output from your Heroku push command (`https://whats-that-pretty-flower.herokuapp.com/` in my case).

( [It should look something like this.](https://whats-that-pretty-flower.herokuapp.com/) )

What if it breaks? First, try restarting the web app:

```bash
$ heroku ps:scale web=0  # switch the app off
$ heroku ps:scale web=1  # switch the app on
```

If that doesn't work, look at the logs with `$ heroku logs --tail`.

## 5. Sprucing Up Your Deployment

It's not pretty, but it works. Other things you may want to look into, which are outside of the scope of this lecture, could include 

- using better HTML and CSS code (or finding templates online) to improve the layout of your web app
- installing a [Heroku add-on](https://elements.heroku.com/addons) to add more functionality to your app (Papertrail is a good one to keep logs of your app's user interactions.)
- incorporate a [Heroku Postgres](https://www.heroku.com/postgres) database in your app
- set up [Continuous Integration](https://www.heroku.com/continuous-integration) so that any future changes you push to your web app will not be deployed if they can't pass unit tests (even if they run on heroku local, that's no guarantee!)

