// 	Reverse a String ("hello" → "olleh")

function reverseStringBrute(s) {
  let rev = "";
  for (let i = s.length - 1; i >= 0; i--) {
    rev += s[i];
  }
  return rev;
}

console.log(reverseStringBrute('saturday'))
console.log(reverseStringBrute(['s','a','t','u']))

// Time Complexity: O(n²); Space Complexity: O(n)

// | Step                            | Operation                                                           | Complexity  |
// | ------------------------------- | ------------------------------------------------------------------- | ----------- |
// | Loop through string once        | O(n) iterations                                                     | O(n)        |
// | String concatenation (per char) | O(n) (since string is immutable, each append copies previous chars) | O(n²) total |
// | Extra space for reversed string | Stores n characters                                                 | O(n)        |

// String concatenation (per char) - O(n²) total
// Strings in Python, JavaScript, Java, etc. are immutable, meaning they cannot be modified in place.
// Every time you concatenate:A new string is created
// All previous characters are copied over.Plus the new character is appended.
