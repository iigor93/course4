""" проверка пользователя в БД, генерация и обновление токенов"""


from dao.user import UserDAO
from service.user import get_hash
import hmac
from config import PWD_HASH_SALT, PWD_HASH_ITERATIONS, ALGO, SECRET
import jwt
import datetime, calendar


class AuthService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def check_user(self, data):
        username = data.get('username')
        password = data.get('password')
        users_db = self.dao.get_all_filter(username)
        if users_db:
            for user in users_db:
                if hmac.compare_digest(user.password.encode('utf-8'), get_hash(password).encode('utf-8')):
                    return self.generate_tokens(user)
        return None

    def generate_tokens(self, user):
        data = {}
        data['user_id'] = user.id
        data['username'] = user.username
        data['role'] = user.role

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        return {"access_token": access_token, "refresh_token": refresh_token}


    def refresh_tokens(self, data):
        refresh_token = data.get('refresh_token')
        try:
            result = jwt.decode(refresh_token, SECRET, algorithms=[ALGO])
            day_now = datetime.datetime.utcnow()
            if result.get('exp') >= calendar.timegm(day_now.timetuple()):
                user = self.dao.get_one(result.get('user_id'))
                return self.generate_tokens(user)
            return None
        except Exception as e:
            return False
