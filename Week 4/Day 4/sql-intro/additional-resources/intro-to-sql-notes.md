# Agenda

 - Intro
 - Syntax
 - Practical concerns
 - Examples
 - Resources

# Intro

[SQL](https://en.wikipedia.org/wiki/SQL) stands for Structured Query Langauge, and and is the most common portal to using structured data. It is likely the most common skillset in Data Science. 

SQL databases allow companies to store massive amounts of data, and allows users to efficiently pull relevant subsets and aggregates from that data. 

Specifically, SQL allows for:

 - A single syntax across many databases
 - Storing and accessing arbitrarily large data sets
 - Flexibility to integrate into many workflows

SQL has similar goals to Pandas, but tends to be easier to use. Additionally, SQL is an internationally supported standard, whereas Pandas was developed primarily for the Python data ecosystem. 

# Syntax

Below are the core commands for SQL:

 - `JOIN`: Combining two tables into a single table, using a shared 'foreign key'
 - `WHERE`: Removing observations that do not meet the specified criteria
 - `GROUP BY`: Aggregating by a single key
 - `HAVING`: Same as `WHERE`, but performed after `GROUP BY`
 - `ORDER BY`: Order observations. 
 - `LIMIT`: Limit to a specific number of observations

There are also a few common commands for SQL:

 - `COUNT()`: The number of observations in a table, or for a key in a `GROUP BY` sub-table
 - `AS`: Give an alias
 - `AVG()`
 - `SUM()`
 - `DISTINCT`: Provide only unique responses (convert the array into a set)

# Practical concerns

 - Many different DBs with slightly different syntaxes
 - Union & Union all: Concatenate results from multiple queries
 - Random samples: Can be handled by creating a column with random values

# Hands on

## Examples

For a brief intro to try out queries on a pre-loaded database, see [w3schools](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)

## Lab

The best way to learn is by doing. 

To get a hands-on experience with SQL, complete all sections of the following HackerRank SQL sections:

 - [Basic Select](https://www.hackerrank.com/domains/sql/select)
 - [Aggregation](https://www.hackerrank.com/domains/sql/aggregation) (SQL's `groupby` equivalent)

# Resources

 - [Syntax cheat sheet](https://zeroturnaround.com/rebellabs/sql-cheat-sheet/): Great to have by your side
 - [Pandas to SQL](https://codeburst.io/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e): Great for translating pandas commands into SQL queries
 - [Khan Academcy](https://www.khanacademy.org/computing/computer-programming/sql/sql-basics/v/s-q-l-or-sequel): Video series on SQL
 - [FB prep](https://www.quora.com/How-do-I-prepare-for-a-Facebook-Data-Science-Analytics-phone-interview): Guides for prepping for a SQL interview
 - [Database Systems: The Complete Book (2nd Edition)](https://www.amazon.com/Database-Systems-Complete-Book-2nd/dp/0131873253): The (graduate level) reference on databases
