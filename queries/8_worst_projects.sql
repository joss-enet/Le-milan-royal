USE kickstarter;

SELECT nameProject, nameMainCategory, financingRate, goal, pledged, nameCurrency
FROM Facts NATURAL JOIN Currency NATURAL JOIN MainCategory
WHERE state = "failed" AND financingRate <> 0
ORDER BY financingRate ASC
LIMIT 25;