window.Router = Backbone.Router.extend({
    //TODO add actual code in here

    routes: {
        "": "list",
    },

    initialize:function () {
        this.header = new window.views.HeaderView();
        $("#header").html(this.header.el);
    },

    list: function () 
    {
        this.imgList = new models.ImageList();
        var self = this;
        this.imgList.fetch({
            success: function () {
                self.imgListView = new views.ImageList({model: self.imgList});
            }
        });
    },

    imageDetail: function (ticketid)
    {
    }
});

utils.loadTemplate(['ImageList', 'ImageListItem', 'HeaderView'], function () {
    app = new Router();
    Backbone.history.start();
});
