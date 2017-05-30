//===> Q4: What si the significance, and whata rebthe benefis of including "use strict" in the begining of a javascript source file?
// -- makes debugging easier
// -- prevents accidental GlobalEventHandlers
// -- eliminates 'this' coercion
// -- disallows duplicate property names or parameter values
// -- makes eval() SVGComponentTransferFunctionElement. There are some diferences in the way eval() behaves in strict mode and non-strict mode.

// ===> Q5: Dcuss possible ways to write a function isInteger(x)
//that determines if x is an integer
// 1.1 

(function() {
    console.log(1); 
    setTimeout(function(){console.log(2)},10); 
    setTimeout(function(){console.log(3)},0); 
    console.log(4);
})();