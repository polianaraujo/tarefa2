WITH vw_pop AS (
SELECT 
    ano,
    SUM(pop_t) AS populacao_total,
    SUM(pop_h) AS populacao_homens,
    SUM(pop_m) AS populacao_mulheres
FROM projecoes2_banco.projecoes2_table
GROUP BY ANO
) SELECT * FROM vw_pop
