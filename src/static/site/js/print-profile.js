function printDiv() {
	var divToPrint=document.getElementById('scorecard');
	var width=parseFloat(divToPrint.getAttribute("width"));
	var height=parseFloat(divToPrint.getAttribute("height"));
	var newWin=window.open('','PrintMap');
	
	$(newWin.document).ready(function() {
		var printDocHead = $('<head></head>').append($('link[rel=stylesheet]').clone());
		console.log(printDocHead);
		var printDocBodyHtml = $(divToPrint).html().replace(/-sm-/g, "-xs-");
		var printDocBody = $('<body></body>').html(printDocBodyHtml);
		console.log(printDocBody);
		var printDoc = $('<html></html>').append(printDocHead).append(printDocBody);
		console.log(printDoc);
		
		newWin.document.write(printDoc[0].outerHTML);
		newWin.document.close();
		newWin.focus();
		setTimeout(function(){
			newWin.print();
			console.log("Print Fired:");
			newWin.close();
		}, 5);
	});
}

function loadPrintCss() {
	$("#printarea").clone().appendTo("#print-me");
	//Apply some styles to hide everything else while printing.
	$("body").addClass("printing");
	//Print the window.
	window.print();
	//Restore the styles.
	$("body").removeClass("printing");
	//Clear up the div.
	$("#print-me").empty();
	}

function genPDF() {
	console.log("Function is called");
	console.log();
	html2canvas(document.getElementById("scorecard"),{
	onrendered: function (canvas) {
		console.log("Inside Function is called");
		var img = canvas.toDataURL();
		window.open(img);
	},
	useCORS: true,
	allowTaint: true
	});
}