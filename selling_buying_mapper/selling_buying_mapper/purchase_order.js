// Copyright (c) 2014, Contributors
// License: See license.txt

frappe.provide("selling_buying_mapper");

frappe.ui.form.on("Purchase Order", "refresh", function(frm) {
	if (frm.doc.docstatus === 0) {
		frm.add_custom_button(__("From Sales Order"),
			function() { selling_buying_mapper.from_sales_order(frm); });
	}
});

selling_buying_mapper.from_sales_order = function(frm) {
	frappe.model.map_current_doc({
		method: "selling_buying_mapper.selling_buying_mapper.selling.make_purchase_order",
		source_doctype: "Sales Order",
		get_query_filters: {
			docstatus: 1,
			status: ["!=", "Stopped"],
			company: frm.doc.company
		}
	});
}
