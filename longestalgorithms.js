function findLongestWordLength(str) {
  var words = str.split(' ')
  var max = 0;
  

  for(var i = 0; i < words.length; i++){
    if(words[i].length > max ){
      max = words[i].length
    }
  }
  return max;
}

findLongestWordLength("The quick brown fox jumped over the lazy dog");