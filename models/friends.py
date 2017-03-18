DAL('sqlite://storage.sqlite')
from datetime import datetime
foreign_keys=True
db.define_table('category2',Field('name'),format = '%(name)s')
db.define_table('recipe',
  Field('user_ref','reference auth_user', default=auth.user, readable=False, writable=False),
  Field('creationTime','datetime', default=datetime.utcnow(), readable=False, writable=False),
  Field('nolike','integer',default=0,readable=True,writable=True),
  Field('title','string', requires=IS_NOT_EMPTY()),
  Field('type',requires=IS_IN_SET(['VEG', 'NON-VEG'])),
  Field('ingredients','list:string', requires=IS_NOT_EMPTY()),
  Field('directions','list:string', requires=IS_NOT_EMPTY()),
  Field('Country','string'),
  Field('notes','text'),
  Field('pictures','upload'),
)
db.define_table('likes',
   Field('username','reference auth_user'),
   Field('rec','reference recipe'),
   Field('unique_key', unique=True, notnull=True,compute= lambda x:(x.username," ",x.rec) ),
               )
