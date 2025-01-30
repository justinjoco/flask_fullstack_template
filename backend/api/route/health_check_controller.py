from flask import Blueprint
health_check_api = Blueprint('health_check_api', __name__)


@health_check_api.get('/health_check')
def health_check():
    return "", 200
