export class Squares {
  count: number;
  
  constructor(count: number) {
    this.count = count;
  }

  get sumOfSquares(): number {
    return this.getRange().reduce((acc, cv) => acc + Math.pow(cv, 2), 0);
  }

  get squareOfSum(): number {
    return Math.pow(this.getRange().reduce((acc, cv) => acc + cv, 0), 2);
  }

  get difference(): number {
    return this.squareOfSum - this.sumOfSquares;
  }

  getRange(): number[] {
    return [...Array(this.count + 1).keys()];
  }
}
