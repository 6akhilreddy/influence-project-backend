from models.Influencer import Influencer
from utilities.security import Security
from factory.validation import Validator

from datetime import datetime

class InfluencerController:
    def __init__(self) -> None:
        self.influencer = Influencer()
        self.validator = Validator()
        self.security = Security()

    def createInfluencer(self, user):

        # Validator will throw error if invalid
        self.validator.validate(user, self.influencer.fields, self.influencer.create_required_fields)

        # verify username already exists
        found_username = len(self.influencer.find({'username': user['username']})) > 0
        
        if not found_username:

            # encrypt the password
            encrypted_password = self.security.encryptPassword(user['password'])
            user['password'] = encrypted_password

            # get the date from timestamp if present
            if 'date_of_birth' in user:
                date_of_birth = datetime.utcfromtimestamp(int(user['date_of_birth'])/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
                user['date_of_birth'] = date_of_birth

            response = self.influencer.create(user)

            return response

        else:
            raise Exception("Username is already present")

    def verifyInfluencer(self, user):
        self.validator.validate(user, self.influencer.fields, self.influencer.login_required_fields)

        # get the influencer data by username
        influencers = self.influencer.find({'username': user['username']})

        if len(influencers) > 0:
            # get the first user
            influencer_data = influencers[0]

            # verify password
            if self.security.verifyPassword(influencer_data['password'], user['password']):
                return True
            
            return False
        
        else:
            raise Exception("Username does not exists")
