 document.addEventListener('DOMContentLoaded', function() {
     var options = {
         coverTrigger : false,
         constrainWidth :false,
         alignment : 'right'
     };
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems,options);
  });

var user_id = document.getElementById('current_user').content;
var number_of_notifications_container  = document.getElementById('number_of_notifications');
var generated_notifications_container  = document.getElementById('generated_notif');

// function check_for_new_notifications(user_id,callback){
//     the_url = "127.0.0.1:5000/notification_stream/"+user_id;
//
//     var xmlHttp = new XMLHttpRequest();
//     xmlHttp.onreadystatechange = function() {
//         if (xmlHttp.readyState == 4)
//             callback(xmlHttp.responseText);
//     };
//     xmlHttp.open("GET", the_url, true); // true for asynchronous
//  }
//
//  function update_notification_container(_json_data){
//     console.log(_json_data);
//  }

(function poll() {
   setTimeout(function() {
       $.ajax({ url: "notification_stream/"+user_id, success: function(data) {
           var html_notifs_build = '';
           var count = 0;
           for(var key in data) {
               count ++;
               html_notifs_build = '<li class = "aaa" id='+key+'><p>'+data[key]+'</p></li>' + html_notifs_build;

           }
           generated_notifications_container.innerHTML = html_notifs_build;
           number_of_notifications_container.innerHTML = count;
       }, dataType: "json", complete: poll });
    }, 1000);
})();

function dismiss_notification(){
    var ids = [];
   var everyChild = generated_notifications_container.children;
   for(var i = 0; i <everyChild.length; i++){
       ids.push(everyChild[i].id)
   }

    console.log(ids);

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            console.log(xmlHttp.responseText);
    };
    xmlHttp.open("POST", "/notification_stream/dismiss", false); // true for asynchronous
    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttp.send(JSON.stringify({'ids' : ids}));

    generated_notifications_container.innerHTML = '';
    number_of_notifications_container.innerHTML = 0;
}

// setInterval(check_for_new_notifications(user_id,update_notification_container),1000);
//  setInterval(function(){
//      console.log('pula');
//  },1000);