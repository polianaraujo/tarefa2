WITH vw_salario AS (
    SELECT 
        year, 
        incomplete, 
        elementary, 
        high, 
        college, 
        `age_14_29`, 
        `age_30_49`, 
        `age_50_59`, 
        `age_60_plus`
    FROM projecoes2_banco.salario_table
    ORDER BY year;
) SELECT * FROM vw_salario;
-- FUNCIONA