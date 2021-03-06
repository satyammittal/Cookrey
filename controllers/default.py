def index():
    if auth.user: redirect(URL('recipes?id=0'))
    #print db.auth_group[auth.user_id].role
    return locals()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
@auth.requires_membership('admins')
def manage():
    tablename = request.args(0)
    if tablename: 
        grid = SQLFORM.smartgrid(db[tablename])
    else:
        grid = UL(*[LI(A(t,_href=URL(args=t))) for t in db.tables])
    page_title="admin"
    return locals()
def user():
    return dict(form=auth())
def like():
   try:
       id1=request.vars.id
       print "t"
       form =id1
       db.likes.insert(username=auth.user_id,rec=form)
       new_votes=db.recipe[form].nolike+1
       
       print new_votes
       db.recipe[form].update_record(nolike=new_votes)
       return str(new_votes)
   except:
       return str("#you already like this")

def call():
    session.forget()
    return service()

# our home page, will show our posts and posts by friends
@auth.requires_login()
def home():
    form=SQLFORM(db.recipe,fields=['title',
                               'ingredients','directions','Country','notes','pictures','type'])
    username=db.auth_user
    if form.accepts(request,session):
        redirect(URL('recipes?id=0'))
    return dict(form=form,username=username)

# our wall, will show our profile and our own posts
@auth.requires_login()
def recipes():
    id=request.vars.id
    if not id:
        id=0
    
    records=db(db.recipe).select(orderby=~db.recipe.creationTime, limitby=(id*10,id*10+10))
    if id>0:
        back=id-1
    else:
        back=id
    #form=SQLFORM(db.recipe,fields=['category'])
    return dict(records=records,k=id+1,back=back)
@auth.requires_login()
def show():
    id=request.vars.id
    recipes=db(db.recipe.id==id).select()
    if not len(recipes): redirect(URL('recipes'))
    if db.recipe[id].user_ref==auth.user_id:
        recipeForm = SQLFORM(db.recipe, recipes[0],fields=['title',
                               'ingredients','directions','Country','notes','pictures'], deletable=True, showid=False)

    else:
        recipeForm="Cann't be edited Press esc key"
    return dict(recipe=recipes[0],recipeForm=recipeForm)
@auth.requires_login()
def wall():
    records=db(db.recipe.user_ref == auth.user_id).select(db.recipe.title,db.recipe.Country,db.recipe.creationTime,db.recipe.pictures,db.recipe.type)
    return dict(records=records)
# a page for searching friends and requesting friendship
@auth.requires_login()
def search():
    FOOD="VEG OR NON-VEG"
    form1 = FORM(INPUT(_type="text", _name="var"), _action="fsearch")
    return locals() 
def fsearch():
    var=str(request.vars["var"])
    records=db(db.recipe.type==var).select()
    return locals()
