$(document).ready(function() {
	$("form").ready(function() {
		environmentService.getEnvironments();
		testRequestService.getTemplates();
		testRequestService.getTestRunners();
	});
	$("table").ready(function() {
		testRequestService.getTestRequests();
	});
	$("button").click(function(){
		testRequestService.runTestRequest();
	});
});