function generateName(){
    var amount = document.getElementById("amount").value;
    var amount=parseInt(amount);
    var cost=(amount*10/100);
    if ( amount >= 0) {
        document.getElementById("result").innerHTML = "Pay " + cost + "via payal or via mpesa and submit transaction id in next form";
        }
    else{
    document.getElementById("result").innerHTML = "Invalid amount";   

        }
}