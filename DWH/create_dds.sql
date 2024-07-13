DROP TABLE IF EXISTS dds.базы_данных;
CREATE TABLE dds.базы_данных (
	id SERIAL PRIMARY KEY
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
);

DROP TABLE IF EXISTS dds.сотрудники_дар;
CREATE TABLE dds.сотрудники_дар (
	id SERIAL PRIMARY KEY,
	"Дата рождения" DATE,
	активность BOOLEAN,
	пол VARCHAR (5),
	фамилия VARCHAR (20),
	имя VARCHAR (20),
	"Последняя авторизация" TIMESTAMP,
	должность VARCHAR (50),
	цфо VARCHAR (10),
	"Дата регистрации" DATE,
	"Дата изменения" DATE,
	подразделения TEXT,
	"E-Mail" VARCHAR (50),
	логин VARCHAR (50),
	компания VARCHAR (50),
	"Город проживания" VARCHAR (50)
);

DROP TABLE IF EXISTS dds.уровни_знаний;
CREATE TABLE dds.уровни_знаний (
	id SERIAL PRIMARY KEY,
	название VARCHAR (20),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.базы_данных_и_уровень_знаний_сотрудников;
CREATE TABLE dds.базы_данных_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	"Базы данных" INT,
	дата DATE,
	"Уровень знаний" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Базы данных") REFERENCES dds.базы_данных (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.базы_данных_и_уровень_битые;
CREATE TABLE dds.базы_данных_и_уровень_битые (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	"Базы данных" INT,
	дата DATE,
	"Уровень знаний" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Базы данных") REFERENCES dds.базы_данных (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.инструменты;
CREATE TABLE dds.инструменты (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.инструменты_и_уровень_знаний_сотрудников;
CREATE TABLE dds.инструменты_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"инструменты" INT,
	"Уровень знаний" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("инструменты") REFERENCES dds.инструменты (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.платформы;
CREATE TABLE dds.платформы (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.платформы_и_уровень_знаний_сотрудников;
CREATE TABLE dds.платформы_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"платформы" INT,
	"Уровень знаний" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("платформы") REFERENCES dds.платформы (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.среды_разработки;
CREATE TABLE dds.среды_разработки (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.среды_разработки_и_уровень_знаний_сотрудников;
CREATE TABLE dds.среды_разработки_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"Среды разработки" INT,
	"Уровень знаний" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Среды разработки") REFERENCES dds.среды_разработки (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.технологии;
CREATE TABLE dds.технологии (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.технологии_и_уровень_знаний_сотрудников; 
CREATE TABLE dds.технологии_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"технологии" INT,
	"Уровень знаний" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("технологии") REFERENCES dds.технологии (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL	
);

DROP TABLE IF EXISTS dds.типы_систем;
CREATE TABLE dds.типы_систем (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.типы_систем_и_уровень_знаний_сотрудников;
CREATE TABLE dds.типы_систем_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"Типы_систем" INT,
	"Уровень знаний" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Типы_систем") REFERENCES dds.типы_систем (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL	
);

DROP TABLE IF EXISTS dds.уровни_владения_ин;
CREATE TABLE dds.уровни_владения_ин (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.фреймворки;
CREATE TABLE dds.фреймворки (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.фреймворки_и_уровень_знаний_сотрудников;
CREATE TABLE dds.фреймворки_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"фреймворки" INT,
	"Уровень знаний" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("фреймворки") REFERENCES dds.фреймворки (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL	
);

DROP TABLE IF EXISTS dds.языки;
CREATE TABLE dds.языки (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.языки_пользователей;
CREATE TABLE dds.языки_пользователей (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	"язык" INT,
	"Уровень знаний ин. языка" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("язык") REFERENCES dds.языки (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний ин. языка") REFERENCES dds.уровни_владения_ин (id) ON UPDATE CASCADE ON DELETE SET NULL	
);

DROP TABLE IF EXISTS dds.языки_программирования;
CREATE TABLE dds.языки_программирования (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.языки_программирования_и_уровень_знаний;
CREATE TABLE dds.языки_программирования_и_уровень_знаний (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"Языки программирования" INT,
	"Уровень знаний" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Языки программирования") REFERENCES dds.языки_программирования (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL	
);

DROP TABLE IF EXISTS dds.уровень_образования;
CREATE TABLE dds.уровень_образования (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.образование_пользователей;
CREATE TABLE dds.образование_пользователей (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	"Уровень образования" INT,
	"Название учебного заведения" VARCHAR (100),
	"Фиктивное название" VARCHAR (30),
	"Год окончания" INT
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень образования") REFERENCES dds.уровень_образования (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.отрасли;
CREATE TABLE dds.отрасли (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.уровни_знаний_в_отрасли;
CREATE TABLE dds.уровни_знаний_в_отрасли (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.опыт_сотрудника_в_отраслях;
CREATE TABLE dds.опыт_сотрудника_в_областях (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"отрасли" INT,
	"Уровень знаний в отрасли" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("отрасли") REFERENCES dds.отрасли (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний в отрасли") REFERENCES dds.уровни_знаний_в_отрасли (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.предметная_область;
CREATE TABLE dds.предметная_область (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.уровни_знаний_в_предметной_област;
CREATE TABLE dds.уровни_знаний_в_отрасли (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.опыт_сотрудника_в_предметных_обла;
CREATE TABLE dds.опыт_сотрудника_в_предметных_обла (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"Предметные области" INT,
	"Уровень знаний в предметной облас" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Предметные области") REFERENCES dds.предметная_область (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний в предметной облас") REFERENCES dds.уровни_знаний_в_предметной_област (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.сертификаты_пользователей;
CREATE TABLE dds.сертификаты_пользователей (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Дата изм." TIMESTAMP,
	"Год сертификата" INT,
	"Наименование сертификата" VARCHAR (100),
	"Организация, выдавшая сертификат" VARCHAR (50),
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE
);
