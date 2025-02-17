WITH vw_socio AS (
    SELECT 
        year, 
        degree, 
        SUM(work_pop) AS total_work_pop_etario
    FROM projecoes2_banco.socio_table
    GROUP BY year, degree
    ORDER BY year, degree
)
SELECT * FROM vw_socio
-- FUNCIONA