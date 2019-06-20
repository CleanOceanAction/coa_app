from flask import render_template, request, session


def contribute(updater: str, eventcode: str):
    title = 'Please enter your contribution!'
    sites = get_sites()
    tls = get_tls()
    trash_items = get_trash_items()

    return render_template('input_form.html',
                           title=title,
                           sites=sites,
                           tls=tls,
                           trash_items=trash_items,
                           updater=updater,
                           eventcode=eventcode,
                           active_page='contribution')


@APP.route('/')
def index():
    need_to_login = not ('updater' in session and
                         'eventcode' in session and
                         1 <= len(session['updater']) and
                         1 <= len(session['eventcode']))
    if need_to_login:
        return render_template('login.html')

    updater = session['updater']
    eventcode = session['eventcode']
    return contribute(updater, eventcode)


@APP.route('/saveuserinfo', methods=['POST'])
def saveuserinfo():
    userinfo = request.form.items()[0][0].split('||')
    updater = userinfo[0]
    eventcode = userinfo[1]
    if 1 <= len(updater) and 1 <= len(eventcode):
        session['updater'] = updater
        session['eventcode'] = eventcode
        return contribute(updater, eventcode)
    else:
        return render_template('login.html')


@APP.route('/thank_you')
def thank_you():
    return render_template('thank_you.html',
                           title='Your records have been successfully saved!',
                           active_page='contribution')
