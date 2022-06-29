from flask import render_template, redirect, url_for, abort, Blueprint, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from IA.models import *
from IA.forms import *

form = Blueprint('form', '__name__')


# OK
@form.route('/register/member', methods=["POST"])
def register_member():
    form = MemberForm()
    if form.validate_on_submit():
        member = Member(
            username=form.username.data,
            name=form.name.data,
            lastname=form.lastname.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            ipv4=form.ipv4.data,
            mac=form.mac.data
        )
        region = Region.query.get(form.region.data.id)
        region.members.append(member)

        antenna_device = AntennaDevice.query.get(form.antenna_device.data.id)
        antenna_device.members.append(member)

        ap_device = ApDevice.query.get(form.ap_device.data.id)
        ap_device.members.append(member)

        db.session.add(member)
        db.session.commit()
        flash(f"{member.username} isimli kullanıcı başarılı bir şekilde oluşturuldu ", "success")
        return redirect(url_for('main.register'))



@form.route("/member/edit/<int:member_id>", methods=['GET','POST'])
def edit_member(member_id):
    member = Member.query.get_or_404(member_id)
    form = MemberForm()
    if form.validate_on_submit():
        member.username = form.username.data
        member.name = form.name.data
        member.lastname = form.lastname.data
        member.phone_number = form.phone_number.data
        member.email = form.email.data
        member.ipv4 = form.ipv4.data
        member.mac = form.mac.data
            
        region = Region.query.get(form.region.data.id)
        if not member in region.members:
            region.members.append(member)
        
        # Bitakine not al hayvan !!!
        antenna_device = AntennaDevice.query.get(form.antenna_device.data.id)
        if not member in antenna_device.members:
            antenna_device.members.append(member)

        ap_device = ApDevice.query.get(form.ap_device.data.id)
        if not member in ap_device.members:
            ap_device.members.append(member)

        flash(f"<b>{member.username}</b> adlı kullanıcı yeniden düzenlendi ", "success")
        db.session.commit()

        return redirect(url_for('main.users'))

    if request.method == 'GET':
        form.username.data = member.username
        form.name.data = member.name
        form.lastname.data = member.lastname
        form.email.data = member.email
        form.ipv4.data = member.ipv4
        form.phone_number.data = member.phone_number
        form.mac.data = member.mac
        form.antenna_device.data = member.antenna_device
        form.ap_device.data = member.ap_device
        

    url = url_for('form.edit_member', member_id=member.id)


    return render_template("register.html",
                                form=form, title=f"{member.username} adli kullanıcıyı yeniden düzenle",
                                btn="Düzenle",
                                url=url,
                                member=member)

    
@form.route('/member/delete/<int:member_id>')
def delete_member(member_id):
    member = Member.query.get_or_404(member_id)
    db.session.delete(member)
    flash(f'<b>{member.username} </b> adlı kullanıcı veritabanından silindi', 'success')
    db.session.commit()
    return redirect(url_for('main.users'))