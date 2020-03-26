from database import init_db, Session

def main():
    init_db()
    session = Session()
    session.commit()

if __name__ == '__main__':
    main()