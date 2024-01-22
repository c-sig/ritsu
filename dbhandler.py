from peewee import *

db = SqliteDatabase('ritsu.sqlite')

class BaseModel(Model):
    class Meta:
        database = db
        
class User(BaseModel):
    id = IntegerField(primary_key=True)
    joined = DateTimeField()
    origin = CharField()
    status = CharField()
    activity = CharField()
    
    def read(id):
        return User.get(User.id == id)
    
    def update(id, joined, origin, status, activity):
        User.update(joined=joined, origin=origin, status=status, activity=activity).where(User.id == id).execute()
        
    def delete(id):
        User.delete().where(User.id == id).execute()
        
    def list():
        return User.select()
    
class Qualification(BaseModel):
    id = CharField(primary_key=True)
    
    def read(id):
        return Qualification.get(Qualification.id == id)
    
    def update(id):
        Qualification.update(id=id).where(Qualification.id == id).execute()
        
    def delete(id):
        Qualification.delete().where(Qualification.id == id).execute()
        
    def list():
        return Qualification.select()
    
class UserQualification(BaseModel):
    id = IntegerField(primary_key=True)
    user_id = ForeignKeyField(User, related_name='qualifications')
    qualification_id = ForeignKeyField(Qualification, related_name='users')
    
    def read(id):
        return UserQualification.get(UserQualification.id == id)
    
    def update(id, user_id, qualification_id):
        UserQualification.update(user_id=user_id, qualification_id=qualification_id).where(UserQualification.id == id).execute()
        
    def delete(id):
        UserQualification.delete().where(UserQualification.id == id).execute()
        
    def list():
        return UserQualification.select()
    
db.connect()

db.create_tables([User, Qualification, UserQualification])

