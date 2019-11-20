# Allow Python to connect to MongoDB on AWS

Note: you need to make some configuration steps for each database. We will setup two databases: `cool` and `hot` (we will do `hot` at the end to show how to add additional databases).

All this work should be done on **AWS**. Before starting this guide, SSH into you AWS machine.

## Setup

### Allow your user access to the database

1. Type `mongo` in the (AWS) terminal
2. Connect to the database `use cool`
3. Now create a user. You can call the user anything you want. We will use `mongo_user`, and give her read/write access to the database `cool`. We are also setting her password to `password`, which you are welcome (and encouraged!) to change:
```mongodb
db.createUser({
    user: 'mongo_user',
    pwd:  'password',
    roles: [{ role: 'readWrite', db: 'cool' }]
});
```
4. Create an admin user as well, after connecting to the admin database
```mongodb
use admin

db.createUser({
  user: 'admin',
  pwd: 'secure_password',
  roles: [{ role: 'userAdminAnyDatabase', db: 'admin'}]
});
```
5. Quit out of mongo:
```
quit()
```

### Edit the MongoDB config file

Before anyone could connect to the databases we created, as long as they were logged on to AWS. Now we are going to change the config file to do two things:
* Allow connections from outside
* Ensure anyone connecting to the database has to supply their username and password
It is important that you do both of these.

1. Open up the config file using vim or nano: `sudo vim /etc/mongod.conf`. You need `sudo`, otherwise you can't save changes to your file.
2. You should find a section that reads
```
# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1
```
Change the last line to
```
# network interfaces
net:
  port: 27017
  bindIp: 0.0.0.0
``` 
This opens up the computer to everyone
3. Find the section: `#security`
4. Change this to (and be careful with indent):

```
security:
  authorization: 'enabled'
```
   

Note that the leading comment character `#` has been removed!
4. Exit and save (Escape, q, w in vim)

### Opening Port 27017 on your AWS instance

We have told Mongo to allow anyone with the username and password to connect to MongoDB. Now we have to tell the _instance_ to allow requests at port 27017 into the computer so Mongo can respond to them. 
1. Go to your AWS console at http://aws.amazon.com
2. Select this instance, and find 'security groups'. You should have a link with something similar to `launch-wizard-1` (or whatever you named your security group). Click this link.
3. Click the tab "Inbound", and then the button "Edit"
4. Add a rule with the following information:
   | Type | Protocol | Port Range | Source | Description | 
   | --- | --- | --- | ---| --- |
   | Custom TCP IP | TCP | 27017 | Anywhere (should fill `0.0.0.0/0, ::/0`) | Mongo |
5. Click Save

### Restart the service

Back on the terminal, restart the service with
```bash
sudo service mongod restart
```

If everything has been successful, the following should **work**:
```bash
mongo
```
You will be given an error message that you are not allowed to connect (because you have not provided a username or password). To connect now, do
```bash
mongo -u mongo_user -p password 127.0.0.1/cool
```
This will connect you to the `cool` database (mongo uses port 27017 by default, you can change to 127.0.0.1:27017/cool to be more explicit)

## Connecting from your local machine

To connect from your local machine, you will need the IP address of your AWS instance. I will use `xxx.xxx.xxx.xxx`. To log on from your local machine, type
```bash
mongo -u mongo_user -p password xxx.xxx.xxx.xxx/cool
```

To connect via Python, use
```python
from pymongo import MongoClient
config = {
  'host': 'xxx.xxx.xxx.xxx:27017',
  'username': 'mongo_user',
  'password': 'password',
  'authSource': 'cool'
}

client = MongoClient(**config)

db = client.cool
```

## Connecting to another database

Suppose we wanted to allow the same user to connect to another database, `hot`. We first connect as `admin`:
```bash
mongo -u admin -p secure_password xxx.xxx.xxx.xxx/admin
```

Once Mongo is running, we can _alter_ our existing mongo user. Because this user was created in the database `cool`, we need to connect to it first:
```
use cool 
db.grantRolesToUser("mongo_user", [{ role: 'readWrite', db: 'hot'}])
```