WITH vw_etario AS (
    SELECT 
        year, 
        features, 
        SUM(work_pop) AS total_work_pop_etario
    FROM projecoes2_banco.etario_table
    GROUP BY year, features
    ORDER BY year, features
)
SELECT * FROM vw_etario
-- FUNCIONA