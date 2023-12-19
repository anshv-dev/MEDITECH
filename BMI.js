function cal()
{
    
 var w=document.getElementById('weight').value;
 var h=document.getElementById('height').value;

 var result=(w/(h*h)).toFixed(3);
 document.getElementById('res').value=result; 

if(result<18.5){
    document.getElementById('range').innerHTML="Underweight";
    document.getElementById('range').style.color="red";
    document.getElementById('range').style.fontWeight="bold";
}
else if(18.5<=result && result<25){
    document.getElementById('range').innerHTML="Healthy"
    document.getElementById('range').style.color="Green";
    document.getElementById('range').style.fontWeight="bold";
}
else if(25<=result && result<30){
    document.getElementById('range').innerHTML="Overweight";
    document.getElementById('range').style.color="Red";
    document.getElementById('range').style.fontWeight="bold";
}
else if(result>30) {
    document.getElementById('range').innerHTML="obesity";
    document.getElementById('range').style.color="red";
    document.getElementById('range').style.fontWeight="bold";
}
else
{
    document.getElementById('range').innerhtml="wrong data";
}
}
