# Copyright (c) 2014, Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_sales_invoice(source_name, target_doc=None):

	target_doc = get_mapped_doc("Purchase Invoice", source_name, {
		"Purchase Invoice": {
			"doctype": "Sales Invoice",
			"field_no_map": ["address_display", "contact_display", "contact_mobile", "in_words",
				"contact_email", "net_total", "conversion_rate", "contact_person", "grand_total",
				"mode_of_payment", "due_date", "posting_date", "aging_date", "cost_center", "is_opening"],
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"Purchase Invoice Item": {
			"doctype": "Sales Invoice Item",
			"field_no_map": ["rate", "base_rate", "price_list_rate", "base_price_list_rate", "base_amount", "amount"]
		}
	}, target_doc)

	target_doc.is_pos = 0
	target_doc.run_method("set_missing_values")

	return target_doc
