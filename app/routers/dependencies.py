from app.sql.database import Database


Database.base().metadata.create_all(bind=Database.engine())


async def get_database_session():
    db = Database.session()()

    try:
        yield db
    finally:
        db.close_all()
