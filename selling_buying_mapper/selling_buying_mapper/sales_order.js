// Copyright (c) 2014, Contributors
// License: See license.txt

frappe.provide("selling_buying_mapper");

frappe.ui.form.on("Sales Order", "refresh", function(frm) {
	if (frm.doc.docstatus === 1) {
		frm.add_custom_button(__("Make Purchase Order"),
			function() { selling_buying_mapper.make_purchase_order(frm); });
	}
});

selling_buying_mapper.make_purchase_order = function(frm) {
	frappe.model.open_mapped_doc({
		method: "selling_buying_mapper.selling_buying_mapper.selling.make_purchase_order",
		frm: frm
	});
}
