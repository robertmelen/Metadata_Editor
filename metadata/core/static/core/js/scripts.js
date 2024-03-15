
        htmx.on('#upload-form', 'htmx:xhr:progress', function(evt) {
            var progress = (evt.detail.loaded / evt.detail.total) * 100;
            htmx.find('#prog-bar').setAttribute("style", "width: " + progress + "%");}
        );
        
        // htmx.on('#upload-form', 'htmx:xhr:loadend', function(evt){
        //     if(evt.detail.successful) {
        //         htmx.find('#prog-bar').setAttribute("style", "width:0%");}
        // })
