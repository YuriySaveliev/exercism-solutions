export function score(x: number, y: number): number {
  let score = 0;
  const r = Math.sqrt(x * x + y * y );
  
  if (r > 10) {
    score = 0;
  } else if (r > 5 && r <= 10) {
    score = 1;
  } else if (r > 1 && r <= 5) {
    score = 5;
  } else if (r <= 1) {
    score = 10;
  }

  return score;
}
