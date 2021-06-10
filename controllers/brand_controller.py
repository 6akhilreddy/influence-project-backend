from models.Brand import Brand
from utilities.security import Security
from factory.validation import Validator

class BrandController:
    def __init__(self) -> None:
        self.brand = Brand()
        self.validator = Validator()
        self.security = Security()

    def createBrand(self, company):

        # Validator will throw error if invalid
        self.validator.validate(company, self.brand.fields, self.brand.create_required_fields)

        # verify username already exists
        found_username = len(self.brand.find({'username': company['username']})) > 0
        
        if not found_username:

            # encrypt the password
            encrypted_password = self.security.encryptPassword(company['password'])
            company['password'] = encrypted_password

            response = self.brand.create(company)

            return response

        else:
            raise Exception("Username is already present")

    def verifyBrand(self, company):
        self.validator.validate(company, self.brand.fields, self.brand.login_required_fields)

        # get the influencer data by username
        brands = self.brand.find({'username': company['username']})

        if len(brands) > 0:
            # get the first user
            brand_data = brands[0]

            # verify password
            if self.security.verifyPassword(brand_data['password'], company['password']):
                return True
            
            return False
        
        else:
            raise Exception("Username does not exists")
