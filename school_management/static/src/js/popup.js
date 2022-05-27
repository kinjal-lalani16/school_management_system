odoo.define('school_management.popup', function (require) {
"use strict";

    var rpc = require("web.rpc");

    $(document).ready(function() {
        $(".edit").click(function(event) {
        $("#des_pop_up").modal("show");
        console.log('hiiiii')
    };
