const display = document.getElementById('display');
let currentInput = '';
let firstOperand = null;
let operator = null;

function appendToDisplay(value) {
  currentInput += value;
  display.value = currentInput;
}

function clearDisplay() {
  currentInput = '';
  firstOperand = null;
  operator = null;
  display.value = '0';
}

function setOperator(op) {
  if (currentInput !== '') {
    if (firstOperand === null) {
      firstOperand = parseFloat(currentInput);
    } else {
      calculate();
    }
    operator = op;
    currentInput = '';
  }
}

function calculate() {
  if (operator && currentInput !== '') {
    const secondOperand = parseFloat(currentInput);
    let result;

    switch (operator) {
      case '+':
        result = firstOperand + secondOperand;
        break;
      case '-':
        result = firstOperand - secondOperand;
        break;
      case '*':
        result = firstOperand * secondOperand;
        break;
      case '/':
        result = firstOperand / secondOperand;
        break;
    }

    display.value = result;
    currentInput = result.toString();
    firstOperand = result;
    operator = null;
  }
}
