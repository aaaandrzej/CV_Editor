from models import Cv, User
from session import get_session

if __name__ == '__main__':

    session = get_session(echo=False)

    cv9 = session.query(Cv).get(9)
    user = session.query(User).get(1)

    # print(user)

    # session.delete(billy)

    # session.commit()

    # for instance in session.query(Cv).order_by(Cv.id):
    #     print(instance.python)

    cv_list = [cv_instance for cv_instance in session.query(Cv)]

    print(cv_list)