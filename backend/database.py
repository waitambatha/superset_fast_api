from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Configure SQLite and PostgreSQL engines
SQLITE_URL = "sqlite+aiosqlite:///./medicines.db"
POSTGRES_URL = "postgresql+asyncpg://postgres:password@localhost:5432/medicines"

engine = create_async_engine(SQLITE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession)
Base = declarative_base()
