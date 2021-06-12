import { PrintParams } from './model';
import { addLeftPadding, numToBinary, prettyPrint } from './helpers';

export function run3cycleColoring(input: number[], stage = 0): void {
    const binaries: string[] = input.map(numToBinary).map(addLeftPadding);
    const { kValues, bits } = getKwithBit(binaries);
    const cValues = getCValues(kValues, bits);

    prettyPrint({ binaries, kValues, bits, cValues, stage });

    if (isNextNeeded(cValues)) {
        run3cycleColoring(cValues, stage + 1);
    } else {
        console.log('Done');
    }
}

function getKwithBit(binary: string[]): { kValues: number[], bits: number[] } {
    const kValues: number[] = [];
    const bits: number[] = [];

    const binaryLength = binary[0].length;

    for (let x = 0; x < binary.length; x++) {
        const current = binary[x];
        const next = binary[x + 1] || binary[0];
        let k = 0;
        let lastMatchingBit = current[binaryLength - 1];

        for (let bitIndex = binaryLength - 1; bitIndex >= 0; bitIndex--) {
            const currentBit = current[bitIndex];
            const nextBit = next[bitIndex];
            if (currentBit === nextBit) {
                k++;
                lastMatchingBit = currentBit;
            } else {
                kValues.push(k);
                bits.push(Number(lastMatchingBit));
                break;
            }
        }
    }

    return { kValues: kValues, bits };
}

function getCValues(kValues: number[], bits: number[]): number[] {
    return kValues.map((k, index) => k * 2 + bits[index]);
}

function isNextNeeded(cValues: number[]): boolean {
    return cValues.some((c) => c > 5);
}


