# ERROR_CODE

from msilib.schema import Error


ERROR_CODE = {
    401: "Authorization fail (权限错误)",

    500: "Invalid parameter (无效参数)",
    501: "Json Parse Error (Json解析错误)",


}


def success():
    return 200, "ok"


def authorization_fail():
    return 401, ERROR_CODE[401]


def invalid_parameter():
    return 500, ERROR_CODE[500]


def json_parse_error():
    return 501, ERROR_CODE[501]



