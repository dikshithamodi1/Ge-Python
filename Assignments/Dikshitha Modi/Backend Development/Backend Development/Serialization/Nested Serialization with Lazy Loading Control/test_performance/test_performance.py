from sqlalchemy import event

def test_query_count(db_session):
    # Count SQL queries executed
    query_count = 0
    @event.listens_for(engine, "before_cursor_execute")

def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    nonlocal query_count
    query_count += 1
    
client.get("/users/")
assert query_count == 1 # Ensure only 1 query run (JOIN)