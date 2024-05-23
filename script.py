import psycopg2
import os

def run_delete_query():
    # Get database connection parameters from environment variables
    db_host = os.environ.get('DATABASE_HOST', '127.0.0.1/32')
    db_port = os.environ.get('DATABASE_PORT', '5432')
    db_name = os.environ.get('DATABASE_NAME','credentials')
    db_user = os.environ.get('DATABASE_USER','postgres')
    db_password = os.environ.get('DATABASE_PASSWORD','Jtrip23@')

    conn=None

    try:
        # Connect to the database
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        
        # Execute the delete query
        cursor = conn.cursor()
        cursor.execute(f"""
                DELETE FROM public.credentials_data
        """)
        conn.commit()
        print("Delete query executed successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL or executing query:", error)

    finally:
        # Close database connection
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    run_delete_query()
