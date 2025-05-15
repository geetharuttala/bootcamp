from pydantic import BaseModel, conint, constr

class User(BaseModel):
    username: constr(min_length=3)
    age: conint(gt=0)

u = User(username="geetha", age=30)
print(u)
