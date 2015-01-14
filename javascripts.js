for (var counter = 0; counter < 20; counter++) {  //a for loop requires two semicolons
  if (counter % 4 == 0)
    print(counter);
  else
    print("(" + counter + ")");
}


var answer = prompt("What is the value of 2 + 2?", "");
if (answer == "4")
  alert("You rock!");
else if (answer == "3" || answer == "5")
  alert("Almost!");
else
  alert("You're a tard...");
  
  
for (var current = 20; ; current++) {  //no counter boundary, because function returns first number divisible by 7
  if (current % 7 == 0)
    break;
}
print(current);


for (var current = 20; current % 7 != 0; current++) //this one produces result same as a above, but w/o a break
  ; //an empty statement
print(current);


var answer = prompt("You! What is the value of 2 + 2?", "");
while(true)
  if (answer == "4")
    alert("You must be a genius or something.");
    break;
  else
    prompt("You! What is the value of 2 + 2?", "");
