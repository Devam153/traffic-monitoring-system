    def mysql_connector():
        mydb = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )        
        mycursor = mydb.cursor()

        d = 'image' + str(choice)
        z = str(d)
        x = vehicle
        q = maxY
        a = minY
        w = diff
        y = times

        try: 
            query = """INSERT INTO traffic VALUES (%s,%s,%s,%s,%s,%s)"""
            tup1 = (z, x, q, a, w, y)
            mycursor.execute(query, tup1)
            mydb.commit()
            msg = "Record added to MySQL table 'traffic'."
        except mysql.connector.IntegrityError:
            msg = "Above record already present in MySQL table 'traffic'."

        # ✅ Common code outside try/except
        query2 = 'SELECT * FROM traffic WHERE Image_No = %s'
        tup2 = (z,)
        mycursor.execute(query2, tup2)
        myrecords = mycursor.fetchall()

        l = [['Image_No','No_of_Vehciles','MaxY','MinY','Difference','Time(sec)']]
        for rec in myrecords:
            l.append(list(rec))

        print(tabulate(l))
        print(msg)


    mysql_connector()