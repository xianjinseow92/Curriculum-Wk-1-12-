# SQL III: Questions

## Questions
1. _How many `Kate`s are there in California by year?_

SELECT SUM(freq), name, year, state
FROM name_freq
WHERE name='Kate' AND state='CA'
GROUP BY year, name, state;

2. _Which year had the most `Kate`s born in California?_

SELECT sum, name, year FROM (
	SELECT SUM(freq), name, year, state
	FROM name_freq
	WHERE name='Kate' AND state='CA'
	GROUP BY year, name, state
	) AS number_of_kates_in_CA_by_year
ORDER BY sum DESC
LIMIT 3;


3. _What is the most popular boy's name in the South in 2000?_

  Note: `name_freq_region` is a view we created by joining the region to the `name_freq` table.

SELECT name, gender, freq, state, region
FROM (
	SELECT * 
	FROM name_freq_region 
	WHERE state='CA' AND year=2000) AS popular_boy_name_South_2000
WHERE gender='M'	
ORDER BY freq DESC
LIMIT 3;

4. _What is the most popular girl's name in the South in 2000?_

SELECT name, gender, freq, state, region
FROM (
	SELECT * 
	FROM name_freq_region 
	WHERE state='CA' AND year=2000) AS popular_boy_name_South_2000
WHERE gender='F'	
ORDER BY freq DESC
LIMIT 3;


5. _Which state has the greatest number of different names in 2000?_

SELECT COUNT(DISTINCT(name)) AS number_of_different_names_in_state, state 
FROM name_freq_region 
WHERE year=2000 
GROUP BY state 
ORDER BY COUNT(DISTINCT(name)) DESC
LIMIT 5;


6. _Which region has the greatest number of different names in 2000?_

SELECT COUNT(DISTINCT(name)) AS number_of_different_names_in_region, region 
FROM name_freq_region 
WHERE year=2000 
GROUP BY region 
ORDER BY COUNT(DISTINCT(name)) DESC
LIMIT 5;



7. _How many children were born in each state between 2000 and 2010? Treat "Between" as inclusive._


SELECT state, SUM(freq) AS no_of_children_born_between_2000_2010
FROM name_freq_region
WHERE year >= 2000 AND year <= 2010
GROUP BY state;


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
