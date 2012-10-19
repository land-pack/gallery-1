window.views = window.views || {}

window.views.ImageListItem = Backbone.View.extend({
    tagName: 'div',
    initialize: function () {
        this.model.bind("change", this.render, this);
        this.model.bind("destroy", this.close, this);
    },

    render: function () {
        $(this.el).attr("class", "thumb");
        var html = Mustache.to_html(this.template, this.model.toJSON());
        $(this.el).html(html); 
        var thumb_width = this.model.get('thumb_width');
        var thumb_height = this.model.get('thumb_height');
        $(this.el).css("width", thumb_width);
        $(this.el).css("height", thumb_height);
        return this;
    },

    close: function () {
        $(this.el).unbind();
        $(this.el).remove();
    }
});

window.views.ImageList = Backbone.View.extend({
    initialize: function () {
        this.model.bind("reset", this.render, this);
        var self = this;
        this.model.bind("add", function (img) {
            $(self.el).append(new views.ImageListItem({model: img}).render().el);
        });
        this.render();
    },

    render: function (eventName) {
        var self = this;
        _.each(this.model.models, function (img) {
            var imgItem = new views.ImageListItem({model: img});
            var html = imgItem.render().el;
            $(self.el).append(html);
        }, this);
        $("#content").html(self.el);
        $(self.el).isotope({ layoutMode : 'fitRows' });
        return this;
    }

});
