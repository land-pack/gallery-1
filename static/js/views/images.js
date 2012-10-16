window.views = window.views || {}

window.views.ImageListItem = Backbone.View.extend({

    initialize: function () {
        this.model.bind("change", this.render, this);
        this.model.bind("destroy", this.close, this);
        this.render();
    },

    render: function () {
       $(this.el).html(:wq 
    }
});
