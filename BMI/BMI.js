function cal()
{
    
 var w=document.getElementById('weight').value;
 var h=document.getElementById('height').value;

 var result=(w/(h*h)).toFixed(1);
 document.getElementById('res').value=result; 

if(result<18.5){
    document.getElementById('range').innerHTML="Underweight";
}
else if(18.5<=result && result<25){
    document.getElementById('range').innerHTML="Healthy";
}
else if(25<=result && result<30){
    document.getElementById('range').innerHTML="Overweight";
}
else if(result>30) {
    document.getElementById('range').innerHTML="obesity";
}
else
{
    document.getElementById('range').innerhtml="wrong data";
}
}
