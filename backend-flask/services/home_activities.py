from datetime import datetime, timedelta, timezone
from opentelemetry import trace

from lib.db import db
# from lib.db import pool, query_wrap_array

#tracer = trace.get_tracer("home.activities")

class HomeActivities:
  # def run(): # removed (logger) to avoid cost
  def run(cognito_user_id=None):  
    #logger.info("HomeActivities")
    #LOGGER.info('Hello Cloudwatch! from  /api/activities/home')
    #with tracer.start_as_current_span("home-activities-mock-data"):
    #  span = trace.get_current_span()
    #  now = datetime.now(timezone.utc).astimezone()
    #  span.set_attribute("app.now", now.isoformat())
      
    sql = db.template('activities','home')
    
    print("SQL-----------")
    print(sql)
    print("SQL-----------")
   

    #with pool.connection() as conn:
    #  with conn.cursor() as cur:
    #    cur.execute(sql)
    #    # this will return a tuple
    #    # the first field being the data
    #    json = cur.fetchone()
    #    #rows = cur.fetchnone()
    #print("-----------")
    #print(sql)
    #print("-----------")
    #print(json[0])
    #return json[0]
    #return results
    results = db.query_array_json(sql)
    return results
    #results ## Error for Rollbar