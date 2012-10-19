window.models = window.models || {}

window.models.TagListItem = Backbone.Model.extend();

window.models.TagList = Backbone.Collection.extend({
    model: window.models.TagListItem,
    url: '/json/tags'
});
