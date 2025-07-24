-- Consultas SQL para beneficiarios
-- Aquí puedes escribir SQL puro con autocompletado

-- 1. Obtener todos los beneficiarios de una CCAF específica
SELECT 
    beneficiario_id,
    ccaf,
    fecha_nacimiento,
    sexo
FROM beneficiarios 
WHERE ccaf = 'Los Héroes'
ORDER BY fecha_nacimiento;

-- 2. Obtener beneficiarios con sus licencias médicas
SELECT 
    b.beneficiario_id,
    b.ccaf,
    b.fecha_nacimiento,
    lm.licencia_id,
    lm.fecha_emision,
    lm.dias_licencia,
    lm.causa,
    lm.monto_subsidio_clp
FROM beneficiarios b
LEFT JOIN licencias_medicas lm ON b.beneficiario_id = lm.beneficiario_id
WHERE lm.fecha_emision >= '2024-01-01';

-- 3. Obtener total de beneficios por CCAF
SELECT 
    ccaf,
    COUNT(*) as total_beneficiarios,
    SUM(CASE WHEN sexo = 'M' THEN 1 ELSE 0 END) as hombres,
    SUM(CASE WHEN sexo = 'F' THEN 1 ELSE 0 END) as mujeres
FROM beneficiarios 
GROUP BY ccaf
ORDER BY total_beneficiarios DESC;