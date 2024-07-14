import pandas as pd
from sqlalchemy import create_engine
import psycopg2 as ps
from datetime import date

connection = ps.connect(
     host='10.82.0.4',
     user='etl_user_6',
     password='+UAu{5*-',
     database='etl_db_6'
)

# Процедуры и функции ####################################################
def activnost_to_bool(data, num):
     for i in range(len(data)):
          data[i]=list(data[i])
          if data[i][num]=='Да':
               data[i][num]=True
          else:
               data[i][num] = False

def propuski(data, num):
     for i in range(len(data)):
          data[i]=list(data[i])
          if data[i][num]=='' or data[i][num]=='-':
               data[i][num]="Не указано"

def propuski_data(data, num):
     for i in range(len(data)):
          data[i]=list(data[i])
          if data[i][num]=='':
               data[i][num]=date.today()

def text_to_id(data, num):
     for i in range(len(data)):
          data[i]=list(data[i])
          n_id=''
          for j in data[i][num]:
              if j.isdigit():
                n_id+=j
          data[i][num]=int(n_id)

cursor = connection.cursor()

# базы_данных #######################################################
request_to_read_data = '''SELECT id, название, активность, "Дата изм."  FROM ods.базы_данных'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
data[0][3]='2020-10-21 13:17:53'

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.базы_данных (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);
     '''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# сотрудники_дар ###################################################
request_to_read_data = '''SELECT * FROM ods.сотрудники_дар'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
propuski(data, 7)
propuski(data, 8)
propuski_data(data, 6)
propuski_data(data, 1)
propuski_data(data, 9)
propuski_data(data, 10)


for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.сотрудники_дар (id, "Дата рождения", активность, пол, фамилия, имя, 
     "Последняя авторизация", должность, цфо, "Дата регистрации", "Дата изменения", подразделения, "E-Mail", 
     логин, компания, "Город проживания") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
     '''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# уровни_знаний ############################################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.уровни_знаний'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.уровни_знаний (id, название, активность, "Дата изм.") VALUES 
     (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# базы_данных_и_уровень_знаний_сотру #####################################
request_to_read_data = '''SELECT id, название, активность, "Дата изм.", "Базы данных", дата, "Уровень знаний"
 FROM ods.базы_данных_и_уровень_знаний_сотру
 WHERE "Уровень знаний" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()


# bitiye_danniye_bazi=[]
# for i, el in enumerate(data):
#     if data[i][6]=='':
#           data.remove(el)
#           bitiye_danniye_bazi.append(el)


# print(len(data))
# print(len(bitiye_danniye_bazi))

activnost_to_bool(data, 2)
text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 6)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.базы_данных_и_уровень_знаний_сотру (id, user_id, активность, "Дата изм.",
     "Базы данных", дата, "Уровень знаний") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()


# for i in bitiye_danniye_bazi:
#      request_to_insert_data = '''
#      INSERT INTO dds_test_pozdnyakova.базы_данных_и_уровень_битые (id, user_id, активность, "Дата изм.",
#      "Базы данных", дата, "Уровень знаний") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
#      cursor.execute(request_to_insert_data, i)
#      connection.commit()

# Инструменты ################################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.инструменты'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.инструменты (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# инструменты_и_уровень_знаний_сотр #############
request_to_read_data = '''SELECT id, название, активность, "Дата изм.", "инструменты", дата, "Уровень знаний"
 FROM ods.инструменты_и_уровень_знаний_сотр
 WHERE "Уровень знаний" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 6)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.инструменты_и_уровень_знаний_сотр (id, user_id, активность, "Дата изм.",
     "Базы данных", дата, "Уровень знаний") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()

# Платформы #################################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.платформы'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.платформы (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# платформы_и_уровень_знаний_сотруд #########################
request_to_read_data = '''SELECT id, "User ID", активность, "Дата изм.", "платформы", дата, "Уровень знаний"
 FROM ods.платформы_и_уровень_знаний_сотруд
 WHERE "Уровень знаний" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
#text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 6)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.платформы_и_уровень_знаний_сотруд (id, user_id, активность, "Дата изм.",
     "платформы", дата, "Уровень знаний") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()

# Среды_разработки ##########################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.среды_разработки'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.среды_разработки (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# среды_разработки_и_уровень_знаний_ ##########
request_to_read_data = '''SELECT id, название, активность, "Дата изм.", "Среды разработки", дата, "Уровень знаний"
 FROM ods.среды_разработки_и_уровень_знаний_
 WHERE "Уровень знаний" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 6)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.среды_разработки_и_уровень_знаний_ (id, user_id, активность, "Дата изм.",
     "Среды разработки", дата, "Уровень знаний") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()

# технологии ################################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.технологии'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.технологии (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# технологии_и_уровень_знаний_сотру ###########################
request_to_read_data = '''SELECT id, название, активность, "Дата изм.", "технологии", дата, "Уровень знаний"
 FROM ods.технологии_и_уровень_знаний_сотру
 WHERE "Уровень знаний" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 6)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.технологии_и_уровень_знаний_сотру (id, user_id, активность, "Дата изм.",
     "технологии", дата, "Уровень знаний") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()

