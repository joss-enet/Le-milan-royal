USE kickstarter;

SELECT nameMainCategory, nameCategory, COUNT(*), ROUND(SUM(usd_pledged), 2), ROUND(AVG(usd_pledged), 2)
FROM Facts NATURAL JOIN MainCategory NATURAL JOIN Category
GROUP BY nameMainCategory, nameCategory WITH ROLLUP
UNION
SELECT nameMainCategory, nameCategory, COUNT(*), ROUND(SUM(usd_pledged), 2), ROUND(AVG(usd_pledged), 2)
FROM Facts NATURAL JOIN MainCategory NATURAL JOIN Category
GROUP BY nameCategory, nameMainCategory WITH ROLLUP;