window.Router = Backbone.Router.extend({
    //TODO add actual code in here

    routes: {
        "": "showList",
        "home": "showList",
        "tag": "showTag",
    },

    initialize:function () {
        this.header = new window.views.HeaderView();
        $("#header").html(this.header.el);
        window.is_touch = 'ontouchstart' in document.documentElement;
    },

    showList: function () 
    {
        this.header.changeFocus("home");
        this.cleanUp();

        this.imgList = new models.ImageList();
        var self = this;
        this.imgList.fetch({
            success: function () {
                self.imgListView = new views.ImageList({model: self.imgList});
            }
        });
    },

    showTag: function () {
        this.header.changeFocus("tag");
        this.cleanUp();

        this.tagList = new models.TagList();
        var self = this;
        this.tagList.fetch({
            success: function () {
                self.tagListViewPage = new views.TagListPage({model: self.tagList});
            }
        });
    },

    cleanUp: function () {
        if (this.imgListView)
            this.imgListView.close();
        if (this.tagListViewPage)
            this.tagListViewPage.close();
    },

    imageDetail: function (ticketid)
    {
    }
});

utils.loadTemplate(['ImageList', 'ImageListItem', 'HeaderView', 'TagListPage',
                        'TagListItem', 'TagListImagePopup'], 
        function () {
            app = new Router();
            Backbone.history.start();
        }
);
