import peewee
from peewee import *

db = SqliteDatabase('ritsu.sqlite')

class BaseModel(Model):
    class Meta:
        database = db
        
class User(BaseModel):
    id = IntegerField(primary_key=True)
    join_date = DateTimeField()
    origin = CharField()
    status = CharField()
    activity = CharField()
    
    def create(id, join_date, origin, status, activity):
        User.create(id=id, join_date=join_date, origin=origin, status=status, activity=activity)
        
    def read(id):
        return User.select().where(User.id == id)
    
    def update(id, join_date, origin, status, activity):
        User.update(id=id, join_date=join_date, origin=origin, status=status, activity=activity).where(User.id == id).execute()
        
    def delete(id):
        User.delete().where(User.id == id).execute()
        
    def list():
        #lists all users
        
        for user in User.select():
            users = []
            #add all data of a user to a list in a list
            users.append([user.id, user.join_date, user.origin, user.status, user.activity])
            
        return users
    
class Qualification(BaseModel):
    id = CharField(primary_key=True)
    category = CharField()
    
class UserQualification(BaseModel):
    id = IntegerField(primary_key=True)
    user_id = ForeignKeyField(User, backref='qualifications')
    qualification_id = ForeignKeyField(Qualification, backref='users')
    
class Group(BaseModel):
    id = IntegerField(primary_key=True)
    lead = ForeignKeyField(User, backref='groups')
    creation_date = DateTimeField()
    
class Series(BaseModel):
    id = IntegerField(primary_key=True)
    order_id = DeferredForeignKey('Order', backref='series')
    group_id = ForeignKeyField(Group, backref='series')
    manager = ForeignKeyField(User, backref='series')

class Chapter(BaseModel):
    id = IntegerField(primary_key=True)
    series_id = ForeignKeyField(Series, backref='chapters')
    status = CharField()
    started = DateTimeField()
    finished = DateField()
    
class Job(BaseModel):
    id = IntegerField(primary_key=True)
    chapter_id = ForeignKeyField(Chapter, backref='jobs')
    assigned_user = ForeignKeyField(User, backref='jobs')
    started = DateTimeField()
    finished = DateTimeField()
    locked = BooleanField()
    
class JobQualification(BaseModel):
    id = IntegerField(primary_key=True)
    qualification_id = ForeignKeyField(Qualification, backref='qualified')

class Order(BaseModel):
    id = IntegerField(primary_key=True)
    order = IntegerField()
    job_id = ForeignKeyField(Job, backref='orders')


db.connect()
if not db.table_exists('user'):
    db.create_tables([User, Qualification, UserQualification, Group, Series, Chapter, Job, JobQualification, Order])
    
print(User.list())