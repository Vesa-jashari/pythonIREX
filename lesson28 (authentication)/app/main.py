from typing import List,Optional
import sqlite3
from models import Item
from database import get_db_connection

def create_item(item: Item)->Item:
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("Insert into items (name, description0) values (?,?)", (item.name,item.description))
    conn.commit()
    item.id=cursor.lastrowid
    conn.close()
    return item

def get_items()->List[Item]:
    conn=get_db_connection()
    items=conn.execute("Select * from items").fetchall()
    conn.close()
    return [Item(**dict(item)) for item in items]


def get_item(item_id: int)->Optional[Item]:
    conn=get_db_connection()
    item=conn.execute("Select * from items where id=?", (item_id)).fetchone()
    conn.close()
    if item is None:
        return None
    return Item(**dict(item))