from models import db
from models import other
from .base_service import BaseService

class UserService(BaseService):       
    def get(self, limit: int, offset: int) -> list[db.User]:
        return self.user_repo.get(limit=limit, offset=offset)
                
    def get_by_id(self, id: int) -> db.User | None:
        return self.user_repo.get_by_id(id)
        
    def get_by_email(self, email: str) -> db.User | None:
        return self.user_repo.get_by_email(email)
    
    def get_by_email_and_pass(self, email: str, password: str) -> db.User | None:
        result = None
        user = self.user_repo.get_by_email(email)
        if user and user.password == password:
            result = user
        return result
    
    def create(self, name: str, surname: str, role: other.Role, email: str, password: str) -> db.User:
        user = db.User()
        user.name = name
        user.surname = surname
        user.role = role
        user.email = email
        user.password = password

        user_id = self.user_repo.add(user)
        return self.get_by_id(user_id)
    
    def update(self, user: db.User) -> db.User | None:
        self.user_repo.update(user)
        return self.get_by_id(user.id)
    
    def delete(self, user: db.User) -> None:
        self.user_repo.delete(user.id)
        
    