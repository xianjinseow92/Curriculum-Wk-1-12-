# SQL Lab

_Structured Query Language_ (SQL) is a useful [declarative language](http://en.wikipedia.org/wiki/Declarative_programming) for working with data. It is usually supported (with some variation) by relational databases. The tutorialspoint [SQL Quick Guide](http://www.tutorialspoint.com/sql/sql-quick-guide.htm) is a handy cheat sheet for a lot of the syntax. As a data user, access to data will usually consist of a more or less complicated `SELECT` statement.

For joining data with SQL, this [Visual Explanation of SQL Joins](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) is quite good. One thing to note is that "join" will also often be known as "merge" in statistical software.

This lab uses the SQL playground provided in-browser by [W3Schools](http://www.w3schools.com/). Click [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) to go straight to the playground.

This is a pre-populated data environment with nothing to install and no risk of breaking anything. The data there is from a commonly-used example database ([info](http://northwinddatabase.codeplex.com/)). Nice!


## Guided

Let's walk through a few examples:

1) Retrieve all Customers from Madrid

```sql
SELECT
    * 
FROM
    Customers
WHERE
    City='Madrid';
```

2) How many customers are there in each city?

```sql
SELECT
    City, COUNT(*)
FROM
    Customers
GROUP BY
    City;
```

3) What is the most common city for customers? (And can you make it easy to find the correct answer?)

```sql
SELECT
    City, COUNT(*) AS count 
FROM
    Customers 
GROUP BY
    City 
ORDER BY
    count DESC;
```

4) What category has the most products?

```sql
SELECT
    CategoryName,
    COUNT(*) AS ProductCount
FROM
    Categories
  JOIN
    Products
  ON
    Categories.CategoryID = Products.CategoryID
GROUP BY
    CategoryName
ORDER BY 
    ProductCount DESC;
```


## Practice

 * Which customers are from the UK?
 * What is the name of the customer who has the most orders?
 * Which supplier has the highest average product price?
 * How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
 * What category appears in the most orders?
 * What was the total cost for each order?
 * Which employee made the most sales (by total cost)?
 * Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
 * Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)