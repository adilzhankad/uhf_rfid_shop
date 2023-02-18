import sqlite3

db = sqlite3.connect("basetest.db")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    Name TEXT,
    Email TEXT,
    Password TEXT
) """)

db.commit()

for value in sql.execute("SELECT * FROM users"):
    print(value)

def save_n_e_p(name,email,password):
    name_arr=[]

    sql.execute(f"INSERT INTO users VALUES (?, ?, ?)",(name, email, password))
    db.commit()

    for value in sql.execute("SELECT * FROM users"):
        print(value)
save_n_e_p("adilzhan", "akomen1000@gmail.com", "krisa")


    