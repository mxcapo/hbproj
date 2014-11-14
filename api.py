"""database control"""
import flask
from model import Party, Guest, session


def guests_by_party():
    parties = session.query(Party).all()
    gparties = {'parties': [party.as_dict() for party in parties]}
    return gparties

def one_party():
    parties = session.query(Party).limit(5).all()
    guests = session.query(Guest).limit(5).all()
    q = {'parties': [party.as_dict() for party in parties]}, \
        {'guests': [guest.as_dict() for guest in guests]}
    # print "------------------------\n", q, "\n------------------------"
    return q

def guests_by_guest():
    guests = session.query(Guest).all()
    jsguests = {'guests': [guest.as_json() for guest in guests]}
    return jsguests

def groups_side_filters():
    groups = session.query(Party.grouping).distinct().all()
    sides = session.query(Party.side).distinct().all()
    priority = session.query(Guest.priority).distinct().all()
    probability = session.query(Guest.probability).distinct().all()
    # print groups, sides
    js = {'side': [name[0] for name in sides]}
    js['grouping'] = [group[0] for group in groups]
    js['probability'] = [prob[0] for prob in probability]
    js['priority'] = [prior[0] for prior in priority]
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
    heads = session.query(Party.grouping).distinct().all()
    # print heads
    return heads


# print parties
