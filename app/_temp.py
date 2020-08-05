from models import Cv, User
from session import get_session

if __name__ == '__main__':

    session = get_session(echo=False)

    # cv9 = session.query(Cv).first()._asdict()
    #
    # print(cv9)

    user = session.query(Cv).first()

    d = user.object_as_dict()

    print(d)


    # user = session.query(User).get(1)
    # user = session.query(User).filter(User.username == "admin").all()[0]

    # print(user.password)

    # session.delete(billy)

    # session.commit()

    # for instance in session.query(Cv).order_by(Cv.id):
    #     print(instance.python)

    # cv_list = [cv_instance for cv_instance in session.query(Cv)]
    #
    # print(cv_list)
