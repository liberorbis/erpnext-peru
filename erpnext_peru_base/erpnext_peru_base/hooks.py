app_name = "erpnext_peru_base"
app_title = "erpnext_peru_base"
app_publisher = "LiberOrbis Sistemas SAC"
app_description = "Localization peruvian for ERPNext"
app_icon = "octicon octicon-zap"
app_color = "blue"
app_email = "erpnext@liberorbis.com"
app_version = "0.0.1"


fixtures = [
	"Custom Field",
	"Custom Script"
]
doc_events = {
     	"Customer": {
		"validate": "erpnext_peru_base.erpnext_peru_base.validate_vat.validate_vat",
        },
	"Sales Invoice": {
		"autoname": "base_peru.base_peru.doctype.sales_invoice.sales_invoice.autoname",
		"get_default_naming_series": "base_peru.base_peru.doctype.sales_invoice.sales_invoice.get_default_naming_series",
		"preserve_naming_series_options_in_property_setter": "base_peru.base_peru.doctype.sales_invoice.sales_invoice.preserve_naming_series_options_in_property_setter"
	}

}
## Includes in <head>
## ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_peru_base/css/erpnext_peru_base.css"
# app_include_js = "/assets/erpnext_peru_base/js/erpnext_peru_base.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_peru_base/css/erpnext_peru_base.css"
# web_include_js = "/assets/erpnext_peru_base/js/erpnext_peru_base.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_peru_base.install.before_install"
# after_install = "erpnext_peru_base.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_peru_base.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_peru_base.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_peru_base.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_peru_base.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_peru_base.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_peru_base.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_peru_base.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "erpnext_peru_base.event.get_events"
# }

