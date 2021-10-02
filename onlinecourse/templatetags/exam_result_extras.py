from django import template

register = template.Library()


def is_get_score(question, answer_ids):
    return question.is_get_score(answer_ids)


register.filter('is_get_score', is_get_score)
