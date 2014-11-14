from model import Guest, Party, session
import csv


def load_guests(session):
    with open('seed_data/guests.csv', 'rU') as csvfile:
        invite_reader = csv.reader(csvfile, delimiter=',')
        next(invite_reader, None)
        for guest_row in invite_reader:
            guest             = Guest()
            # guest.id        = guest_row[0]
            guest.party_id    = guest_row[1]
            guest.last_name   = guest_row[2]
            guest.first_name  = guest_row[3]
            guest.side        = guest_row[4]
            guest.grouping    = guest_row[5]
            guest.priority    = guest_row[6]
            guest.probability = guest_row[7]
            guest.gender      = guest_row[8]
            # guest.guest_type  = guest_row[9]

            session.add(guest)

def load_parties(session):
    with open('seed_data/parties.csv', 'rU') as csvfile:
        party_reader = csv.reader(csvfile, delimiter=',')
        next(party_reader, None)
        for party_row in party_reader:
            party             = Party()
            # party.id        = party_row[0]
            party.side        = party_row[1]
            party.grouping    = party_row[2]
            party.addr_1      = party_row[3]
            party.addr_2      = party_row[4]
            party.city        = party_row[5]
            party.state       = party_row[6]
            party.zipcode     = party_row[7]
            party.country     = party_row[8]

            session.add(party)

def main(session):
    load_guests(session)
    load_parties(session)

    session.commit()

if __name__ == "__main__":
    # s = newmod.connect()
    main(session)
