# here do all validations and business logic for user
class UserService:

    def __init__(self, dao):
        self.dao = dao

    def validate_user_data(self, data):
        # Perform validation logic here
        if 'name' not in data or 'email' not in data:
            raise ValueError("Name and email are required fields.")
        # Add more validation rules as needed
        
    def get_all_user_service(self):
        return self.dao.get_all_user_model()

    def add_user_service(self, data):
        return self.dao.add_user_model(data)

    def add_multiple_users_service(self, data):
        return self.dao.add_multiple_users_model(data)

    def delete_user_service(self, id):
        return self.dao.delete_user_model(id)

    def update_user_service(self, data):
        return self.dao.update_user_model(data)

    def patch_user_service(self, data):
        return self.dao.patch_user_model(data)