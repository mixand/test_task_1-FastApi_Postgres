from fastapi import APIRouter, BackgroundTasks

from logs_info import logger
from utils.models import InputData, QuestionsDb, LastQuestion
from utils.others import matching_and_saving

router = APIRouter(
    prefix="/questions",
    tags=['questions']
)


@router.post("/", status_code=200, response_model=LastQuestion)
async def get_questions(input_data: InputData, background_tasks: BackgroundTasks):
    background_tasks.add_task(matching_and_saving, input_data.questions_num)
    try:
        last_question = await QuestionsDb.get_last_question()
    except Exception:
        logger.error(f"get_questions has error", exc_info=True)
    return {"last_question": last_question}
