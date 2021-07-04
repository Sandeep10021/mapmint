/*
    splitWords - a jQuery plugin which splits words into 2 spans.
    @author    John Hunter
    created    2011-03-01
*/
(function($) {

    $.fn.splitWords = function(index) {
        /*
            If index is specified the sentence will split at that point 
            (minus index counts from end). Otherwise sentence is split in two.
        */

        return this.each(function() {

            var el = $(this),
                i, first, words = el.text().split(/\s/);


            if (typeof index === 'number') {
                i = (index > 0) ? index : words.length + index;
            }
            else {
                i = Math.floor(words.length / 2);
            }

            first = words.splice(0, i);

            el.empty().
                append(makeWrapElem(1, first)).
                append(makeWrapElem(2, words));
        });
    };

    function makeWrapElem(i, wordList) {
        return $('<span class="wrap-' + i + '">' + wordList.join(' ') + ' </span>');
    }

}(jQuery));
