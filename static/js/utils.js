window.utils = {

    // Asynchronously load templates located in separate .html files
    loadTemplate: function(view_names, callback) {

        var deferreds = [];

        $.each(view_names, function(index, view_name) {
            if (window.views && window.views[view_name]) {
                deferreds.push($.get('/html/tpl/' + view_name + '.html', function(data) {
                    window.views[view_name].prototype.template = data;
                }));
            } else {
                console.log(view_name + " not found");
            }
        });

        $.when.apply(null, deferreds).done(callback);
    }
} 
