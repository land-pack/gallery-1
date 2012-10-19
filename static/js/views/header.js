window.views = window.views || {}

window.views.HeaderView = Backbone.View.extend({

    initialize: function () {
        this.render();
    },

    changeFocus: function (name) {
        this.$("li").removeClass("active");
        this.$("li[ref=" + name + "]").addClass("active");
    },

    render: function () {
        $(this.el).html(this.template);
        return this;
    },
});
