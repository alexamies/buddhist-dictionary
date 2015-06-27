// Code for Bootstrap popover

$(function () {
  var popoverElem = $('.dict-entry').popover({
    trigger: 'click',
    html: true,
    content: "placeholder",
    template: '<div class="popover" role="tooltip">' +
              '  <div class="arrow"></div>' +
              '  <div class="btn-group btn-group-xs pull-right" role="group">' +
              '    <button class="btn btn-default popover-dismiss" type="button">&times;</button>' +
              '  </div>' +
              '  <div><h3 class="popover-title"></h3>' +
              '  </div>' +
              '  <div class="popover-content"></div>' +
              '</div>',
  }).on('show.bs.popover', function() {
    //console.log("Got click: this: " + this);
    var text = "";
    var title = "";
    if (this.hasAttribute('word_id')) {
      var word_id = this.getAttribute('word_id');
      word_entry = words[word_id]
      text = '<p>' +  word_entry['pinyin'] + 
             '<br/>' + word_entry['english'] + '<br/>' + word_entry['notes'] + '</p>';
    } else if (this.hasAttribute('phrase_id')) {
      var phrase_id = this.getAttribute('phrase_id');
      phrase_entry = phrases[phrase_id]
      text = '<p>' +  phrase_entry['gloss'] + '</p>';
    }
    //console.log("title: " + title);
    popoverElem.attr('data-content', text);
  }).on('shown.bs.popover', function () {
    var $popup = $(this);
    $(this).next('.popover').find('button.popover-dismiss').click(function (e) {
        $popup.popover('hide');
    });
  });
});
