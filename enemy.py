from database import cursor, db
class Enemy :
    def ambil_data (self) :
        cursor.execute("SELECT * FROM enemy")
        data = cursor.fetchall()

        for x in data :
            print(x)

    def tambah_data (self) :
        nama = input('Masukan nama = ')
        tipe = input('Masukan tipe = ')
        health = int(input('Masukan health = '))
        damage = int(input('Masukan damage = '))
        
        query = f"INSERT INTO enemy (name, type, health, damage) VALUES ('{nama}','{tipe}','{health}','{damage}')"
        cursor.execute(query)
        db.commit()
        print('Berhasil mendaftarkan daftar enemy')

    def ubah_data (self) :
        idInput = int(input("masukan id = "))
        nama = input('Masukan nama = ')
        tipe = input('Masukan tipe = ')
        health = int(input('Masukan health = '))
        damage = int(input('Masukan damage = '))

        query = "UPDATE enemy SET name=%s, type= %s, health=%s, damage=%s WHERE ID = %s"
        values = (nama, tipe, health, damage, idInput)

        cursor.execute(query, values)
        db.commit()
        print(f"Berhasil mengubah data enemy dengan id {idInput} menjadi {nama}, {tipe}, {health}, {damage}")

    def hapus_data (self) :
         idInput = int(input("masukan id = "))
         query = f"DELETE FROM enemy WHERE id='{idInput}'"
         cursor.execute(query,)
         db.commit()
         print(f"Berhasil menghapus enemy dengan id {idInput}")

    def enemy_attack (self, idenemy, idhero) :
        # damage enemy
        query = f"SELECT damage from Enemy WHERE id = '{idenemy}'"
        cursor.execute(query)
        damageenemy = cursor.fetchone()[0]

        # health enemy 
        query2 = f"SELECT health FROM Hero WHERE id = '{idhero}'"
        cursor.execute(query2)
        heroHealth = cursor.fetchone()[0]

        # update health 
        heroHealth-= damageenemy
        query3 = "UPDATE Hero SET health = %s WHERE id = %s"
        values = (heroHealth,idhero)
        cursor.execute(query3, values)
        db.commit()
        
        print('Enemy berhasil menyerang hero')

    def tambah_damage(self, idEnemy) :
        query1 = f"SELECT damage from Enemy WHERE id = '{idEnemy}'"
        cursor.execute(query1)
        damageEnemy = cursor.fetchone()[0]

        damageEnemy += 250
        query2 = "UPDATE Enemy SET damage = %s WHERE id = %s"
        values  = (damageEnemy,idEnemy)
        cursor.execute(query2,values)
        db.commit()

        print('berhasil menambah damage enemy')
