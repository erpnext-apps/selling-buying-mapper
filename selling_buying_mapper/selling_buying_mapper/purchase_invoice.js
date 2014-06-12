// Copyright (c) 2014, Contributors
// License: See license.txt

frappe.provide("selling_buying_mapper");

frappe.ui.form.on("Purchase Invoice", "refresh", function(frm) {
	if (frm.doc.docstatus === 1) {
		frm.add_custom_button(__("Make Sales Invoice"),
			function() { selling_buying_mapper.make_sales_invoice(frm); });
	}
});

selling_buying_mapper.make_sales_invoice = function(frm) {
	frappe.model.open_mapped_doc({
		method: "selling_buying_mapper.selling_buying_mapper.buying.make_sales_invoice",
		frm: frm
	});
}
