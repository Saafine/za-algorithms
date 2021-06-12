import { PrintParams } from './model';

export function numToBinary(num: number): string {
    return (num >>> 0).toString(2);
}

export function addLeftPadding(binary: string, _, source: string[]): string {
    const maxLen = source.reduce((max, current) => max > current.length ? max : current.length, 0);
    return binary.padStart(maxLen, '0');
}

export function prettyPrint({ cValues, binaries, kValues, bits, stage }: PrintParams) {
    console.log('-----------------------------------------------------');
    console.log(` ------------------- ETAP ${stage} ---------------------`);
    console.log('-----------------------------------------------------');
}