# Типы_систем ####################################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.типы_систем'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.типы_систем (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# типы_систем_и_уровень_знаний_сотру##########################
request_to_read_data = '''SELECT id, название, активность, "Дата изм.", "Типы систем", дата, "Уровень знаний"
 FROM ods.типы_систем_и_уровень_знаний_сотру
 WHERE "Уровень знаний" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 6)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.типы_систем_и_уровень_знаний_сотру (id, user_id, активность, "Дата изм.",
     "Типы систем", дата, "Уровень знаний") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()

#уровни_владения_ин ###################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.уровни_владения_ин'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.уровни_владения_ин (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# фреймворки ###################################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.фреймворки'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.фреймворки (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# фреймворки_и_уровень_знаний_сотру #####################
request_to_read_data = '''SELECT id, название, активность, "Дата изм.", "фреймворки", дата, "Уровень знаний"
 FROM ods.фреймворки_и_уровень_знаний_сотру
 WHERE "Уровень знаний" != '' AND фреймворки != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 6)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.фреймворки_и_уровень_знаний_сотру (id, user_id, активность, "Дата изм.",
     "фреймворки", дата, "Уровень знаний") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()


# языки ############################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.языки'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.языки (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# языки_пользователей ################################
request_to_read_data = '''SELECT id, название, активность, "Дата изм.", "язык", "Уровень знаний ин. языка"
 FROM ods.языки_пользователей
 WHERE "Уровень знаний ин. языка" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 5)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.языки_пользователей (id, user_id, активность, "Дата изм.",
     "язык", "Уровень знаний ин. языка") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()

# языки_программирования ########################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.языки_программирования'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.языки (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# языки_программирования_и_уровень ###################
request_to_read_data = '''SELECT id, название, активность, "Дата изм.", "Языки программирования", дата, "Уровень знаний"
 FROM ods.языки_программирования_и_уровень
 WHERE "Уровень знаний" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 6)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.языки_программирования_и_уровень (id, user_id, активность, "Дата изм.",
     "Языки программирования", дата, "Уровень знаний") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()

# уровень_образования #######################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.уровень_образования'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.уровень_образования (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# образование_пользователей #####################
request_to_read_data = '''SELECT id, "User ID", активность, "Дата изм.", "Уровень образование",
"Название учебного заведения", "Фиктивное название", "Год окончания"
 FROM ods.образование_пользователей
 WHERE "Уровень образование" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
#text_to_id(data, 1)
text_to_id(data, 4)

for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.образование_пользователей (id, user_id, активность, "Дата изм.",
     "Уровень образования", "Название учебного заведения", "Фиктивное название", "Год окончания")
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()

# отрасли ######################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.отрасли'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.отрасли (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# уровни_знаний_в_отрасли ######################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.уровни_знаний_в_отрасли'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.уровни_знаний_в_отрасли (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# опыт_сотрудника_в_отраслях #########################
request_to_read_data = '''SELECT id, "User ID", активность, "Дата изм.", "отрасли", дата, "Уровень знаний в отрасли"
 FROM ods.опыт_сотрудника_в_отраслях
 WHERE "Уровень знаний в отрасли" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
#text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 6)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.опыт_сотрудника_в_отраслях (id, user_id, активность, "Дата изм.",
     "отрасли", дата, "Уровень знаний в отрасли") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()


# предметная_область ####################
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.предметная_область'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.предметная_область (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# уровни_знаний_в_предметной_област ###############
request_to_read_data = '''SELECT id, название, активность, "Дата изм." FROM ods.уровни_знаний_в_предметной_област'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.уровни_знаний_в_предметной_област (id, название, активность, "Дата изм.") VALUES (%s, %s, %s, %s);'''
     cursor.execute(request_to_insert_data, i)
     connection.commit()

# опыт_сотрудника_в_предметных_обла ######################
request_to_read_data = '''SELECT id, "User ID", активность, "Дата изм.", "Предментые области", дата, "Уровень знаний в предметной облас"
 FROM ods.опыт_сотрудника_в_предметных_обла
 WHERE "Уровень знаний в предметной облас" != '' '''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
#text_to_id(data, 1)
text_to_id(data, 4)
text_to_id(data, 6)


for i in range(len(data)):
    if data[i][5]=='':
         data[i][5]=data[i][3]

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.опыт_сотрудника_в_предметных_обла (id, user_id, активность, "Дата изм.",
     "Предметные области", дата, "Уровень знаний в предметной облас") VALUES (%s, %s, %s, %s, %s, %s, %s);'''
     try:
          cursor.execute(request_to_insert_data, i)
     except:
          data.remove(i)
     connection.commit()

# сертификаты_пользователей #################
request_to_read_data = '''SELECT id, "User ID", активность, "Дата изм.", "Год сертификата", "Наименование сертификата", 
"Организация, выдавшая сертификат" FROM ods.сертификаты_пользователей'''
cursor.execute(request_to_read_data)
data = cursor.fetchall()

activnost_to_bool(data, 2)
#text_to_id(data, 1)

for i in data:
     request_to_insert_data = '''
     INSERT INTO dds_test_pozdnyakova.сертификаты_пользователей (id, user_id, активность, "Дата изм.", 
     "Год сертификата", "Наименование сертификата", "Организация, выдавшая сертификат") VALUES (%s, %s, %s, %s, %s, %s, %s);'''


cursor.close()
connection.close()

print('Данные импортированы успешно!')