//Team TopherAcademy: Andy, Victor, Mark, Anastasia
//Softdev pd0
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

var fact = function(n) {
    if (n == 1) {
        return(1);
    }  
    return n * fact(n-1);
} 

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)


//-----------------------------------------------------------------


//fib:

var fib = function(n) {
    if (n <= 1) {
        return(n);
    }  
    return fib(n-1) + fib(n-2);
} 

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

//=================================================================
