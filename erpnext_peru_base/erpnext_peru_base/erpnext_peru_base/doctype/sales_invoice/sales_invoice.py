# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import frappe.defaults
from frappe.utils import cint, cstr, flt
from frappe import _, msgprint, throw
from erpnext.accounts.party import get_party_account, get_due_date
from erpnext.controllers.stock_controller import update_gl_entries_after
from frappe.model.mapper import get_mapped_doc


def autoname(sales_invoice, method):
	from frappe.model.naming import make_autoname
	sales_invoice.name = make_autoname(sales_invoice.document_type+sales_invoice.serie_nr+'-.######')
	sales_invoice.document_nr = sales_invoice.name.split("-")[1]
	#self.name = str(self.document_type) + ' - ' + str(self.document_nr)


def get_default_naming_series(doctype, method):
	naming_series = "FT666,FT5555,FT6666"
	naming_series = naming_series.split(",")
	doctype.naming_series = naming_series[1]
	return naming_series[1] or naming_series[2]

def get_options(doct, method,arg=''):
	aaa="FT666,FT7777"
	print aaa
	return aaa

def preserve_naming_series_options_in_property_setter(doct,method):
	naming_series = "FT666,FT5555,FT6666"
	naming_series = naming_series.split(",")
	doct.naming_series = naming_series[0]
	return naming_series[0] or naming_series[1]

# def validate(sales_invoice, method):
# 	sales_invoice.naming_series = "23123"
# 	super(SalesInvoice, sales_invoice).validate()
