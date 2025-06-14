import sqlite3

class Database:
    def __init__(self, db_path='trainer_data.db'):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS trainers (
                discord_id INTEGER PRIMARY KEY,
                trainer_code TEXT NOT NULL,
                username TEXT NOT NULL,
                team TEXT NOT NULL,
                timezone TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_or_update_trainer(self, discord_id, trainer_code, username, team, timezone):
        self.c.execute('''
            INSERT INTO trainers(discord_id, trainer_code, username, team, timezone)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(discord_id) DO UPDATE SET
                trainer_code=excluded.trainer_code,
                username=excluded.username,
                team=excluded.team,
                timezone=excluded.timezone
        ''', (discord_id, trainer_code, username, team, timezone))
        self.conn.commit()

    def get_trainer(self, discord_id):
        self.c.execute('SELECT * FROM trainers WHERE discord_id = ?', (discord_id,))
        return self.c.fetchone()

    def close(self):
        self.conn.close()
