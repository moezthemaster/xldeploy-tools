import requests
import xmltodict
import logging
import sys

XLD_BASE_URL = 'http://127.0.0.1:4516/deployit/repository/ci/'
RESSOURCE = 'Infrastructure/DEV_LOCAL'
AUTH = ('admin', 'password')
HEADERS = {'Content-Type': 'application/xml'}


def get_ressource_id(ressource):
    """

    :param ressource:
    :return:
    """
    r = requests.get(XLD_BASE_URL + ressource, auth=AUTH, headers=HEADERS, verify=False)
    my_dict = xmltodict.parse(r.text)
    token = my_dict['file.Archive']['@token']
    return token


def get_infrastructure_os(infra):
    r = requests.get(XLD_BASE_URL + infra, auth=AUTH, headers=HEADERS, verify=False)
    my_dict = xmltodict.parse(r.text)
    os = my_dict['overthere.LocalHost']['os']
    return os


a = get_infrastructure_os(RESSOURCE)
print a

# print my_dict['file.Archive']['@id']
# print my_dict['file.Archive']['@token']
# print my_dict['file.Archive']['@created-by']
