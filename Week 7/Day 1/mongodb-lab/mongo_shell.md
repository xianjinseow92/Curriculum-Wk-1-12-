# Mongo shell

Most of the time, you will use `pymongo` to connect Python to Mongo. When using AWS, or trying to debug why `pymongo` won't connect, it is useful to be able to know the basics of the shell (terminal) version of Mongo.

The shell version of Mongo uses Javascript with some Mongo specific extensions, so if you are familiar with JS you can define functions and save results to variables in the shell.

## Starting mongod

We need to start the mongo daemon `mongod` to listen and serve requests. The way we do this differs a little on OSX and ubuntu. If you get completely stuck, you can just run `mongod` in your terminal (but you will need to open a new terminal window, as that one will not be used by the mongo daemon).

If you installed mongo using brew on OSX, you can run
```bash
brew services start mongodb
```

If you installed mongo on ubuntu, you can run
```
sudo service mongod start
```

Annoyingly, `brew` and the Ubuntu `service` command swap the order: one is `service_name start`, the other is `start <service_name>`.

## Importing data

If we have data stored in a JSON file, we can use the shell command `mongoimport` to transfer the file all at once.

We are going to create two databases: `books` and `outings`, and insert data into them.

1. In terminal, go to today's lesson
2. Run the following commands:
```bash
mongoimport --db books --collection author --file data/author.json
mongoimport --db books --collection catalog --file data/catalog.json
mongoimport --db outings --collection restaurant --jsonArray --file data/chicago_restaurant.json
```

The `books` database has two collections: `author` (with the information from `author.json`) and `catalog` (wtth the information from `catalog.json`). The `outings` collection just has a `restaurant` collection, with the data from `chicago_restaurant.json`

## Using `mongo` shell

In the terminal, start by loading `mongo`. At the prompt, connect to the `outings` database using the `use` command:

```js
> use outings;
switched to db outings
> show collections;
restaurant
```

The current database that we are using has the built-in variable name `db`. Mongo commands take the form
```js
db.<collection name>.<command>(arguments)
```

#### Using `.find({.....})`

Let's look at a document. We can look at a single restaurant with `findOne()`:
```js
> db.restaurant.findOne()
{
	"_id" : ObjectId("5bf25227268f1af309ea06b1"),
	"id" : 149062,
	"name" : "Osteria Langhe",
	"address" : "2824 West Armitage Avenue",
	"city" : "Chicago",
	"state" : "IL",
	"area" : "Chicago / Illinois",
	"postal_code" : "60647",
	"country" : "US",
	"phone" : "7736611582x",
	"lat" : 41.917688,
	"lng" : -87.698281,
	"price" : 2,
	"reserve_url" : "http://www.opentable.com/single.aspx?rid=149062",
	"mobile_reserve_url" : "http://mobile.opentable.com/opentable/?restId=149062",
	"image_url" : "https://www.opentable.com/img/restimages/149062.jpg"
}
```
The object returned is a javascript object (similar to a Python dictionary).

We can pass objects to `find` to restrict what we get back. Here are some examples of things to try:
```js
> // returns restaurants with a price rating of 2, and prints them nicely
> db.restaurant.find({'price': 2}).pretty()
// 11 documents are printed out

> // returns restaurants with a name that contains "Caf" and price rating of 2.
> // Note no quotes around /Caf/ (this is a regex)
> db.restaurant.find({'price':2, 'name': /Caf/}).pretty()
// 2 documents are printed out
```

What if we wanted to find restaurants with a price rating of _at least_ 3, instead of exactly 2? In this case, we would have to use mongo _operators_, which have dollar signs in them. The operator for "greater than or equal to" is `$gte`.
```js
> // returns restaurants with a price rating greater than or equal to 3:
> db.restaurant.find({'price': {'$gte': 3}}).pretty()
// 14 documents are printed
```

If we just want the count, we can chain `.count()` to the end:
```js
> db.restaurant.find({'price': {'$gte': 3}}).count()
14
```

The `find()` command is similar to the SQL `SELECT` statement. The first argument of find is similar to the `WHERE` clause, as it tells us what conditions have to be met for the document to be returned.

