from hero import Hero 
from enemy import Enemy

objHero = Hero()
objEnemy = Enemy()

def menu_hero () :
    while True : 
        print('Menu Hero :')
        print('1. Lihat Data')
        print('2. Tambah data')
        print('3. Ubah data')
        print('4. Hapus data') 
        print('5. Kembali')
        pilihan = int(input('Pilih menu : '))

        if (pilihan not in [1,2,3,4,5]) :
            print('input tidak valid')
            continue

        if (pilihan == 1) :
            objHero.ambil_data()
        elif (pilihan == 2) :
            objHero.tambah_data()
        elif (pilihan == 3) :
            objHero.ubah_data()
        elif (pilihan == 4) :
            objHero.hapus_data()
        else :
            break

def menu_enemy () :
    while True :
        print('Menu Enemy : ')
        print('1. Lihat Data')
        print('2. Tambah Data')
        print('3. Ubah Data')
        print('4. Hapus Data')
        print('5. Kembali')

        pilihan = int(input('Pilih menu = '))
        
        if (pilihan not in [1,2,3,4,5]) :
            print('input tidak sesuai')
            continue

        if (pilihan == 1) :
            objEnemy.ambil_data()
        elif (pilihan == 2) :
            objEnemy.tambah_data()
        elif (pilihan == 3) :
            objEnemy.ubah_data()
        elif (pilihan == 4) :
            objEnemy.hapus_data()
        else : 
            break

def menu_play () :
    while True :
        print('MENU : ')
        print('1. Hero Attack')
        print('2. Hero Regen')
        print('3. Enemy Attack')
        print('4. Tambah damage')
        print('5. Kembali')

        choice = int(input('Masukan pilihan = '))

        if (choice not in [1,2,3,4,5]) :
            print('input tidak sesuai')
            continue 
        elif (choice == 1) :

            heroPilih = int(input('Masukan id hero = '))
            enemyPilih = int(input('Masukan id enemy = '))

            objHero.hero_attack(heroPilih,enemyPilih)

        elif (choice == 2) :
            heroPilih = int(input('Masukan id hero = '))
            objHero.hero_regen(heroPilih)
        elif (choice == 3) :
            heroPilih = int(input('Masukan id hero = '))
            enemyPilih = int(input('Masukan id enemy = '))

            objEnemy.enemy_attack(enemyPilih,heroPilih)
        elif (choice == 4) :
            print('1. Tambah damage hero ')
            print('2. Tambah damage enemy')

            damagePilih = int(input('Masukan pilihan = '))

            if (damagePilih not in [1,2]) :
                print('nomor invalid ')
                continue
            elif (damagePilih == 1) :
                heroPilih = int(input('Masukan id hero = '))
                objHero.tambah_damage(heroPilih)
            else : 
                enemyPilih = int(input('Masukan id enemy = '))
                objEnemy.tambah_damage(enemyPilih)
        elif (choice == 5) :
            break 


def main_menu () :
    while True :
        print('MENU : ')
        print('1. Menu Hero')
        print('2. Menu Enemy')
        print('3. Play Game')
        print('4. Keluar')

        pilihan = int(input('Masukan menu = '))

        if (pilihan not in [1,2,3,4]) :
            print('input tidak sesuai ')
            continue 
        elif (pilihan == 1) :
            menu_hero()
        elif (pilihan == 2) :
            menu_enemy()
        elif (pilihan == 3) :
            menu_play()
        else :
            break
main_menu()