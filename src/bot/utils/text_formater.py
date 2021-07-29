from src.bot.utils import texts
from src.core.tables import AfterQuiz


def get_text_after_quiz(quiz: AfterQuiz):
    date_str = quiz.created_at.strftime('%d/%m/%Y %H:%M:%S')
    p2 = quiz.parameter2
    if p2.__contains__('['):
        p2 = p2.replace('[', '').replace(']', '').replace(',', ' - ')
    p4 = quiz.parameter4
    if p4.__contains__('['):
        p4 = p4.replace('[', '').replace(']', '').replace(',', ' - ')

    text = texts.AFTER_QUIZ_TEXT.format(quiz.id, date_str, quiz.parameter1,
                                        p2, quiz.parameter3,
                                        p4, quiz.name, quiz.phone, quiz.status)
    return text


def get_text_back_call(back_call: AfterQuiz):
    date_str = back_call.created_at.strftime('%d/%m/%Y %H:%M:%S')
    text = texts.BACK_CALL_TEXT.format(back_call.name, back_call.phone, date_str, back_call.status)
    return text
