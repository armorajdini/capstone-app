import sqlite3
import os

db_files = ["3landspiel.db", "3landspiel_v2.db"]

for db_file in db_files:
    if os.path.exists(db_file):
        print(f"--- Checking database: {db_file} ---")
        try:
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            
            # Tabellen auflisten
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [t[0] for t in cursor.fetchall()]
            print(f"Tables: {', '.join(tables)}")
            
            if 'spiellinien' in tables:
                query = """
                SELECT s.id, t.titel, u.name 
                FROM spiellinien s 
                LEFT JOIN themen t ON s.thema_id = t.id 
                LEFT JOIN users u ON s.user_id = u.id 
                ORDER BY s.id DESC LIMIT 5;
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        print(f"ID: {row[0]} | Thema: {row[1]} | User: {row[2]}")
                else:
                    print("No entries found in 'spiellinien'.")
            
            conn.close()
        except Exception as e:
            print(f"Error reading {db_file}: {e}")
    else:
        print(f"Database file not found: {db_file}")
