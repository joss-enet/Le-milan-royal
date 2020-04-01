USE kickstarter;

SELECT nameProject, duration, usd_pledged, usd_goal, usd_pledged - usd_goal as pledgeSupplémentaire
FROM Facts
WHERE state = "successful"
ORDER BY duration DESC
LIMIT 30;