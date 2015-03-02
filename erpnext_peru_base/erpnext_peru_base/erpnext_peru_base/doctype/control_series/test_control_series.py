# Copyright (c) 2013, Peru and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

test_records = frappe.get_test_records('Control Series')

class TestControl_Series(unittest.TestCase):
	pass
