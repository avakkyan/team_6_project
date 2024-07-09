DROP TABLE IF EXISTS dds.базы_данных;
CREATE TABLE dds.базы_данных (
	id SERIAL PRIMARY KEY,
	название VARCHAR (50),
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.сотрудники_дар;
CREATE TABLE dds.сотрудники_дар (
	id SERIAL PRIMARY KEY,
	"Дата рождения" DATE,
	активность BOOLEAN,
	пол VARCHAR (50),
	фамилия VARCHAR (100),
	имя VARCHAR (100),
	"Последняя авторизация" TIMESTAMP,
	должность TEXT,
	цфо VARCHAR (100),
	"Дата регистрации" DATE,
	"Дата изменения" DATE,
	подразделения TEXT,
	"E-Mail" VARCHAR (250),
	логин VARCHAR (250),
	компания VARCHAR (250),
	"Город проживания" VARCHAR (250)
);

DROP TABLE IF EXISTS dds.уровни_знаний;
CREATE TABLE dds.уровни_знаний (
	id SERIAL PRIMARY KEY,
	название VARCHAR (100),
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.базы_данных_и_уровень_знаний_сотрудников;
CREATE TABLE dds.базы_данных_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP,
	"Базы данных id" INT,
	Дата DATE,
	"Уровень знаний id" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Базы данных id") REFERENCES dds.базы_данных (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний id") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.инструменты;
CREATE TABLE dds.инструменты (
	id SERIAL PRIMARY KEY,
	название TEXT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.инструменты_и_уровень_знаний_сотрудников;
CREATE TABLE dds.инструменты_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"инструменты id" INT,
	"Уровень знаний id" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("инструменты id") REFERENCES dds.инструменты (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний id") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.платформы;
CREATE TABLE dds.платформы (
	id SERIAL PRIMARY KEY,
	название TEXT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.платформы_и_уровень_знаний_сотрудников;
CREATE TABLE dds.платформы_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"платформы id" INT,
	"Уровень знаний id" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("платформы id") REFERENCES dds.платформы (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний id") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.среды_разработки;
CREATE TABLE dds.среды_разработки (
	id SERIAL PRIMARY KEY,
	название TEXT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.среды_разработки_и_уровень_знаний_сотрудников;
CREATE TABLE dds.среды_разработки_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"Среды разработки id" INT,
	"Уровень знаний id" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Среды разработки id") REFERENCES dds.среды_разработки (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний id") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL
);

DROP TABLE IF EXISTS dds.технологии;
CREATE TABLE dds.технологии (
	id SERIAL PRIMARY KEY,
	название TEXT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.технологии_и_уровень_знаний_сотрудников; 
CREATE TABLE dds.технологии_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"технологии id" INT,
	"Уровень знаний id" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("технологии id") REFERENCES dds.технологии (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний id") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL	
);

DROP TABLE IF EXISTS dds.типы_систем;
CREATE TABLE dds.типы_систем (
	id SERIAL PRIMARY KEY,
	название TEXT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.типы_систем_и_уровень_знаний_сотрудников;
CREATE TABLE dds.типы_систем_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"Типы_систем id" INT,
	"Уровень знаний id" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Типы_систем id") REFERENCES dds.типы_систем (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний id") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL	
);

DROP TABLE IF EXISTS dds.уровни_владения_ин;
CREATE TABLE dds.уровни_владения_ин (
	id SERIAL PRIMARY KEY,
	название TEXT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.фреймворки;
CREATE TABLE dds.фреймворки (
	id SERIAL PRIMARY KEY,
	название TEXT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.фреймворки_и_уровень_знаний_сотрудников;
CREATE TABLE dds.фреймворки_и_уровень_знаний_сотрудников (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"фреймворки id" INT,
	"Уровень знаний id" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("фреймворки id") REFERENCES dds.фреймворки (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний id") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL	
);

DROP TABLE IF EXISTS dds.языки;
CREATE TABLE dds.языки (
	id SERIAL PRIMARY KEY,
	название VARCHAR (100),
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.языки_пользователей;
CREATE TABLE dds.языки_пользователей (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP,
	"язык id" INT,
	"Уровень знаний ин. языка id" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("язык id") REFERENCES dds.языки (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний ин. языка id") REFERENCES dds.уровни_владения_ин (id) ON UPDATE CASCADE ON DELETE SET NULL	
);

DROP TABLE IF EXISTS dds.языки_программирования;
CREATE TABLE dds.языки_программирования (
	id SERIAL PRIMARY KEY,
	название TEXT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP
);

DROP TABLE IF EXISTS dds.языки_программирования_и_уровень_знаний;
CREATE TABLE dds.языки_программирования_и_уровень_знаний (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Сорт." INT,
	"Дата изм." TIMESTAMP,
	дата DATE,
	"Языки программирования id" INT,
	"Уровень знаний id" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Языки программирования id") REFERENCES dds.языки_программирования (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Уровень знаний id") REFERENCES dds.уровни_знаний (id) ON UPDATE CASCADE ON DELETE SET NULL	
);

DROP TABLE IF EXISTS dds.резюмедар;
CREATE TABLE dds.резюмедар (
	id SERIAL PRIMARY KEY,
	user_id INT,
	активность BOOLEAN,
	"Языки id" INT,
	"Базы данных id" INT,
	"Инструменты id" INT,
	"Платформы id" INT,
	"Среды разработки id" INT,
	"Типы систем id" INT,
	"Фреймворки id" INT,
	"Языки программирования id" INT,
	"Технологии id" INT,
	FOREIGN KEY (user_id) REFERENCES dds.сотрудники_дар (id) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY ("Языки программирования id") REFERENCES dds.языки_программирования (id) ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY ("Языки id") REFERENCES dds.языки (id) ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY ("Базы данных id") REFERENCES dds.базы_данных (id) ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY ("Инструменты id") REFERENCES dds.инструменты (id) ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY ("Платформы id") REFERENCES dds.платформы (id) ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY ("Среды разработки id") REFERENCES dds.среды_разработки (id) ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY ("Типы систем id") REFERENCES dds.типы_систем (id) ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY ("Фреймворки id") REFERENCES dds.фреймворки (id) ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY ("Технологии id") REFERENCES dds.технологии (id) ON UPDATE CASCADE ON DELETE SET NULL
);
