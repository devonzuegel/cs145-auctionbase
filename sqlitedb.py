import web

db = web.database(dbn='sqlite', db='auctions.db')

######################BEGIN HELPER METHODS######################

# Enforce foreign key constraints
# WARNING: DO NOT REMOVE THIS!
def enforceForeignKey(): db.query('PRAGMA foreign_keys = ON')

# initiates a transaction on the database
def transaction(): return db.transaction()
# Sample usage (in auctionbase.py):
#
# t = sqlitedb.transaction()
# try:
#   sqlitedb.query('[FIRST QUERY STATEMENT]')
#   sqlitedb.query('[SECOND QUERY STATEMENT]')
# except Exception as e:
#   t.rollback()
#   print str(e)
# else:
#   t.commit()
#
# check out http://webpy.org/cookbook/transactions for examples



# returns the current time from your database
def getTime():
  query_string = 'select time from CurrentTime'
  results = query(query_string)
  return results[0].time  # alternatively: return results[0]['time']



def setTime(new_time):
  t = db.transaction()
  try:
    db.update('CurrentTime', where="time", time = new_time)
  except Exception as e:
    t.rollback()
    print str(e)
  else:
    t.commit()



# returns a single item specified by the Item's ID in the database
def getItemById(item_id):
  q = 'select * from Item where ID = $itemID'
  result = query(q, { 'itemID': item_id })

  # TODO: rewrite this method to catch the Exception in case `result' is empty
  try:
    return result[0]
  except IndexError:
    return 'There are no items with that ID!'

    

def getItems(vars = {}):
  # Create basic query that selects all items
  q = 'select * from Item'

  # If params for the search are indicated, add them to
  # narrow down the query
  if vars != {}:
    q += ' where ' + web.db.sqlwhere(vars, grouping=' AND ')

  return query(q)



# wrapper method around web.py's db.query method
# check out http://webpy.org/cookbook/query for more info
def query(query_string, vars = {}):
  return list(db.query(query_string, vars))



#####################END HELPER METHODS#####################