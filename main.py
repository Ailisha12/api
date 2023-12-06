import api
import pandas as pd

API = api.DB(host='127.0.0.1', username='postgres', password='Happyenglish1', database='database')

data = {'name': ['Ира', 'Коля', 'Петя', 'Ваня', 'Абрам'], 'age': [17, 20, 17, 22, 14]}
df = pd.DataFrame(data)
API.create_table(df, 'db', 'children')
print(df)

API.delete_from_table('users', 'db', conditions="age = 17")

query = "SELECT * FROM db.users"
result = API.read_sql(query)
print(result)

API.truncate_table('db', 'children')

data = {'name': ['Ира', 'Коля', 'Петя', 'Ваня', 'Абрам'], 'age': [17, 20, 17, 22,12]}
df = pd.DataFrame(data)

API.insert_sql(df, 'db', 'children')

query = "UPDATE db.children SET name ='Максим' WHERE age = 14"
API.execute(query)

query = "SELECT * FROM db.children"
result = API.read_sql(query)
print(result)