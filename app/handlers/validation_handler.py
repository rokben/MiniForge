from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request


def validation_exception_handler(_request : Request, exc : RequestValidationError): 
    errors = exc.errors()
    dict_error={"detail":{}}
    for error in errors:
        dict_error["detail"][error["loc"][1]] = error["msg"]

    return JSONResponse(
        status_code=422,
        content=dict_error
    )

