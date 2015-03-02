# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
import logging
import string
import datetime
import re
import json

from frappe import _
from frappe.model.document import Document

_logger = logging.getLogger(frappe.__name__)

#called father function to validate various numbers of documents by type
@frappe.whitelist(allow_guest=True)
def validate_vat(doc, method):
    ret=True
    if isinstance(doc, basestring):
        doc = json.loads(doc)
    nif = doc.get('doc_number')
    check_duple_vat(doc)
    if not check_vat_pe(nif):
        frappe.throw(_("RUC: {nif} invalid, please review...").format(nif=nif),frappe.DataError)
 #   after_install()
    return ret
#validate number RUC peruvian
def check_vat_pe(nif):
    nif = str(nif)
    if not nif.isdigit():
       frappe.throw(_("Number document: {nif} , only numbers").format(nif=nif),frappe.DataError)
       return False
    if len (nif) <> 11:
        frappe.throw(_("Number document: {nif},  11 dígits, please review...").format(nif=nif),frappe.DataError)
        return  False
    control = str(5432765432)
    n = 0
    for i, j in enumerate(nif[:-1]):
        n += int(control[i]) * int(j)
    r = 11 - n%11
    if r == 11:
        n = 1
    elif r == 10:
       n = 0
    else:
       n = r
    return n == int(nif[-1])

#check duplicate number_doc
def check_duple_vat(doc):

    name_self= doc.get('name')
    nif = doc.get('doc_number')
    if not nif:#is possible nif to be null
        return

    _logger.info("doc is {0}".format(doc))

    customer = frappe.db.sql("""select customer_name, name from `tabCustomer` where (doc_number = %s) and (name <> %s)""" , (nif,name_self),as_dict=True)#only one must exist
    _logger.info("cursor for customer_name is {0}".format(customer))
    customer_name = customer[0].get('customer_name') if len(customer) > 0 else None
    cname = doc.get("customer_name")
    if(customer_name and customer_name == cname and name_self):#nif already exist but is for the same customer
        return
    elif(customer_name):#nif already exists but another customer already has it
        frappe.throw(_("Number {nif} exist in {name}").format(nif=nif, name=customer_name),frappe.DataError)
    else:#no customer exist with this nif. Save it
        return
