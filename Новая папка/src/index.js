"use strict";
const N = 120;
const values = new Map();
const intervals = new Map();
const calcStep = () => {
    let k = Math.round(Math.log10(N) * 3.322 + 1);
    k = k < 5 ? 5 : k;
    k = k > 15 ? 15 : k;
    return 1 / k;
};
const k = calcStep();
const generateIntervals = () => {
    for (let i = 0; i < 1 - k; i += k) {
        intervals.set([+i.toFixed(2), +(i + k).toFixed(2)], 0);
    }
};
const generateNumbers = () => {
    for (let i = 0; i < N; i++) {
        const number = +Math.random().toFixed(3);
        for (let interval of intervals.keys()) {
            if (interval[0] < number && number <= interval[1]) {
                const intervalCountNumber = intervals.get(interval);
                if (intervalCountNumber !== undefined) {
                    intervals.set(interval, intervalCountNumber + 1);
                }
            }
        }
    }
};
const Pi2 = new Map();
const calcPi = () => {
    for (let interval of intervals.keys()) {
        // const middle = interval[0] + interval[1] / 2;
        const pi = interval[1] - interval[0];
        Pi2.set(interval, pi);
    }
};
const nih = new Map();
const calcNih = () => {
    for (let [interval, pi] of Pi2.entries()) {
        nih.set(interval, pi * N);
    }
};
const diff = new Map();
const calcDiff = () => {
    for (let [interval, ni_h] of nih.entries()) {
        const ni = intervals.get(interval);
        if (ni)
            diff.set(interval, ni - ni_h);
    }
};
const sqrt = new Map();
const calcSqrt = () => {
    for (let [interval, dif] of diff.entries()) {
        sqrt.set(interval, dif ** 2);
    }
};
const sqrtDivNih = new Map();
const calcSqrtDivNih = () => {
    for (let [interval, s] of sqrt.entries()) {
        const ni_h = nih.get(interval);
        if (ni_h)
            sqrtDivNih.set(interval, s / ni_h);
    }
};
let hiSqrt = 0;
const calcHi = () => {
    for (let hi of sqrtDivNih.values()) {
        hiSqrt += hi;
    }
};
generateIntervals();
generateNumbers();
calcPi();
calcNih();
calcDiff();
calcSqrt();
calcSqrtDivNih();
calcHi();
console.log(intervals, hiSqrt);
