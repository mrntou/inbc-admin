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
    antenna_devices = ["LiteBeam 5AC Gen2", "AirGrid M5 HP", "LiteBeam M5"]
    ap_devices = ['INBC NET - VN AP', "INBC NET PSVN A", "INBC NET - OM", "INBCNET5"]
    modem_devices = ['TP-LINK']
    for x in regions:
        r = Region(region=x)
        db.session.add(r)

    for x in antenna_devices:
        an = AntennaDevice(device_name=x)
        db.session.add(an)

    for x in ap_devices:
        ap = ApDevice(device_username=x)
        db.session.add(ap)

    # for x in modem_devices:
    #     modem = ModemDevice(device_name=x)
    #     db.session.add(x)

    db.session.commit()

if args['delete']:
    os.remove(r"IA/iadata.db")
    # create_database()
    # user = User(username='admin')
    # user.set_password('admin')
    # db.session.add(user)
    # db.session.commit()


