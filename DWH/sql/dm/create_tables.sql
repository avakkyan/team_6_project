CREATE TABLE dm.инструменты (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.уровни_знаний_в_отрасли (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.уровни_знаний_в_предметной_области (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.предметная_область (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.отрасли (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.среды_разработки (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.уровень_образования (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.базы_данных (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.category_know (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.уровни_владения_ин (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.сертификаты_пользователей (
    id INT PRIMARY KEY,
   "User ID" INT,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE,
    "Наименование сертификата" text,
    "Организация, выдавшая сертификат" text,
    "Год сертификата" int
);

CREATE TABLE dm.фреймворки (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.языки (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.типы_систем (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.технологии (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.сотрудники_дар (
    id INT PRIMARY KEY,
    "Дата рождения" text,
    активность bool,
    пол VARCHAR(5),
    фамилия VARCHAR(20),
    имя VARCHAR(20),
    "Последняя авторизация" text,
    должность text,
    цфо VARCHAR(10),
    "Дата регистрации" text,
    подразделения text,
    "E-Mail" VARCHAR(50),
    логин VARCHAR(50),
    компания VARCHAR(50),
    "Город проживания" VARCHAR(50),
    "Дата изменения" text
);

CREATE TABLE dm.языки_программирования (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.платформы (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE
);

CREATE TABLE dm.уровни_знаний (
    id INT PRIMARY KEY,
    название text,
    активность BOOLEAN,
    "Дата изм." DATE,
    n_level int
);

CREATE TABLE dm.period(
    id INT PRIMARY KEY,
    название text,
    начало_периода DATE,
    конец_периода DATE,
    активность BOOLEAN,
    "Дата изм." DATE
);


CREATE TABLE summary_tab (
    id INT PRIMARY KEY,
    record_id INT,
    "User ID" INT,
    date_first DATE,
    date_last DATE,
    category_know_id INT,
    know_id INT,
    level_id INT,
    n_level INT,
    certificate_id INT,
    period_id INT,
    growth INT,
    FOREIGN KEY ("User ID") REFERENCES dm.сотрудники_дар(id),
    FOREIGN KEY (level_id) REFERENCES  dm.уровни_знаний_в_отрасли(id) ON UPDATE CASCADE,
    FOREIGN KEY (level_id) REFERENCES  dm.уровни_знаний_в_предметной_области(id) ON UPDATE CASCADE,
    FOREIGN KEY (level_id) REFERENCES  dm.уровни_знания_ин(id) ON UPDATE CASCADE,
    FOREIGN KEY (level_id) REFERENCES  dm.уровень_образования(id) ON UPDATE CASCADE,
    FOREIGN KEY (level_id) REFERENCES dm.уровень_образования(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.языки_программирования(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.языки(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.предметная_область(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.среды_разработки(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.базы_данных(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.инструменты(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.отрасли(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.платформы(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.технологии(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.типы_систем(id) ON UPDATE CASCADE,
    FOREIGN KEY (know_id) REFERENCES dm.фреймворки(id) ON UPDATE CASCADE,
    FOREIGN KEY (category_know_id) REFERENCES dm.category_know(id),
    FOREIGN KEY (certificate_id) REFERENCES dm.сертификаты_пользователей(id),
    FOREIGN KEY (period_id) REFERENCES dm.period(id)
);
