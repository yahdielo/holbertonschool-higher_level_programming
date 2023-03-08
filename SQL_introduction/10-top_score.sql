-- order from high scores
SELECT score, name FROM second_table ORDER BY CAST(`score` AS SIGNED) DESC;