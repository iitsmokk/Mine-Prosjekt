-- ============================================================================
-- DATA1500 - Oblig 1: Arbeidskrav I våren 2026
-- Initialiserings-skript for PostgreSQL
-- ============================================================================

-- Opprett grunnleggende tabeller
CREATE TABLE kunde (
    kunde_id SERIAL PRIMARY KEY,
    fornavn VARCHAR(100) NOT NULL,
    etternavn VARCHAR(100) NOT NULL,
    epost TEXT UNIQUE NOT NULL,
    tlf_nr CHAR(8) UNIQUE NOT NULL,

    CONSTRAINT maks_8_siffer
        CHECK(tlf_nr ~'^[0-9]{8}$')
);

CREATE TABLE sykkel_stasjon (
    stasjon_id SERIAL PRIMARY KEY,
    stasjon_posisjon TEXT
);

CREATE TABLE sykkel (
    sykkel_id SERIAL PRIMARY KEY,
    stasjon_id INTEGER,

    FOREIGN KEY (stasjon_id) REFERENCES sykkel_stasjon(stasjon_id),

    låst BOOLEAN,
    utlevert BOOLEAN
);



CREATE TABLE utleie (
    ordre_nr SERIAL PRIMARY KEY,

    sykkel_id INTEGER NOT NULL,
    kunde_id INTEGER NOT NULL,
    utleie_stasjon_id INTEGER NOT NULL,
    innlevering_stasjon_id INTEGER,

    leiebeløp DECIMAL(8, 2),
    utleie_tidspunkt TIMESTAMP NOT NULL,
    innlevering_tidspunkt TIMESTAMP,

    FOREIGN KEY (sykkel_id) REFERENCES sykkel(sykkel_id),
    FOREIGN KEY (kunde_id) REFERENCES kunde(kunde_id),
    FOREIGN KEY (utleie_stasjon_id) REFERENCES sykkel_stasjon(stasjon_id),
    FOREIGN KEY (innlevering_stasjon_id) REFERENCES sykkel_stasjon(stasjon_id)
);

-- Sett inn testdata
-- =========================
-- TESTDATA
-- =========================

-- Kunder (5 stk)
INSERT INTO kunde (fornavn, etternavn, epost, tlf_nr)
SELECT
    'Fornavn' || i,
    'Etternavn' || i,
    'kunde' || i || '@mail.no',
    LPAD((10000000 + i)::text, 8, '0')
FROM generate_series(1, 5) AS s(i);


-- Sykkelstasjoner (5 stk)
INSERT INTO sykkel_stasjon (stasjon_posisjon)
SELECT 'Stasjon ' || i
FROM generate_series(1, 5) AS s(i);


-- Låser (100 stk, 20 per stasjon)
CREATE TABLE IF NOT EXISTS lås (
    lås_id SERIAL PRIMARY KEY,
    stasjon_id INTEGER NOT NULL,
    FOREIGN KEY (stasjon_id) REFERENCES sykkel_stasjon(stasjon_id)
);

INSERT INTO lås (stasjon_id)
SELECT ((i - 1) % 5) + 1
FROM generate_series(1, 100) AS s(i);


-- Sykler (100 stk, 20 per stasjon)
INSERT INTO sykkel (stasjon_id, låst, utlevert)
SELECT
    ((i - 1) % 5) + 1,
    TRUE,
    FALSE
FROM generate_series(1, 100) AS s(i);


-- Utleier (50 stk)
INSERT INTO utleie (
    sykkel_id,
    kunde_id,
    utleie_stasjon_id,
    innlevering_stasjon_id,
    leiebeløp,
    utleie_tidspunkt,
    innlevering_tidspunkt
)
SELECT
    (RANDOM() * 99 + 1)::int,
    (RANDOM() * 4 + 1)::int,
    (RANDOM() * 4 + 1)::int,
    (RANDOM() * 4 + 1)::int,
    ROUND((RANDOM() * 100)::numeric, 2),
    NOW() - (RANDOM() * INTERVAL '10 days'),
    NOW()
FROM generate_series(1, 50);

-- DBA setninger (rolle: kunde, bruker: kunde_1)



-- Eventuelt: Opprett indekser for ytelse



-- Vis at initialisering er fullført (kan se i loggen fra "docker-compose log"
SELECT 'Database initialisert!' as status;