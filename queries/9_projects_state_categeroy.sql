USE kickstarter;

SELECT state, nameMainCategory, nameCategory, COUNT(*)
FROM Facts NATURAL JOIN MainCategory NATURAL JOIN Category
GROUP BY state, nameMainCategory, nameCategory WITH ROLLUP;