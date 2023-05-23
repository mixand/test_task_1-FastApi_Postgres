import asyncio
import requests

from typing import Union, List

from logs_info import logger
from utils.models import QuestionsDb


async def get_questions_list(count_value: int) -> Union[List[dict], None]:
    url = "https://jservice.io/api/random"

    data = {"count": count_value}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=data)
    try:
        result = response.json()
        return result
    except Exception:
        logger.error(f"get_questions_list did not respond")
        return None


async def matching_and_saving(count_value: int) -> None:
    try:
        for i in range(count_value):
            time_sleep: int = 1
            while True:
                one_question = await get_questions_list(1)
                logger.info(one_question)
                if one_question is not None:
                    check_question_result = await QuestionsDb.check_question(one_question[0]["id"])
                    if check_question_result is None:
                        await QuestionsDb.pots_question_to_db(one_question[0]["id"], one_question[0]["question"],
                                                              one_question[0]["answer"], one_question[0]["created_at"])
                        break
                    logger.info(one_question[0]["id"])
                else:
                    logger.error(f"error with request, time_sleep={time_sleep}")
                    await asyncio.sleep(time_sleep)
                    time_sleep += 1
    except Exception:
        logger.error(f"matching_and_saving has error", exc_info=True)
