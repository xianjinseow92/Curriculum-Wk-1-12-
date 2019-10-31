# SQL III: Questions

## Questions
1. _How many `Kate`s are there in California by year?_

2. _Which year had the most `Kate`s born in California?_

3. _What is the most popular boy's name in the South in 2000?_

  Note: `name_freq_region` is a view we created by joining the region to the `name_freq` table.

4. _What is the most popular girl's name in the South in 2000?_

5. _Which state has the greatest number of different names in 2000?_

6. _Which region has the greatest number of different names in 2000?_

7. _How many children were born in each state between 2000 and 2010? Treat "Between" as inclusive._

8. _Which state doesn't have a region associated with it?_
  Hint: you can find a list of distinct states by looking at
  ```sql
  SELECT DISTINCT(state) FROM name_freq;
  ```
  You should use a JOIN to connect this to the states in the region table.


9. _Rank the most popular androgynous names in 2000 (i.e. names that were given to both males and females)?_


  Challenge: There are quite a few popular names such as `Emily` that have a bulk of either male or female. Can you modify this query to calculate the absolute % difference between males and females, and then return those with the smallest difference (i.e. the most 'balanced' androgynous names).

10. _Which state has the highest % of `John`'s in a 2000?_

## Advanced - window functions

1. _What is the most popular girl's name in the South by year?_
This can be done with either a window function, or using a variation on the following trick:
```sql
select type, variety, price
from fruits
where (
   select count(*) from fruits as f
   where f.type = fruits.type and f.price <= fruits.price
) <= 2;
```

2. For each region, what is the most popular name for boys in 2010?
