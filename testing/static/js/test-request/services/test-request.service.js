// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var testRequestService = {
	updateTableRowColors: function() {
		$("tr .status").each(function(){
			$this = $(this);
			if($this.html() == "Requested")
				$this.parent().css('background-color','white');
			else if($this.html() == "Succeeded")
				$this.parent().css('background-color','green');
			else if($this.html() == "Failed")
				$this.parent().css('background-color','red');
			
		})
	},

	formatTestRequestRow: function(testRequest) {
		row = "<tr id='" + testRequest.id + "'>" +
			"<td>" + testRequest.id + "</td>" +
			"<td>" + testRequest.requester + "</td>" +
			"<td>" + testRequest.created_on + "</td>" +
			"<td>" + testRequest.environment + "</td>" +
			"<td>" + testRequest.test_runner.name + "</td>" +
			"<td>" + testRequest.template + "</td>" +
			"<td class='status'>" + testRequest.status.name + "</td>" +
			"<td>" + testRequest.log + "</td>" +
			"</tr>";
		return row;
	},
	
	getTestRequests: function() {
		$.get("/rest-api/test-request", function(data, status){
	        if(status == "success") {
	        	$.each(data, function(k, testRequest) {
	        		row = testRequestService.formatTestRequestRow(testRequest);
	        		$("#test-requests-results tr:first").after(row);
	        	})
	        	testRequestService.updateTableRowColors();
	        }
	    });
	},

	getTestRequest: function(testRequestId) {
		$.get("/rest-api/test-request/" + testRequestId + "/log", function(data, status){
	        if(status == "success") {
	        	testRequest = data;
	        	row = testRequestService.formatTestRequestRow(testRequest);
        		$("tr#" + testRequest.id).replaceWith(row);
        		testRequestService.updateTableRowColors();
        		if(testRequest.status.name != "Succeeded" && testRequest.status.name != "Failed")
        			setTimeout(function() {
        				testRequestService.getTestRequest(testRequestId)
        			}, 5000);
	        }
	    });
	},

	runTestRequest: function() {
		data = {
			requester: $("#requester").val(),
			environment: $("#environment").val(),
			test_runner: $("#test-runner").val(),
			template: $("#template").val(),
			custom_path: $("#custom-path").val(),
		};
		$.post("/rest-api/test-request", data, function(data, status){
	        if(status == "success") {
	        	testRequest = data;
	        	row = testRequestService.formatTestRequestRow(testRequest);
	        	$("#test-requests-results tr:first").after(row);
	        	testRequestService.updateTableRowColors();
	        	testRequestService.getTestRequest(testRequest.id);
	        }
	    });
	}
}