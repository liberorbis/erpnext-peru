# Copyright (c) 2013, dsdf and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

test_records = frappe.get_test_records('Serial Control')

class TestSerialControl(unittest.TestCase):
	pass
