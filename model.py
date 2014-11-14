from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from json import dumps

engine  = create_engine("sqlite:///wedding.db", echo=False)
session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base       = declarative_base()
Base.query = session.query_property()

class Party(Base):
    __tablename__ = "parties"
    id            = Column(Integer, primary_key =True)
    side          = Column(String(30), nullable=False)
    grouping      = Column(String(40), nullable=True)
    addr_1        = Column(String(50), nullable=True)
    addr_2        = Column(String(50), nullable=True)
    city          = Column(String(50), nullable=True)
    state         = Column(String(10), nullable=True)
    zipcode       = Column(String(15), nullable=True)
    country       = Column(String(30), nullable=True)

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
                            'name': guest.name(),
                            'guest_type': guest.guest_type}
                            for guest in self.guests]
        # print sdict
        return sdict

    def as_json(self):
        sjs = dumps(self.as_dict())
        return sjs

class Guest(Base):
    __tablename__ = "guests"
    id          = Column(Integer, primary_key=True)
    party_id    = Column(Integer, ForeignKey('parties.id'))
    last_name   = Column(String(50), nullable=True)
    first_name  = Column(String(50), nullable=True)
    priority    = Column(String(20), nullable=True)
    probability = Column(String(20), nullable=True)
    gender      = Column(String(1), nullable=True)
    guest_type  = Column(String(30), default="wedding")
    party       = relationship("Party", lazy='joined', \
                                        backref=backref("guests", \
                                        orderby=id))


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

    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def as_dict(self):
        sdict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        sdict['party'] = {'party_id': self.party_id,
                           'side': self.party.side,
                           'grouping': self.party.grouping,
                           'addr_1': self.party.addr_1,
                           'addr_2': self.party.addr_2,
                           'city': self.party.city,
                           'state': self.party.state,
                           'zipcode': self.party.zipcode,
                           'guests': self.party.guests,
                           'country': self.party.country}
        sdict['name'] = self.name()

        sdict['party']['guests'] = [{'last_name': guest.last_name,
                            'first_name': guest.first_name,
                            'priority': guest.priority,
                            'probability': guest.probability,
                            'party_id': guest.party_id,
                            'gender': guest.gender,
                            'name': guest.name(),
                            'guest_type': guest.guest_type}
                            for guest in self.party.guests]
        return sdict


    def as_json(self):
        sjs = dumps(self.as_dict())
        return sjs

# class Wedding(Guest):
#     __mapper_args__ = {'polymorphic_identity': 'wedding'}
#     wedding         = Column(saBool, default=True)

# class RehearsalCocktail(Wedding):
#     __mapper_args__    = {'polymorphic_identity': 'rehearsal_cocktail'}
#     rehearsal_cocktail = Column(saBool, default=True)

# class RehearsalDinner(RehearsalCocktail):
#     __mapper_args__  = {'polymorphic_identity': 'rehearsal_dinner'}
#     rehearsal_dinner = Column(saBool, default=True)

# class Bach(RehearsalDinner):
#     __mapper_args__ = {'polymorphic_identity': 'bach'}
#     bach            = Column(saBool, default=True)

# class WeddingParty(Bach):
#     __mapper_args__ = {'polymorphic_identity': 'wedding_party'}
#     wedding_party   = Column(saBool, default=True)

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
