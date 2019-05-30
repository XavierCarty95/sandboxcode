function truncateString(str, num) {
  // Clear out that junk in your trunk\
  var join; 
  if (str.length > num && num > 3) {
    
    join = str.slice(0, num - -1).trim() + '...';
    return join 
    
  } else if (str.length > num && num <= 3) {
    return str.slice(0, num) + '...';
  } else {
        return str;
  }

}
var res = truncateString("Peter Piper picked a peck of pickled peppers", 11);
console.log(res)
