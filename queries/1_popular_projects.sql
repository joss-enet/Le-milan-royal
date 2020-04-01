USE kickstarter;

SELECT nameProject, pledged, nameCountry, nameCategory
FROM Facts NATURAL JOIN Country NATURAL JOIN Category
WHERE nameCategory="Hardware"
ORDER BY pledged DESC
LIMIT 50;