function frankenSplice(arr1, arr2, n) {
  // It's alive. It's alive!
  for(var i = 0; i < arr1.length; i++){
         arr1.slice(0,1)
  }
    arr2.splice(n,0,arr1)
    
    console.log(arr2)
}

frankenSplice([1, 2], ["a", "b"], 1);