USE kickstarter;

SELECT nameCountry, population, COUNT(*), SUM(usd_pledged)
FROM Facts NATURAL JOIN Country
GROUP BY nameCountry, population
ORDER BY population DESC;