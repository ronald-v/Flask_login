from .entities.User import User

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, fullname FROM users 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)  #ejecuta la consulta
            row = cursor.fetchone()
            cursor.close()

            if row != None:
                print('DB:', row[2])
                print('Form:', user.password)
                print('Hash:', User.generate_password(user.password))

                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, fullname FROM users WHERE id = {}".format(id)
            cursor.execute(sql)  #ejecuta la consulta
            row = cursor.fetchone()
            cursor.close()

            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
        