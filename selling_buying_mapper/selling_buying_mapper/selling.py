# Copyright (c) 2014, Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_purchase_order(source_name, target_doc=None):
	"""
		Requirements
		- sales_order field should exist in Purchase Order form
	"""

	def _update_item(source_child, target_child, source_parent):
		target_child.conversion_factor = 1

	target_doc = get_mapped_doc("Sales Order", source_name, {
		"Sales Order": {
			"doctype": "Purchase Order",
			"field_map": {
				"name": "sales_order"
			},
			"field_no_map": ["address_display", "contact_display", "contact_mobile", "in_words",
				"contact_email", "net_total", "conversion_rate", "contact_person", "grand_total"],
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"Sales Order Item": {
			"doctype": "Purchase Order Item",
			"field_map": {
				"stock_uom": "uom"
			},
			"field_no_map": ["rate", "base_rate", "price_list_rate", "base_price_list_rate", "base_amount"],
			"postprocess": _update_item
		}
	}, target_doc)

	target_doc.run_method("set_missing_values")
	target_doc.run_method("get_schedule_dates")

	return target_doc

