import psycopg2

def conectar():
    return psycopg2.connect(
        host="db.zqxivchoqdcolklahdzu.supabase.co",
        database="postgres",
        user="postgres",
        password="Arostone15030",
        port="5432"
    )