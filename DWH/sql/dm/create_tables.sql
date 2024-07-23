CREATE TABLE dm_avakyan.category_know (
    id INT PRIMARY KEY,
    название VARCHAR(50),
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm_avakyan.сотрудники_дар (
    id INT PRIMARY KEY,
    активность bool,
    пол VARCHAR(5),
    фамилия VARCHAR(20),
    имя VARCHAR(20),
    "Последняя авторизация" date,
    должность VARCHAR(50),
    цфо VARCHAR(10),
    подразделения VARCHAR(50),
    "E-Mail" VARCHAR(50),
    логин VARCHAR(50),
    компания VARCHAR(50),
    "Город проживания" VARCHAR(50)
);

CREATE TABLE dm_avakyan.period(
    id INT PRIMARY KEY,
    название VARCHAR(50),
    начало_периода DATE,
    конец_периода DATE,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm_avakyan.levels AS(
    SELECT id, название, активность, "Дата изм." FROM dds.уровни_знаний
        UNION ALL
        SELECT id, название, активность, "Дата изм." FROM dds.уровни_знаний_в_отрасли
        UNION ALL
        SELECT id, название, активность, "Дата изм." FROM dds.уровни_знаний_в_предметной_област
        UNION ALL
        SELECT id, название, активность, "Дата изм." FROM dds.уровни_владения_ин
        UNION ALL
        SELECT id, название, активность, "Дата изм." FROM dds.уровень_образования);

ALTER TABLE dm_avakyan.levels ADD COLUMN n_level INTEGER;

ALTER TABLE dm_avakyan.levels
ADD PRIMARY KEY (id);

UPDATE dm_avakyan.levels SET n_level = 2 WHERE название = 'Novice';
UPDATE dm_avakyan.levels SET n_level = 3 WHERE название = 'Junior';
UPDATE dm_avakyan.levels SET n_level = 4 WHERE название = 'Middle';
UPDATE dm_avakyan.levels SET n_level = 5 WHERE название = 'Senior';
UPDATE dm_avakyan.levels SET n_level = 6 WHERE название = 'Expert';
UPDATE dm_avakyan.levels SET n_level = 1 WHERE название = 'Использовал на проекте';

UPDATE dm_avakyan.levels SET n_level = NULL WHERE n_level IS NULL;

CREATE TABLE dm_avakyan.knowledge AS
SELECT id, название, активность, "Дата изм." FROM dds.языки_программирования
    UNION ALL
    SELECT id, название, активность, "Дата изм." FROM dds.языки
    UNION ALL
    SELECT id, название, активность, "Дата изм." FROM dds.предметная_область
    UNION ALL
    SELECT id, название, активность, "Дата изм." FROM dds.среды_разработки
    UNION ALL
    SELECT id, название, активность, "Дата изм." FROM dds.базы_данных
    UNION ALL
    SELECT id, название, активность, "Дата изм." FROM dds.инструменты
    UNION ALL
    SELECT id, название, активность, "Дата изм." FROM dds.отрасли
    UNION ALL
    SELECT id, название, активность, "Дата изм." FROM dds.платформы
    UNION ALL
    SELECT id, название, активность, "Дата изм." FROM dds.технологии
    UNION ALL
    SELECT id, название, активность, "Дата изм." FROM dds.типы_систем
    UNION ALL
    SELECT id, название, активность, "Дата изм." FROM dds.фреймворки;

ALTER TABLE dm_avakyan.knowledge
ADD PRIMARY KEY (id);

CREATE TABLE dm_avakyan.summary_tab (
    id INT PRIMARY KEY,
    "User ID" INT,
    date_first DATE,
    date_last DATE,
    category_know_id INT,
    know_id INT,
    level_id INT,
    n_level INT,
    period_id INT,
    growth INT,
    FOREIGN KEY ("User ID") REFERENCES dm_avakyan.сотрудники_дар(id),
    FOREIGN KEY (level_id) REFERENCES  dm_avakyan.levels(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm_avakyan.knowledge(id) ON UPDATE CASCADE,
    FOREIGN KEY (category_know_id) REFERENCES dm_avakyan.category_know(id),
    FOREIGN KEY (period_id) REFERENCES dm_avakyan.period(id)
);
