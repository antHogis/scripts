#!/usr/bin/node

let expression = '';

for (arg of process.argv.slice(2)) {
    console.log(arg)
    expression += arg;
}

console.log('expr:' + expression)

if (expression) {
    evaluateAndPrint(expression)
} else {
    promptExpressions(readLine)
}

function evaluateAndPrint(expression) {
    console.log(eval(expression));
}

function promptExpressions() {
    readLine.question('math> ', (answer) => {
        if (answer != 'q') {
            evaluateAndPrint(answer);
            promptExpressions();
        } else {
            readLine.close();
        }
    })
}