odoo.define('ks_curved_backend_theme_enter.ks_activity_controller', function(require) {
    "use strict";
    const ks_ActivityController = require('mail.ActivityController');
    const core = require('web.core');
    const BasicView = require('web.BasicView');

    ks_ActivityController.include({
        events: _.extend({}, ks_ActivityController.prototype.events, {
            "click button.reload_view": "_KsReloadView",
        }),

        _KsReloadView: function() {
            this.reload();
        },

});
});