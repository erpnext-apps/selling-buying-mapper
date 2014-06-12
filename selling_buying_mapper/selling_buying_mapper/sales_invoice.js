// Copyright (c) 2014, Contributors
// License: See license.txt

frappe.provide("selling_buying_mapper");

frappe.ui.form.on("Sales Invoice", "refresh", function(frm) {
	if (frm.doc.docstatus === 0) {
		frm.add_custom_button(__("From Purchase Invoice"),
			function() { selling_buying_mapper.from_purchase_invoice(frm); });
	}
});

selling_buying_mapper.from_purchase_invoice = function(frm) {
	frappe.model.map_current_doc({
		method: "selling_buying_mapper.selling_buying_mapper.buying.make_sales_invoice",
		source_doctype: "Purchase Invoice",
		get_query_filters: {
			docstatus: 1,
			company: frm.doc.company
		}
	});
}
