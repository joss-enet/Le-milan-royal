USE kickstarter;

SELECT nameCountry,COUNT(state) as countSuccessful, countFailed, COUNT(state)/ countFailed as Rate
FROM Country NATURAL JOIN Facts JOIN (
   SELECT idCountry, COUNT(state) as countFailed
   FROM Facts
   GROUP BY idCountry
) AS failed ON Facts.idCountry = failed.idCountry
WHERE state=”successful”
GROUP BY nameCountry
ORDER BY Rate DESC;