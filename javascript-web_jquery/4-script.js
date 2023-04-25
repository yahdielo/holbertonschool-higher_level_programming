#!/usr/node


$(document).ready( function() {
    $('#toggle_header').click( function() {
        var class_name = $('header').attr('class');
        if (class_name === 'green') {
            $('header').toggleClass(class_name);
            $('header').addClass('red');
        } else {
            $('header').toggleClass(class_name);
            $('header').addClass('green')
        }
    })
})