WITH vw_projecao AS (
    SELECT 
        year,
        (pop_h + pop_m) AS pop_t,
        e0_t,
        e60_t
    FROM projecoes2_banco.projecoes2_table
) SELECT * FROM vw_projecao;
-- FUNCIONA