# Connecting to a Database
def connect_to_database(database_path):
    import sqlite3

    connection = sqlite3.connect(database_path)
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


# Data Backup and Restore
def backup_database(database_path, backup_path):
    import shutil

    shutil.copyfile(database_path, backup_path)


def restore_database(database_path, backup_path):
    import shutil

    shutil.copyfile(backup_path, database_path)