#### Using `.find({....}, {....})`

The `find` command can take a second argument which tells us which fields to return. For example, if we are only interested in the names and addresses of the 3+ rated restaurants, we can write:
```js
> db.restaurant.find({'price': {'$gte': 3}}, {'name': 1, 'address': 1})
{ "_id" : ObjectId("5bf25227268f1af309ea06b2"), "name" : "Chicago Chop House", "address" : "60 W Ontario St" }
{ "_id" : ObjectId("5bf25227268f1af309ea06b3"), "name" : "10pin Bowling Lounge", "address" : "330 N State Street" }
{ "_id" : ObjectId("5bf25227268f1af309ea06b5"), "name" : "Signature Room at the 95th", "address" : "875 N. Michigan Avenue" }
{ "_id" : ObjectId("5bf25227268f1af309ea06b7"), "name" : "goosefoot", "address" : "2656 W Lawrence Ave" }
{ "_id" : ObjectId("5bf25227268f1af309ea06bb"), "name" : "The Terrace Rooftop  Bar  Restaurant", "address" : "Conrad Chicago" }
{ "_id" : ObjectId("5bf25227268f1af309ea06bc"), "name" : "Anteprima", "address" : "5316 N Clark Street" }
{ "_id" : ObjectId("5bf25227268f1af309ea06be"), "name" : "Gibsons Bar & Steakhouse - Chicago", "address" : "1028 North Rush" }
{ "_id" : ObjectId("5bf25227268f1af309ea06c0"), "name" : "Ditka's - Chicago", "address" : "100 E. Chestnut Street" }
{ "_id" : ObjectId("5bf25227268f1af309ea06c1"), "name" : "L2O", "address" : "2300 N. Lincoln Park West" }
{ "_id" : ObjectId("5bf25227268f1af309ea06c2"), "name" : "RL Restaurant", "address" : "115 E Chicago Ave" }
{ "_id" : ObjectId("5bf25227268f1af309ea06c5"), "name" : "Macku Signature", "address" : "2925 N Halsted St" }
{ "_id" : ObjectId("5bf25227268f1af309ea06c7"), "name" : "David Burke's Primehouse in the James Hotel", "address" : "616 N Rush Street" }
{ "_id" : ObjectId("5bf25227268f1af309ea06c8"), "name" : "Coco Pazzo", "address" : "300 West Hubbard" }
{ "_id" : ObjectId("5bf25227268f1af309ea06c9"), "name" : "The Capital Grille - Chicago - Downtown", "address" : "633 North Saint Clair" }
```
Notice that the object `_id` assigned by mongo is returned by default (even though we didn't specify it). We can switch this one off:

```js
> db.restaurant.find({'price': {'$gte': 3}}, {'name': 1, 'address': 1, '_id': 0})
{ "name" : "Chicago Chop House", "address" : "60 W Ontario St" }
{ "name" : "10pin Bowling Lounge", "address" : "330 N State Street" }
{ "name" : "Signature Room at the 95th", "address" : "875 N. Michigan Avenue" }
{ "name" : "goosefoot", "address" : "2656 W Lawrence Ave" }
{ "name" : "The Terrace Rooftop  Bar  Restaurant", "address" : "Conrad Chicago" }
{ "name" : "Anteprima", "address" : "5316 N Clark Street" }
{ "name" : "Gibsons Bar & Steakhouse - Chicago", "address" : "1028 North Rush" }
{ "name" : "Ditka's - Chicago", "address" : "100 E. Chestnut Street" }
{ "name" : "L2O", "address" : "2300 N. Lincoln Park West" }
{ "name" : "RL Restaurant", "address" : "115 E Chicago Ave" }
{ "name" : "Macku Signature", "address" : "2925 N Halsted St" }
{ "name" : "David Burke's Primehouse in the James Hotel", "address" : "616 N Rush Street" }
{ "name" : "Coco Pazzo", "address" : "300 West Hubbard" }
{ "name" : "The Capital Grille - Chicago - Downtown", "address" : "633 North Saint Clair" }
```

The second argument is the _projection_ -- it tells us which fields to return. It is similar to the list of field names you give in SQL. If the restaurants were stored in a SQL database instead, then the equivalent SQL would be
```sql
SELECT name, address FROM restaurant WHERE price >= 3;
```

The projection object has to follow some rules:
1. If we have `field: 1` in the object, then we are starting with nothing and building up (i.e. fields are only included if they are mentioned explicitly). The `_id` field is special, and is included even if not mentioned.
2. If we have `field: 0` in the object, then we are starting with all the fields and excluding (i.e. fields are only excluded if they are mentioned explicitly)
3. You have to build up or build down -- you cannot mix `field: 1` and `field: 0`. The exception to this rule is `_id` which can be turned on or off explicitly (default is on).

Here are some examples:
* ALLOWED: includes `name`, `address`, `price`, and `_id` (default)

  `db.restaurant.find({}, {'name': 1, 'address': 1, 'price': 1})`
* ALLOWED: includes `name`, `address`, and `price`, while excluding `_id`

  `db.restaurant.find({}, {'name': 1, 'address': 1, 'price': 1, '_id': 0})`

* ALLOWED: includes all fields except `lat` and `lng`

  `db.restaurant.find({}, {'lat': 0, 'lng': 0})`

* ILLEGAL: mixes `0` and `1`, unclear whether fields not mentioned should be included or excluded:

  `db.restaurant.find({}, {'name': 1, 'address': 1, 'price': 1, 'lat': 0})`

#### Using javascript

We can store objects using standard javascript syntax as well:
```js
> let cheap_filter = {'price': {'$lte': 3}}
> let projection = {'price': 1, 'address': 1, 'name': 1, '_id': 0}
> db.restaurant.find(cheap_filter, projection).sort({'price': 1});
{ "name" : "Osteria Langhe", "address" : "2824 West Armitage Avenue", "price" : 2 }
{ "name" : "Café Ba-Ba-Reeba", "address" : "2024 North Halsted St.", "price" : 2 }
{ "name" : "Gaudí Café", "address" : "1147 W Grand Ave", "price" : 2 }
{ "name" : "Sola", "address" : "3868 N Lincoln", "price" : 2 }
{ "name" : "Fat Rice", "address" : "2957 W. Diversey Ave", "price" : 2 }
{ "name" : "Spencer's Jolly Posh Foods", "address" : "3755 N Southport", "price" : 2 }
{ "name" : "HUB 51", "address" : "51 W. Hubbard", "price" : 2 }
{ "name" : "Kamehachi of Tokyo - Wells Street", "address" : "1531 N Wells Street", "price" : 2 }
{ "name" : "Bottlefork", "address" : "441 North Clark Street", "price" : 2 }
{ "name" : "AraOn", "address" : "160 W. Adams Street", "price" : 2 }
{ "name" : "Chuck's: A Kerry Simon Kitchen", "address" : "224 North Michigan Ave", "price" : 2 }
{ "name" : "The Terrace Rooftop  Bar  Restaurant", "address" : "Conrad Chicago", "price" : 3 }
{ "name" : "Anteprima", "address" : "5316 N Clark Street", "price" : 3 }
{ "name" : "Ditka's - Chicago", "address" : "100 E. Chestnut Street", "price" : 3 }
{ "name" : "RL Restaurant", "address" : "115 E Chicago Ave", "price" : 3 }
{ "name" : "Macku Signature", "address" : "2925 N Halsted St", "price" : 3 }
{ "name" : "David Burke's Primehouse in the James Hotel", "address" : "616 N Rush Street", "price" : 3 }
{ "name" : "Coco Pazzo", "address" : "300 West Hubbard", "price" : 3 }
```

#### Exiting

Type `quit()` to exit the mongo shell.

## Summary

* `mongo` (or mongo shell) is a terminal application that runs an extended version of javascript
* `mongo` shell is useful for doing quick queries, or checking `mongod` is running.
* Most of the time, you will be using Python and the `pymongo` package to interact with mongo. More on that in the [next notebook](MongoLab_student.ipynb).
