from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['db_connection_string_value']
engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem",  #ssl offers secure access to the database
    }
  })


def load_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("select* from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)  #row._mapping--->dict(row)
    return jobs
