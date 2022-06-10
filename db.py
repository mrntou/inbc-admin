from IA.models import *
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-u', '--user', action='store_true')
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


