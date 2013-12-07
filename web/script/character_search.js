// Functions for character lookup

/** 
 * Binds the AJAX search function to the form.
 */
function bindForm() {
    $('searchForm').observe('submit', function(e) {
        e.stop();
        var valid = ($F('character') && ($F('character').strip().length > 0));
        if (valid) {
            new Ajax.Updater('results', this.action, {
        	    method: 'post', parameters: this.serialize()
            });
        } else {
        	alert('Please enter a character to search for.');
        }
    });
}

document.observe('dom:loaded', bindForm);

/*
 * Shows a 'searching ...' message while the ajax script is retrieving results.
 */
Ajax.Responders.register({
    onCreate: function() {
        $('searching').show();
        $('searchButton').disable();
    },
    onComplete: function() {
        if (0 == Ajax.activeRequestCount) {
            $('searching').hide();
            $('searchButton').enable();
        }
    }
});