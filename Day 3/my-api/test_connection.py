import pyodbc

try:
    conn = pyodbc.connect(
        r"DRIVER={ODBC Driver 17 for SQL Server};SERVER=STUDENT11,1433;DATABASE=MIS;Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM new_books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
except Exception as e:
    print("Connection failed:", e)