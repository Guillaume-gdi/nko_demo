/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.PauseSubPortal = publicWidget.Widget.extend({
    selector: '.pause_sub_button',
    events: Object.assign({}, {
        'click': '_pauseSub',
    }),

    init: function (parent, options) {
        this.orm = this.bindService("orm");
        this._super.apply(this, arguments);
    },
    _pauseSub: async function (ev) {
        const res = await rpc('/nko_demo/pause_sub/' + this.el.dataset.id);
        console.log("pause sub res", res);
        // refresh the page (maybe something better can be done)
        window.location.reload();
    },
});
