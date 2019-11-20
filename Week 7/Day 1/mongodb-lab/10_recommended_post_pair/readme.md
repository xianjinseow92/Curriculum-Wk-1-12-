This is a suggested pair for the day _after_ the students have completed the mongo lab.

It acts to reinforce several key concepts. As designed, we are
* Reinforcing the `requests` library / `curl` by GET-ing the data
* Reminding students how to do `insertMany` to a collection from Python (i.e. given the list of dictionaries, make many documents)
* Reinforcing the main thing we do with databases -- selection. Selection covers `find`, `distinct` and `aggregate` pipelines.

One thing that we **don't** cover in this exercise is how to load data from flat files (e.g. `.json` files). This isn't a huge deal -- even without this skill, students can always load files into memory and then `insert` them into the database. 

Because I cannot guarantee the availability of the API endpoint that provides the data forever, I have "frozen" a copy of the data as it existed on November 18th 2018 in the directory `backup_data`. If the API  endpoint is down, walk the students through loading the data from this file instead. If everything is working as expected, this file will not be needed.
