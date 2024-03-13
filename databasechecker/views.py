from connections import cursor

request = """ SELECT body FROM backend """
cursor.execute(request)
for i in cursor.fetchall():
    print(i)
