USE kickstarter;

SELECT nameCountry,COUNT(state) as countSuccessful, countTotal, COUNT(state)/ countTotal as Rate
FROM Country NATURAL JOIN Facts JOIN (
   SELECT idCountry, COUNT(state) as countTotal
   FROM Facts
   GROUP BY idCountry
) AS failed ON Facts.idCountry = failed.idCountry
WHERE state="successful"
GROUP BY Facts.idCountry, nameCountry
ORDER BY Rate DESC;