"""database control"""
from flask import session as flasksesh
import newmod
from newmod import session as dbsesh
from sqlalchemy.orm import subqueryload

def guests_by_party():
    parties = dbsesh.query(newmod.Party).all()
    gparties = {'parties': [party.as_dict() for party in parties]}
    return gparties

def one_party():
    parties = dbsesh.query(newmod.Party).limit(5).all()
    # print parties
    return [party.as_dict() for party in parties]

def guests_by_guest():
    guests = dbsesh.query(newmod.Guest).all()
    jsguests = {'guests': [guest.as_json() for guest in guests]}
    return jsguests

def groups_side_filters():
    groups = dbsesh.query(newmod.Party.grouping).distinct().all()
    sides = dbsesh.query(newmod.Party.side).distinct().all()
    # print groups, sides
    js = {'side': [name[0] for name in sides]}
    js['grouping'] = [group[0] for group in groups]
    # print js
    # d = {}
    # for tup in groups:
    #     if tup[1] in d.keys():
    #         d[tup[1]].append(tup[0])
    #     else:
    #         d[tup[1]] = [tup[0]]
    # # print d
    # return d
    return js

def grouping_headers():
    heads = dbsesh.query(newmod.Party.grouping).distinct().all()
    # print heads
    return heads


# print parties
