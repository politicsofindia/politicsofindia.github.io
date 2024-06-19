import aiosqlite

async def init_db():
    async with aiosqlite.connect('users.db') as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        await db.commit()

async def add_user(email, password):
    async with aiosqlite.connect('users.db') as db:
        await db.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
        await db.commit()
