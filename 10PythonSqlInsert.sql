import sqlite3

def insert_student(name: str, grade: float) -> None:
    conn = sqlite3.connect('my.db')
    cursor = conn.cursor()
    sql = ''' INSERT INTO students(name, grade)
              VALUES(?,?) '''
    cursor.execute(sql, (name, grade))
    conn.commit()
    conn.close()