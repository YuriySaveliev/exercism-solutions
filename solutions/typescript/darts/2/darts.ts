export function score(x: number, y: number): number {
  const r = Math.sqrt(x * x + y * y);

  if (r > 5 && r <= 10) {
    return  1;
  }
  if (r > 1 && r <= 5) {
    return 5;
  }
  if (r <= 1) {
    return 10;
  }
  
  return 0;
}
