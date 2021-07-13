from rest_framework.exceptions import APIException


class TodoExecuteException(APIException):
    status_code = 406
    default_code = 'Задача не найдена или не пренадлежит вам'
    default_detail = 'Задача не найдена или не пренадлежит вам'
