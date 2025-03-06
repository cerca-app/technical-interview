from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# SQLite database configuration
engine = create_engine(
    "sqlite:///app.db",
    echo=False,
    connect_args={"check_same_thread": False},  # Allow multi-threading for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

