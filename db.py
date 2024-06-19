import aiosqlite

DB_NAME = 'users.db'

async def init_db():
    connection = await aiosqlite.connect(DB_NAME)
    cursor = await connection.cursor()

    await cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            leader_name TEXT NOT NULL
        )
    ''')

    await connection.commit()
    await cursor.close()
    await connection.close()

async def add_user(email, password, leader_name):
    async with aiosqlite.connect(DB_NAME) as connection:
        cursor = await connection.cursor()
        await cursor.execute('INSERT INTO users (email, password, leader_name) VALUES (?, ?, ?)', (email, password, leader_name))
        await connection.commit()
        await cursor.close()
