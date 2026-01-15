function reverseIntegerBrute(x) {
  const sign = x < 0 ? -1 : 1;
  const rev = parseInt(Math.abs(x).toString().split('').reverse().join('')) * sign;
  if (rev < -(2**31) || rev > 2**31 - 1) return 0;
  return rev;
}

// edge cases:
// Negative numbers (-123 → -321)
// Numbers ending with zero (120 → 21)
// Overflow (1534236469 → 0)
// Zero (0 → 0)
