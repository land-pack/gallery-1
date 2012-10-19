window.views = window.views || {}

window.views.TagListItem = Backbone.View.extend({
    tagName: 'div',

    initialize: function () {
        this.model.bind("change", this.render, this);
        this.model.bind("destroy", this.close, this);
    },

    render: function () {
        var html = Mustache.to_html(this.template, this.model.toJSON());
        $(this.el).html(html); 
        return this;
    },

    close: function () {
        $(this.el).unbind();
        $(this.el).remove();
    }

});

window.views.TagListPage = Backbone.View.extend({
    tagName: 'div',

    initialize: function () {
        this.model.bind("reset", this.render, this);
        var self = this;
        this.model.bind("add", function (tag) {
            $(self.el).append(new views.ImageListItem({model: tag}).render().el);
        });
        this.initRender();
        this.render();
    },
    
    initRender: function () {
        $(this.el).html("<ul class='unstyled'></ul");
        $(this.el).addClass("well tagPageMain");
    },

    render: function () {
        
        var self = this;
        var el_ul = this.$("ul"); 
        _.each(this.model.models, function (tag) {
            var tagItem = new views.TagListItem({model: tag});
            var html = tagItem.render().el;
            el_ul.append(html);
        }, this);
        $("#content").html(self.el);

        return this;
    },

    close: function () {
        $(this.el).unbind();
        $(this.el).remove();
    }


});

window.views.TagListImagePopup = Backbone.View.extend({
    tagName: 'div',

    initialize: function () {
        this.render();
        this.el = $(this.template);
    },

    render: function () {
                
        //var self = this;
        //var el_ul = this.$("ul"); 
        //_.each(this.model.models, function (tag) {
        //    var tagItem = new views.TagListItem({model: tag});
        //    var html = tagItem.render().el;
        //    el_ul.append(html);
        //}, this);
        //$("#content").html(self.el);

        return this;
    },

    close: function () {
        $(this.el).unbind();
        $(this.el).remove();
    }


});
