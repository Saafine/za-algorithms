import { run3cycleColoring } from './main';

describe('3 cycle', () => {
    it('should find result', () => {
        const compareCvalues = (cValues: number[]) => cValues[0] === 1 && cValues[1] === 0 && cValues[2] === 2 && cValues[3] === 5;
        const isFound = ({ stage, cValues }) => stage === 2 && compareCvalues(cValues);
        const shouldStop = ({ stage, cValues }) => stage === 2;

        const multiplier = 100
        for (let x = 0; x < multiplier; x++) {
            for (let y = 0; y < multiplier; y++) {
                for (let z = 0; z < multiplier; z++) {
                    for (let w = 0; w < multiplier; w++) {
                        try {
                            run3cycleColoring([x, y, z, w], 1, isFound, shouldStop, false);
                        } catch (e) {
                            console.log(x, y, z, w);
                            return;
                        }
                    }
                }
            }

        }
    });

    it('should run', () => {
        run3cycleColoring([ 2, 0, 1, 10]);
    })
});
