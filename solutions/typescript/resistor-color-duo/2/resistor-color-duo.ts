export enum COLORS {
  black,
  brown,
  red,
  orange,
  yellow,
  green,
  blue,
  violet,
  grey,
  white,
};

type Color = keyof typeof COLORS;

export function decodedValue(colors: Color[]): number {
  return 10 * COLORS[colors[0]] + COLORS[colors[1]];
}
