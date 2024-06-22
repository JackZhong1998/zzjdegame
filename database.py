import sqlite3

def save_game_state(game_state):
    conn = sqlite3.connect('game_state.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS game_state (id INTEGER PRIMARY KEY, state TEXT)''')
    cursor.execute('''INSERT INTO game_state (state) VALUES (?)''', (str(game_state),))
    conn.commit()
    conn.close()

def load_game_state():
    conn = sqlite3.connect('game_state.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT state FROM game_state ORDER BY id DESC LIMIT 1''')
    game_state = cursor.fetchone()
    conn.close()
    return eval(game_state[0]) if game_state else {}