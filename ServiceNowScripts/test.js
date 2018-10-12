(function executeRule(current, previous /*null when async*/) {
	

	// Create a GlideRecord Object for the table Slow Queries
	var myObj = new GlideRecord('sys_query_pattern');

	// Query the database to get all the records
	myObj.query();
	
	// Display the total number of records received
	gs.addInfoMessage("Number of records in table  are "+myObj.getRowCount()+"\n");
	
	// Declare the variables
	var fields_arr =[]; // Array to store the fields
	var fields_obj = {}; // Object to store the fields and the number of occurences
	var field_ans; // Variable to store the field from the query
	
	var i =0; // For counting
	
	// Loop through the records
	while(myObj.next()){	
		
		// Get the value of the example query
		var example_query = myObj.getValue('example');
		
		// Create the regex variable to get the req query
		var patt = /task[0-9]\.`assignment_group+` +IN +(\()?('[^']+'[,\s]*)+(\))?/gi;
		
		// Create a regex variable to get the field
		var field_patt = /`[^`]+`/gi;
		
		// Test if the req string is present in the query
		var ans = patt.test(example_query);
		
		if(ans != false){ // Check if the string is present or not
			i +=1;// Increment the counter that stores the number of queries with the string
			
			gs.log(i+". example field is: "+example_query);
			gs.log("\n Searching for fields in this query");
			
			// Get all the fields 
			while((field_ans = field_patt.exec(example_query)) != null){ // Loop 
			
				// Remove the backticks 
			    field_ans = field_ans.toString().replace(/`/g,"");
				
			
			   // Store fields in an array
			   fields_arr.push(field_ans);

		}
			
			// Sort the array
			fields_arr =fields_arr.sort();
			
			// Iterate through the array
			for(k=0; k<fields_arr.length; k++){
				fields_obj[fields_arr[k]] = null ? (fields_obj[fields_arr[k]] = 1) : (fields_obj[fields_arr[k]] +1);
				
			}
			
			gs.info("Fields are:"+Object.keys(fields_obj));

			
		}
			
	}
	gs.addInfoMessage("No of Record found are "+i);
	

})(current, previous);