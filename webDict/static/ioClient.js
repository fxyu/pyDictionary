var socket = null

$(document).ready(function () {
    // var url = 'http://localhost';
    var url = window.location.origin;
    var port = '5000';
    // console.log(url + ':' + port)
    console.log(url)
    socket = io.connect(url);
    
    socket.on('connect', function () {
        // socket.emit('connect_event', { data: 'connected!' });
        console.log('Connected! Get History!')
        socket.emit('client_getHistory', null, (json)=>{
            console.log(json)
            $('#histList').empty()
            json.forEach(element => {
                newHistory(element)
            });
        })
    })

    socket.on('server_newWord', function(word, json){
        console.log(json)
        $('#pronouce').attr('src',json.audio)
        $('#pronouce').parent()[0].load()
        $('#title').text(word)
        $("#defin").text(json.yahoo)
        newHistory(word)
    })

    socket.on('server_playAudio', function(){
        $('#pronouce').parent()[0].play()
    })


    socket.on('server_response', function (msg) {
        // $('#log').append('<br>' + $('<div/>').text('Received #' + ': ' + msg.data).html());
    });

    $('#btn_search').click(function(evt){
        var word = $('#tf_word').val()
        searchWord(word)
    })

    $('#tf_word').keydown(function(evt) {
        if (evt.keyCode == 13){
            $('#btn_search').trigger('click')
            $('#tf_word').val('')
        }
    });

}); 

function newHistory(word){
    newli = $('<li>')
        .addClass('list-group-item')
        .text(word)
        .click((evt)=>{
            searchWord(word)
        })
    $('#histList').prepend(newli)
}

function searchWord(word){
    console.log(word)
    // Update History List
    // newHistory(word)
    
    // Emit request to server
    socket.emit('client_searchWord', word, function(json){
        // console.log(json)
        // $('#title').text(word)
        // $("#defin").text(json.yahoo)
    }) 
}