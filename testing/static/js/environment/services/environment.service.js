var environmentService = {

	getEnvironments: function() {
		$.get("/rest-api/environment", function(data, status){
	        if(status == "success") {
	        	$.each(data, function(k, template) {
	        		 $('#environment').append($('<option>', { 
	        		        value: template.id,
	        		        text : template.id 
	        		 }));
	        	})
	        }
	    });
	}
}