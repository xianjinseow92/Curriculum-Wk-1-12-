# MongoDB Installation

Everybody should install the `pymongo` package for later:

```bash
conda install pymongo
```

The instructions on how to install MongoDB will differ by platform:

- Instructions for [Mac OSX](#os_x)
- Instructions for [Windows](#windows)
- Instructions for [ubuntu](#ubuntu)
- Instructions for [AWS](#aws)

## OS X

You should probably use the homebrew installation. If you don't already have homebrew installed, you can install it by typing the following into your terminal:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Installation steps (run these in the terminal)
1. Make sure that brew is updated
```bash
brew update
```
2. Install MongoDB
```bash
brew install mongodb
```
3. Create a data directory for MongoDB, and set permissions
```bash
sudo mkdir -p /data/db
sudo chown -R `id -un` /data/db
```

>Congratulations -- you have installed MongoDB!

### Running MongoDB

To start the daemon (the piece that runs in the background):

```bash
mongod
```
You *need* this, otherwise there is nothing to connect to. It will keep giving status updates, so you will need another terminal to connect to. Don't use `mongod &` as your terminal will get flooded with logging messages.

To start an interactive session, in a new terminal type
```bash
mongo
```
This should bring up the mongo terminal. Type `quit()` to exit back to the terminal.

## Windows

The mongo installation instructions for Windows are [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/). 

## Ubuntu

These instructions are for version 16.04 of Ubuntu. You can try them for other versions, but you may have to do a google search to find instructions for your specific version.

### Installation

In a terminal, type:

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.0.asc | sudo apt-key add -

echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
```


Then update your local package database and install MongoDB Community Edition

```bash
sudo apt-get update
sudo apt-get install -y mongodb-org
```


### Starting the service

You should start the service with `sudo service mongod start`. There are other commands related to starting and stopping the mongodb daemon:

```
sudo service mongod status
sudo service mongod stop
sudo service mongod start
```

### Opening mongo in a terminal

Go to a terminal and type `mongo` to run. To exit, type `quit()`

## AWS

If you are using AWS, you can follow the instructions for installing on ubuntu. You will need a few additional steps so that you can connect python on your local machine to MongoDB on AWS.

Once you have that setup, you should follow the instructions for [allowing python on your local machine to connect to mongo on AWS](python_to_aws_mongo_setup.md)