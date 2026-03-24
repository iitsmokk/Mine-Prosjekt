-- ============================================================================
-- TEST-SKRIPT FOR OBLIG 1
-- ============================================================================

-- Kjør med: docker-compose exec postgres psql -h -U admin -d data1500_db -f test-scripts/queries.sql

SELECT sykkel_id FROM sykkel;

SELECT etternavn, fornavn, tlf_nr FROM kunde ORDER BY etternavn ASC;

SELECT sykkel_id FROM utleie WHERE utleie_tidspunkt > '2023-03-01 00:00:00' ;

SELECT COUNT (kunde_id) AS AntallKunder FROM kunde;

SELECT k.kunde_id, COUNT(u.ordre_nr) AS AntallLeier FROM kunde k LEFT JOIN utleie u ON k.kunde_id = u.kunde_id GROUP BY k.kunde_id;

SELECT k.kunde_id, COUNT(u.ordre_nr) AS AntallLeier
FROM kunde k 
LEFT JOIN utleie u 
ON k.kunde_id = u.kunde_id 
GROUP BY k.kunde_id
HAVING COUNT(u.ordre_nr) = 0;

SELECT s.sykkel_id, COUNT(u.ordre_nr) AS AntallLeier
FROM sykkel s
LEFT JOIN utleie u 
ON s.sykkel_id = u.sykkel_id
GROUP BY s.sykkel_id
HAVING COUNT(u.ordre_nr) = 0;




