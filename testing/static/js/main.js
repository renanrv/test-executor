$(document).ready(function() {
	$("table").ready(function() {
		testRequestService.getTestRequests();
	});
	$("button").click(function(){
		testRequestService.runTestRequest();
	});
});