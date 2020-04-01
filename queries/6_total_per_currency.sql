USE kickstarter;

SELECT nameCurrency, SUM(pledged), SUM(usd_pledged), COUNT(*)
FROM Facts NATURAL JOIN Currency
GROUP BY nameCurrency
ORDER BY SUM(usd_pledged) DESC;