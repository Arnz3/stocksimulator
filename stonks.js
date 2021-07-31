var climbingIDK = new Array(true, true, true, true, true);

function update_stonks() {
    var stockValues = document.getElementsByClassName("value");
    for (let i = 0; i < stockValues.length; i++) {
        var incrementer = Math.round(Math.random()*11) /100;
        if (incrementer === 0.11){
            if(climbingIDK[i]){
                climbingIDK[i] = false;
                stockValues[i].style.color = "#ff0000";
            }
            else{
                climbingIDK[i] = true;
                stockValues[i].style.color = "#00ff00";
            }
        }
        else{
            var currentValue = parseInt(stockValues[i].innerHTML);
            if(climbingIDK[i]){
                stockValues[i].innerHTML = currentValue + incrementer;
            }
            else{
                if(currentValue - incrementer < 1){
                    stockValues[i].innerHTML = currentValue + incrementer;
                }
                else{
                    stockValues[i].innerHTML = currentValue - incrementer;
                }
            }
        }
    }
    setTimeout(update_stonks, 2000);
}

update_stonks();