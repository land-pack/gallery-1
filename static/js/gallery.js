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
        this.list = new window.views.ImageListItem();
        $("#content").html(this.list.el);
    },

    imageDetail: function (ticketid)
    {
    }
});

utils.loadTemplate(['ImageList', 'ImageListItem', 'HeaderView'], function () {
    app = new Router();
    Backbone.history.start();
});
