window.models = window.models || {}

window.models.ImageListItem = Backbone.Model.extend();

window.models.ImageList = Backbone.Collection.extend({
    model: window.models.ImageListItem,
    url: '/json/images'
});
