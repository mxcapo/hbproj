"""database control"""
from flask import session as flasksesh
import newmod
from newmod import session as dbsesh

def guests_by_party():
    parties = dbsesh.query(newmod.Party).all()
    gparties = {'parties': [party.as_dict() for party in parties]}
    return gparties

def one_party():
    parties = dbsesh.query(newmod.Party).limit(50).all()
    # print parties
    return [party.as_dict() for party in parties]

def guests_by_guest():
    guests = dbsesh.query(newmod.Guest).all()
    jsguests = {'guests': [guest.as_json() for guest in guests]}
    return jsguests

def filters():
    g = dbsesh.query(newmod.Party.grouping, newmod.Party.side).distinct().all()
    d = {}
    for tup in g:
        if tup[1] in d.keys():
            d[tup[1]].append(tup[0])
        else:
            d[tup[1]] = [tup[0]]
    # print d
    return [d]



# print parties
