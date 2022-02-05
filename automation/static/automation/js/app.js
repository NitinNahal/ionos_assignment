
  /* ---------- Main Menu Open/Close, Min/Full ---------- */
  $('.navbar-toggler').click(function(){

    if ($(this).hasClass('sidebar-toggler')) {
      $('body').toggleClass('sidebar-hidden');
      resizeBroadcast();
    }

    if ($(this).hasClass('sidebar-minimizer')) {
      $('body').toggleClass('sidebar-hidden');
      resizeBroadcast();
    }

    if ($(this).hasClass('aside-menu-toggler')) {
      $('body').toggleClass('aside-menu-hidden');
      resizeBroadcast();
    }

    if ($(this).hasClass('mobile-sidebar-toggler')) {
      $('body').toggleClass('sidebar-mobile-show');
      resizeBroadcast();
    }

  });

// circle node in tree view
	//$("#tree-circle").load({% url 'cc_tool:test' %});

  //chart
    var ctx = document.getElementById("main-chart").getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});


// data table

$(document).ready(function() {

} );

/* user session check */
function user_session(csrf_token, url_data_session,url_update_data_session, node,node_id,mgw_id,toReCheck){
    var session_data = (function () { var json = null;
    $.ajax({'async': false,'global': false,'url': url_data_session,'data' : {node_id : node_id, mgw_id :mgw_id}, 'dataType': "json",'success': function (data) {json = data;}});
    return json;})();
    if(session_data == "" || session_data == "null" || toReCheck == true){
        $.post(url_update_data_session, {csrfmiddlewaretoken: csrf_token, node: node, nodeid: node_id, mgw_id : mgw_id, toReCheck : toReCheck}, function(data){
            $("#myModal").html(data);
            $("#myModal").modal();
        });
        return ''
    }else{
        return session_data
    }
}