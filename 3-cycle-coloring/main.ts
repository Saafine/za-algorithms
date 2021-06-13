import { addLeftPadding, numToBinary, prettyPrint } from './helpers';

export function run3cycleColoring(input: number[], stage = 1, isFound?: any, shouldStop?: any, shouldPrint = true): void {
  const binaries: string[] = input.map(numToBinary).map(addLeftPadding);
  const { kValues, bits } = getKwithBit(binaries);
  const cValues = getCValues(kValues, bits);

  shouldPrint && prettyPrint({ binaries, kValues, bits, cValues, stage, input });

  if (isFound && isFound({stage, cValues})) {
    throw Error('Found')
  }
  if (shouldStop && shouldStop({stage, cValues})) return;

  if (!isInputReduced(cValues)) {
    runForK(cValues);
  } else {
    run3cycleColoring(cValues, stage + 1, isFound, shouldStop, shouldPrint);
  }
}

function runForK(cValues: number[], k = 5) {
  const cValuesReduced = [];

  for (let x = 0; x < cValues.length; x++) {
    const c = cValues[x];
    if (c !== k) {
      cValuesReduced.push(c);
    } else {
      const options = [0, 1, 2, 3, 4];
      const topNeighbour =
        cValues[x - 1] !== undefined
          ? cValues[x - 1]
          : cValues[cValues.length - 1]; // top or last
      const bottomNeighbour =
        cValues[x + 1] !== undefined ? cValues[x + 1] : cValues[0]; // bottom or first
      const minNeighbour = options.find(
        option => option !== topNeighbour && option !== bottomNeighbour
      );
      cValuesReduced.push(minNeighbour);
    }
  }

  // console.log('k', k);
  // console.log(cValuesReduced);

  if (k === 3) {
    // console.log('Done');
  } else {
    runForK(cValuesReduced, k - 1);
  }
}

function getKwithBit(binary: string[]): { kValues: number[]; bits: number[] } {
  const kValues: number[] = [];
  const bits: number[] = [];

  const binaryLength = binary[0].length;

  for (let x = 0; x < binary.length; x++) {
    const current = binary[x];
    const next = binary[x + 1] !== undefined ? binary[x + 1] : binary[0];
    let k = 0;

    for (let bitIndex = binaryLength - 1; bitIndex >= 0; bitIndex--) {
      const currentBit = current[bitIndex];
      const nextBit = next[bitIndex];
      if (currentBit === nextBit) {
        k++;
      } else {
        kValues.push(k);
        bits.push(Number(currentBit));
        break;
      }
    }
  }

  return { kValues: kValues, bits };
}

function getCValues(kValues: number[], bits: number[]): number[] {
  return kValues.map((k, index) => k * 2 + bits[index]);
}

function isInputReduced(cValues: number[]): boolean {
  return cValues.some(c => c > 5);
}
