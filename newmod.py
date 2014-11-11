from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey, Table, MetaData
from sqlalchemy import Column as saCol, Integer as saInt, String as saStr, Boolean as saBool
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from flask import make_response
from json import dumps

ENGINE  = None
Session = None
engine  = create_engine("sqlite:///wedding.db", echo=False)
session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base       = declarative_base()
Base.query = session.query_property()

class Party(Base):
    __tablename__ = "parties"
    id            = saCol(saInt, primary_key =True)
    side          = saCol(saStr(30), nullable=False)
    grouping      = saCol(saStr(40), nullable=True)
    addr_1        = saCol(saStr(50), nullable=True)
    addr_2        = saCol(saStr(50), nullable=True)
    city          = saCol(saStr(50), nullable=True)
    state         = saCol(saStr(10), nullable=True)
    zipcode       = saCol(saStr(15), nullable=True)
    country       = saCol(saStr(30), nullable=True)

    def __str__(self):
        output = "----------------------------------------\n"
        output += "%s\n" % self.id
        if self.addr_2:
            output += "%s\n%s\n" % (self.addr_1, self.addr_2)
        else:
            output += "%s\n" % (self.addr_1)
        output += "%s, %s %s %s" % (self.city, self.state,
                                    self.zipcode,
                                    self.country)

        return output

    def as_dict(self):
        sdict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        sdict['guests'] = [{'last_name': guest.last_name,
                            'first_name': guest.first_name,
                            'priority': guest.priority,
                            'probability': guest.probability,
                            'party_id': self.id,
                            'gender': guest.gender,
                            'guest_type': guest.guest_type}
                            for guest in self.guests]
        # print sdict
        return sdict

    def as_json(self):
        sjs = dumps(self.as_dict())
        return sjs

class Guest(Base):
    __tablename__ = "guests"
    id          = saCol(saInt, primary_key=True)
    party_id    = saCol(saInt, ForeignKey('parties.id'))
    last_name   = saCol(saStr(50), nullable=True)
    first_name  = saCol(saStr(50), nullable=True)
    priority    = saCol(saStr(20), nullable=True)
    probability = saCol(saStr(20), nullable=True)
    gender      = saCol(saStr(1), nullable=True)
    guest_type  = saCol(saStr(30), default="wedding")
    party       = relationship("Party", backref="guests")


    # __mapper_args__ = {'polymorphic_identity': 'guest',
    #                    'polymorphic_on': guest_type}

    def __str__(self):
        output = "----------------------------------------\n"
        output += "Guest: %s, %s\n" % (self.last_name,
                                       self.first_name)
        output += "Guest Type: %s\n" % (self.guest_type)
        output += "Guest ID: %r \nParty ID: %r\n" % (self.id,
                                                     self.party_id)
        output += "Priority: %s\nProbability: %s" % (self.priority,
                                                     self.probability)

        return output

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def as_json(self):
        sjs = dumps(self.as_dict())
        return sjs

# class Wedding(Guest):
#     __mapper_args__ = {'polymorphic_identity': 'wedding'}
#     wedding         = saCol(saBool, default=True)

# class RehearsalCocktail(Wedding):
#     __mapper_args__    = {'polymorphic_identity': 'rehearsal_cocktail'}
#     rehearsal_cocktail = saCol(saBool, default=True)

# class RehearsalDinner(RehearsalCocktail):
#     __mapper_args__  = {'polymorphic_identity': 'rehearsal_dinner'}
#     rehearsal_dinner = saCol(saBool, default=True)

# class Bach(RehearsalDinner):
#     __mapper_args__ = {'polymorphic_identity': 'bach'}
#     bach            = saCol(saBool, default=True)

# class WeddingParty(Bach):
#     __mapper_args__ = {'polymorphic_identity': 'wedding_party'}
#     wedding_party   = saCol(saBool, default=True)

def create_database():
    Base.metadata.create_all(engine)
    # print "made it"
def drop_create_all():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def main():
    pass

if __name__ == "__main__":
    main()
