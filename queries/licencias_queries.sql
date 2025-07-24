-- Tamaño y composicion del gasto en licencias
select
	lm.causa,
	sum(lm.monto_subsidio_clp) as total_clp,
	count(*) as n_licencias,
	avg(lm.dias_licencia) as dias_prom,
	min(lm.dias_licencia) as dias_min,
	max(lm.dias_licencia ) as dias_max
from licencias_medicas  lm
group by causa
order by total_clp desc;


-- Tiempo promedio de pago por CCAF
SELECT
    ccaf,
    AVG((fecha_pago - fecha_emision)::integer) AS demora_prom_dias
FROM licencias_medicas
WHERE estado_pago = 'Pagado'
GROUP BY ccaf;

-- Beneficiarios con licencias reiteradas (>=3 en 12 meses)
WITH r AS (
  SELECT beneficiario_id,
         COUNT(*) AS lics_12m
  FROM licencias_medicas
  WHERE fecha_emision >= CURRENT_DATE - INTERVAL '12 months'
  GROUP BY beneficiario_id
)
SELECT * FROM r WHERE lics_12m >= 3;

