from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import Boolean, Integer, String, DateTime

from ..database import db
from ..mixins import CRUDModel

class loginData(CRUDModel):
    __tablename__ = 'prihlaseni'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    jmeno = Column(String, nullable=False, index=False)
    prijmeni = Column(String, nullable=False, index=False)
    muz = Column(Boolean(name='muz'), default=False)
    zena = Column(Boolean(name='zena'), default=False)



    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

