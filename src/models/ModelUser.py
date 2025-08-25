from .entities.User import User

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, password FROM login 
                    WHERE status = 1 AND id = '{}'""".format(user.username)
            cursor.execute(sql)  #ejecuta la consulta
            row = cursor.fetchone()
            # cursor.close()

            if row != None:
                user = User(0, row[0], User.check_password(row[1], user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id FROM login 
                    WHERE status = 1 AND id = '{}'""".format(id)
            cursor.execute(sql)  #ejecuta la consulta
            row = cursor.fetchone()
            # cursor.close()

            if row != None:
                return  User(0, row[0], None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
        