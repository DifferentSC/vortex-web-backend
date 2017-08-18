from flask import Flask
from vortexwebserver.database import init_db, db_session

app = Flask(__name__)
init_db()


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

import vortexwebserver.views