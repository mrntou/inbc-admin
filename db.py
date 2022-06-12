from IA.models import *
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument('-u', '--user', action='store_true')
ap.add_argument('-d', '--delete', action='store_true')
ap.add_argument('-r', '--region', action='store_true')

args = vars(ap.parse_args())

def create_database():
    db.create_all()
    print('Done.')

create_database()

if args['user']:
    user = User(username='admin')
    user.set_password('admin')
    db.session.add(user)
    db.session.commit()
    print('User admin has been created!')

if args['region']:
    regions = ['satikoy','omurlukoy','basirlikoy','demirbeyli']
    for x in regions:
        r = Region(region=x)
        db.session.add(r)
    db.session.commit()

if args['delete']:
    os.remove(r"IA/iadata.db")
    # create_database()
    # user = User(username='admin')
    # user.set_password('admin')
    # db.session.add(user)
    # db.session.commit()


