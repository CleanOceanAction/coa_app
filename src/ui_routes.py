from flask import render_template, request, session

@cont.route('/')
def contribute():
    need_to_login = not ('updater' in session and 'eventcode' in session and len(session['updater'])>=1 and len(session['eventcode'])>=1:
    if need_to_login:
        return render_template("login.html")

    updater=session['updater']
    eventcode=session['eventcode']
    title = "Please enter your contribution!"
    sites = get_sites()
    tls = get_tls()
    trash_items = get_trash_items()

    return render_template("input_form.html",
                           title=title,
                           sites=sites,
                           tls=tls,
                           trash_items=trash_items,
                           updater=updater,
                           eventcode=eventcode,
                           active_page='contribution')


@cont.route('/saveuserinfo', methods=['GET', 'POST'])
def saveuserinfo():
    if request.method == 'POST':
        userinfo=request.form.items()[0][0].split('||')
        updater=userinfo[0]
        eventcode=userinfo[1]
        if len(updater)>=1 and len(eventcode)>=1:
            session['updater']=updater
            session['eventcode']=eventcode
            title = "Please enter your contribution!"
            sites = get_sites()
            tls = get_tls()
            trash_items = get_trash_items()
            return render_template("input_form.html",
                                   title=title,
                                   sites=sites,
                                   tls=tls,
                                   trash_items=trash_items,
                                   updater=updater,
                                   eventcode=eventcode,
                                   active_page='contribution')
        else:
            return render_template("login.html")


@cont.route('/thank_you')
def thank_you():
    return render_template("thank_you.html",
                           title="Your records have been successfully saved!",
                           active_page='contribution')
