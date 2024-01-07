from flask import Blueprint, request

blueprint = Blueprint('api', __name__, url_prefix='/api')



@blueprint.route('/nomenclature', methods=['GET'])
def nomenclature():
    return  {
            'message': 'Hello World!',
            'method': request.method
            }