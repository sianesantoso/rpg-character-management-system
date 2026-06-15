from database import cursor, db
class Hero :
    def ambil_data (self) :
        cursor.execute("SELECT * FROM hero")
        data = cursor.fetchall()

        for x in data :
            print(x)

    def tambah_data (self) :
        nama = input('Masukan nama = ')
        tipe = input('Masukan tipe = ')
        health = int(input('Masukan health = '))
        damage = int(input('Masukan damage = '))
        
        query = ("INSERT INTO hero (name, type, health, damage) VALUES (%s, %s, %s, %s)")
        values = (nama, tipe, health, damage )
        cursor.execute(query, values)
        db.commit()
        print('Berhasil mendaftarkan daftar hero')

    def ubah_data (self) :
        idInput = int(input("masukan id = "))
        nama = input('Masukan nama = ')
        tipe = input('Masukan tipe = ')
        health = int(input('Masukan health = '))
        damage = int(input('Masukan damage = '))

        query = "UPDATE hero SET name=%s, type= %s, health=%s, damage=%s WHERE ID = %s"
        values = (nama, tipe, health, damage, idInput)

        cursor.execute(query, values)
        db.commit()
        print(f"Berhasil mengubah data hero dengan id {idInput} menjadi {nama}, {tipe}, {health}, {damage}")

    def hapus_data (self) :
         idInput = int(input("masukan id = "))
         query = "DELETE FROM hero WHERE id=%s"
         values = (idInput,)
         cursor.execute(query, values)
         db.commit()
         print(f"Berhasil menghapus enemy dengan id {idInput}")

    def hero_attack (self, idHero, idEnemy) :
        # damage hero
        query = f"SELECT damage from Hero WHERE id = '{idHero}'"
        cursor.execute(query)
        damageHero = cursor.fetchone()[0]

        # health enemy 
        query2 = f"SELECT health FROM Enemy WHERE id = '{idEnemy}'"
        cursor.execute(query2)
        enemyHealth = cursor.fetchone()[0]

        # update health 
        enemyHealth-= damageHero
        query3 = "UPDATE Enemy SET health = %s WHERE id = %s"
        values = (enemyHealth, idEnemy)
        cursor.execute(query3, values)
        db.commit()
        
        print('Hero berhasil menyerang enemy')

    def hero_regen (self, idHero) :
        query1 = f"SELECT health from Hero WHERE id = '{idHero}'"
        cursor.execute(query1)
        hpHero = cursor.fetchone()[0]

        query2 = "UPDATE Hero SET health = %s WHERE id = %s"
        values = (hpHero, idHero)
        cursor.execute(query2,values)
        db.commit()

        print('hero berhasil regen')

    def tambah_damage(self, idHero) :
        query1 = f"SELECT damage from Hero WHERE id = '{idHero}'"
        cursor.execute(query1)
        damageHero = cursor.fetchone()[0]

        damageHero += 250
        query2 = "UPDATE Hero SET damage = %s WHERE id = %s"
        values  = (damageHero,idHero)
        cursor.execute(query2,values)
        db.commit()

        print('berhasil menambah damage hero')