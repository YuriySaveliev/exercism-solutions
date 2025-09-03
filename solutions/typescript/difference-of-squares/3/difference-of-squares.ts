export class Squares {
  constructor(public count: number) {
    this.count = count;
  }

  get sumOfSquares(): number {
    return this.getRange().reduce((acc, cv) => acc + cv ** 2, 0);
  }

  get squareOfSum(): number {
    return this.getRange().reduce((acc, cv) => acc + cv, 0) ** 2;
  }

  get difference(): number {
    return this.squareOfSum - this.sumOfSquares;
  }

  getRange(): number[] {
    return Array.from({length: this.count}, (_, i) => i + 1);
  }
}
