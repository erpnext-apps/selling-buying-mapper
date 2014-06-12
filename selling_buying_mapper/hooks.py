app_name = "selling_buying_mapper"
app_title = "Selling Buying Mapper"
app_publisher = "Anand Doshi"
app_description = "Maps Sales Order to Purchase Order and Purchase Invoice to Sales Invoice"
app_icon = "icon-resize-horizontal"
app_color = "#95BDD3"
app_email = "anand@frappe.io"
app_url = "https://github.com/anandpdoshi/selling_buying_mapper"
app_version = "0.0.1"
hide_in_installer = True

doctype_js = {
	"Sales Order": "selling_buying_mapper/sales_order.js",
	"Sales Invoice": "selling_buying_mapper/sales_invoice.js",
	"Purchase Order": "selling_buying_mapper/purchase_order.js",
	"Purchase Invoice": "selling_buying_mapper/purchase_invoice.js"
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/selling_buying_mapper/css/selling_buying_mapper.css"
# app_include_js = "/assets/selling_buying_mapper/js/selling_buying_mapper.js"

# include js, css files in header of web template
# web_include_css = "/assets/selling_buying_mapper/css/selling_buying_mapper.css"
# web_include_js = "/assets/selling_buying_mapper/js/selling_buying_mapper.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Installation
# ------------

# before_install = "selling_buying_mapper.install.before_install"
# after_install = "selling_buying_mapper.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "selling_buying_mapper.notifications.get_notification_config"

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
# 		"selling_buying_mapper.tasks.all"
# 	],
# 	"daily": [
# 		"selling_buying_mapper.tasks.daily"
# 	],
# 	"hourly": [
# 		"selling_buying_mapper.tasks.hourly"
# 	],
# 	"weekly": [
# 		"selling_buying_mapper.tasks.weekly"
# 	]
# 	"monthly": [
# 		"selling_buying_mapper.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "selling_buying_mapper.install.before_tests"

