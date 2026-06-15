# RPG Character Management System 🛠️

A console-based RPG management system built with Python and MySQL. This project allows users to manage heroes and enemies, perform CRUD operations, and simulate battles using OOP principles.

## Features ⭐

* Hero Management (Create, Read, Update, Delete)
* Enemy Management (Create, Read, Update, Delete)
* Hero Attack System
* Enemy Attack System
* Hero Regeneration
* Damage Upgrade System
* MySQL Database Integration
* Object-Oriented Programming (OOP)

## Technologies Used 💻

* Python
* MySQL
* mysql-connector-python

## Database Schema

### Hero Table

| Column | Type         |
| ------ | ------------ |
| id     | INT          |
| name   | VARCHAR(255) |
| type   | VARCHAR(255) |
| health | INT          |
| damage | INT          |

### Enemy Table

| Column | Type         |
| ------ | ------------ |
| id     | INT          |
| name   | VARCHAR(255) |
| type   | VARCHAR(255) |
| health | INT          |
| damage | INT          |

## Installation

```bash
pip install mysql-connector-python
```

Create a MySQL database:

```sql
CREATE DATABASE game_db;
```
Verify Database Connection

```bash
python database.py
```

Run the Application:
```bash
python menu.py
```

## Project Structure

```text
RPG-Character-Management-System
├── screenshots/
│   ├── adddamage.png
│   ├── addhero.png
│   ├── addmenuenemy.png
│   ├── backfrom_menuenemy.png
│   ├── backfrom_menuhero.png
│   ├── changeenemy.png
│   ├── changehero.png
│   ├── connectdb.png
│   ├── deleteenemy.png
│   ├── enemyattack.png
│   ├── exit.png
│   ├── heroattack.png
│   ├── heroregen.png
│   ├── mainmenu.png
│   ├── menuenemy.png
│   ├── menuhero.png
│   └── playmenu.png
├── database.py
├── hero.py
├── enemy.py
└── menu.py
```

## APP Preview

### Main Menu
![Main Menu](screenshots/mainmenu.png)

### Hero Management
![Hero Management Menu](screenshots/menuhero.png)
![Hero Management Look](screenshots/lookhero.png)
![Hero Management Add](screenshots/addhero.png)
![Hero Management Change](screenshots/changehero.png)
![Hero Management Delete](screenshots/deletehero.png)
![Hero Management Back](screenshots/backfrom_menuhero.png)

### Enemy Management
![Hero Management Menu](screenshots/menuenemy.png)
![Hero Management Look](screenshots/lookenemy.png)
![Hero Management Add](screenshots/addenemy.png)
![Hero Management Change](screenshots/changeenemy.png)
![Hero Management Delete](screenshots/deleteenemy.png)
![Hero Management Back](screenshots/backfrom_menuenemy.png)

### Battle System
![Battle System Menu](screenshots/playmenu.png)
![Battle System Hero Attack](screenshots/heroattack.png)
![Battle System Hero Regen](screenshots/heroregen.png)
![Battle System Enemy Attack](screenshots/enemyattack.png)
![Battle System Add Damage](screenshots/adddamage.png)
![Battle System Exit](screenshots/exit.png)


