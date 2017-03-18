# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('COOKrey'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href=URL("home"),
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'
## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################    
def _():
        # shortcuts
        app = request.application
        ctr = request.controller
        # useful links to internal and external resources
        response.menu += [
             (T('Create'), False, URL('default','home')),
        (T('Wall'), False, URL('default','wall')),
        (T('Recipes'), False, URL('default','recipes?id=0')),
        (T('Search'), False, URL('default','search?id=0'))
            ]

        if db.auth_group[auth.user_id] is not None and db.auth_group[auth.user_id].role=='admins':
            response.menu+= [
                (T('Manage'),False,URL('default','manage'))
                ]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
