from sqlalchemy import text
from src.utils.db_utils import engine

async def test_db_connection():
    print("Attempting to connect to the database...")
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
    except Exception as e:
        print("❌ Database connection failed. Error details:")
        print(e)