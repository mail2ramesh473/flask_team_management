import MySQLdb
import json
from copy import deepcopy

from configs.config import config_dict


def get_mysql_connection():
    try:
        conn = MySQLdb.connect(
            host=config_dict['db']['host'],
            user=config_dict['db']['username'],
            passwd=config_dict['db']['password'],
            db=config_dict['db']['db'],
            connect_timeout=int(config_dict['db']['timeout'])
        )
        if config_dict['db']['db']:
            conn.autocommit(True)
        cursor = conn.cursor()

    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception:
        conn, cursor = None, None

    return conn, cursor


def validate_request(req_data):
    for re_key in req_data:
        if re_key in ['firstName', 'lastName', 'phone', 'emailId', 'role']:
            return True
    return False


def format_response(response):
    new_response = deepcopy(response)
    for res_key in new_response:
        if res_key not in ['userId', 'firstName', 'lastName', 'phone', 'emailId', 'role']:
            response.pop(res_key)
    return response


def get_document(user_id):
    query = "SELECT * from members where userId='%s'" % user_id
    conn, cursor = get_mysql_connection()
    cursor.execute(query)
    result = cursor.fetchone()
    return result


def insert_document(first_name=None, last_name=None, phone_number=None, email=None, role=None):
    conn, cursor = get_mysql_connection()
    keys, values = [], []
    if first_name:
        keys.append("firstName")
        values.append("""%s""" % first_name)
    if last_name:
        keys.append("lastName")
        values.append("""%s""" % last_name)
    if phone_number:
        keys.append("phone")
        values.append("""%s""" % phone_number)
    if email:
        keys.append("emailId")
        values.append("""%s""" % email)
    if role:
        keys.append("role")
        values.append("""%s""" % role)
    query = 'INSERT into members %s values'
    query = query % str(tuple(keys))
    query = query.replace("'", "")
    query = query + "%s" % str(tuple(values))
    cursor.execute(query)
    uniq_id = cursor.lastrowid

    return uniq_id

def update_document(user_id, first_name=None, last_name=None, phone_number=None, email=None, role=None):
    conn, cursor = get_mysql_connection()
    query = 'update members set'
    if first_name:
        query += ' firstName="%s"'%first_name
    if last_name:
        query += ', lastName="%s"' % last_name
    if phone_number:
        query += ', phone="%s"' % phone_number
    if email:
        query += ', emailId="%s"' % email
    if role:
        query += ', role="%s"' % role

    query += ' where userId=%s'%user_id
    cursor.execute(query)

    return True


def delete_document(user_id):
    conn, cursor = get_mysql_connection()
    query = 'delete from members where userId=%s'%user_id
    status = cursor.execute(query)
    import pdb;pdb.set_trace()



