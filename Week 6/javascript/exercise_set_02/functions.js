function calc(){
  // This gets the values input by the user with
  // the "val" method. We are using the IDs (unique
  // per page) to ensure we are getting the desired
  // data.
  //
  // By default, we get strings back. Need to convert to
  // numbers
  let number1 = parseFloat($('#num1').val());
  let number2 = parseFloat($('#num2').val());
  let operation = $('#operation').val();

  msg = `We have been asked to calculate ${number1} ${operation} ${number2}`
  console.log(msg);

  let answer = 0;

  // Semi TODO: get the right answer for the appropriate operation.
  if (operation == 'add'){
    answer = number1 + number2
  } else if (operation == 'power'){
    answer = Math.pow(number1, number2)
  } else if (operation == 'subtract'){
    answer = number1 - number2
  } else if (operation == 'multiply'){
    answer = number1 * number2
  } else if (operation == 'divide'){
    answer = number1 / number2
  } else {
      answer = 'unknown operation';
  }
  //TODO: Complete the function for the other operations

  //TODO: Write the answer to the appropriate span
  $('span').html(answer);
}
