from typing import Union, Any
from pydantic import BaseModel
from sqlalchemy import select

from db import questions_db, database


class InputData(BaseModel):
    questions_num: int


class LastQuestion(BaseModel):
    last_question: Union[str, None]


class QuestionsDb:
    @staticmethod
    async def get_last_question() -> Union[dict, None]:
        query = select(questions_db).order_by(questions_db.columns.id.desc())
        result = await database.fetch_one(query)
        if result is not None:
            result = dict(result)["question"]
        return result

    @staticmethod
    async def check_question(id_value: int) -> Any:
        query = select(questions_db).where(questions_db.columns.id_question == id_value)
        return await database.fetch_one(query)

    @staticmethod
    async def pots_question_to_db(id_question: int, question: str, answer: str, data_created: str) -> None:
        dict_post = {"id_question": id_question,
                     "question": question,
                     "answer": answer,
                     "data_created": data_created,
                     }
        query = questions_db.insert().values(dict_post)
        await database.execute(query=query)
