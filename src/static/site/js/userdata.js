var udata;

$.ajax({
    'async': false,
    'type': "GET",
    'global': false,
    'dataType': 'json',
    'url': "/userdata/",
    'data': { 'request': "", 'target': 'arrange_url', 'method': 'method_target' },
    'success': function (data) {
        udata = data;
    }
});


document.getElementById("name").innerHTML=udata["name"];
document.getElementById("registration_no").innerHTML=udata["registration_no"];
document.getElementById("college").innerHTML=udata["college"];
document.getElementById("email").innerHTML=udata["email"];
document.getElementById("test_date").innerHTML=udata["test_date"];
document.getElementById("valid_till").innerHTML=udata["valid_till"];
document.getElementById("overall").innerHTML=udata["overall_percentile"]|0;
document.getElementById("aptus").innerHTML=udata["aptus_percentile"]|0;
document.getElementById("latus").innerHTML=udata["latus_percentile"]|0;
document.getElementById("tekhne").innerHTML=udata["tekhne_percentile"]|0;
document.getElementById("personalis").innerHTML=udata["personalis_code"];


