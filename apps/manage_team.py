import json
from flask import jsonify

from utils import validate_request, format_response, get_document, insert_document, \
    update_document, delete_document


def add_member(data):
    valid_req = validate_request(data)
    if valid_req:
        role = data.get('role')
        role_val = 'admin' if role in (1, 'admin') else 'regular'
        data['role'] = role_val
        unq_id = data.get('userId')
        if unq_id:
            instance = get_document(unq_id)
            if instance:
                http_response = {"success": False, "error": "Document Already exists"}
                http_response.status_code = 400
                return http_response
            else:
                data.pop('userId')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        phone = data.get('phone')
        email = data.get('email')
        role = data.get('role')
        uniq_id = insert_document(first_name=first_name, last_name=last_name,
                                  phone_number=phone, email=email, role=role)

        data['userId'] = uniq_id
        response = format_response(data)
        response = jsonify(response)
        response.status_code = 200
    else:
        res_error = "Neither of required fields are present in Request payload"
        response = jsonify({"success": False, "error": res_error})
        response.status_code = 400

    return response


def update_member(data):
    valid_req = validate_request(data)
    if valid_req:
        role = data.get('role')
        role_val = 'admin' if role in (1, 'admin') else 'regular'
        data['role'] = role_val
        unq_id = data.get('userId')
        if unq_id:
            instance = get_document(unq_id)
            if not instance:
                http_response = {"success": False, "error": "Document not exists"}
                http_response.status_code = 400
                return http_response
        else:
            http_response = {"success": False, "error": "userId required to update document"}
            http_response.status_code = 400
            return http_response
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        phone = data.get('phone')
        email = data.get('email')
        role = data.get('role')
        status = update_document(unq_id, first_name=first_name, last_name=last_name,
                                  phone_number=phone, email=email, role=role)

        response = jsonify({"success": status, "message": "Document Updates successfully"})
        response.status_code = 200
    else:
        res_error = "Neither of required fields are present in Request payload"
        response = jsonify({"success": False, "error": res_error})
        response.status_code = 400

    return response


def delete_member(data):
    import pdb;pdb.set_trace()
    unq_id = data.get('userId')
    if unq_id:
        instance = get_document(unq_id)
        if not instance:
            http_response = {"success": False, "error": "Document not exists"}
            http_response.status_code = 400
            return http_response
    else:
        http_response = {"success": False, "error": "userId required to delete document"}
        http_response.status_code = 400
        return http_response
    status = delete_document(unq_id)
    if status:
        response = jsonify({"success": status, "message": "Document deleted successfully"})
        response.status_code = 200
        return response
