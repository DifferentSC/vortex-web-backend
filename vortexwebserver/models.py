from sqlalchemy import Table, Column, Integer, String, Enum
from vortexwebserver.database import Base


class RunningDAG(Base):
    __tablename__ = 'running_dag'
    id = Column(Integer, primary_key=True)
    application_name = Column(String(50))
    dag_type = Column(Enum("IR", "Logical", "Physical"))
    dag_json = Column(String(5000))

    def __init__(self, application_name, dag_type, dag_json):
        self.application_name = application_name
        self.dag_type = dag_type
        self.dag_json = dag_json

    def __repr__(self):
        return '<Application name: %r, Dag type: %r, Dag Json: %r>' \
               % (self.application_name, self.dag_type, self.dag_json)
