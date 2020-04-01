USE kickstarter;

SELECT year, month, Count(*) as nombreKickstarter
FROM Facts JOIN DateTime ON idDateTimeLaunch = idDateTime
WHERE year> 2016
GROUP BY year,month with ROLLUP
ORDER BY nombreKickstarter;