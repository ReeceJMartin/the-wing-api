from fastapi import APIRouter
import datetime

router = APIRouter()


@router.get("/greeting/", tags=["greeting"])
def read_item_again():
    file = open("currentMessage.txt", "r")

    message = file.read()

    file.close()

    messageJSON = {"message": message}

    return messageJSON


@router.post("/greeting/{new}")
def post(new: int):
    file = open("currentMessage.txt", "w")

    file.write(str(new))

    file.close()

    time = datetime.datetime.now()

    inputJSON = {"input": [new], "time": [str(time)]}

    return inputJSON
