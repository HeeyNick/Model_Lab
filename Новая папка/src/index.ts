const N = 120;
const map: Map<Array<number>, Array<number>> = new Map();

const calcStep = (): number => {
  let k = Math.round(Math.log10(N) * 3.322 + 1);

  k = k < 5 ? 5 : k;
  k = k > 15 ? 15 : k;
  return 1 / k;
};

const generateIntervals = (intervals: Map<Array<number>, number>) => {
  const k = calcStep();
  for (let i = 0; i <= 1 - k; i += k) {
    intervals.set([+i.toFixed(2), +(i + k).toFixed(2)], 0);
  }
};

const calcHits = () => {
  const intervals: Map<Array<number>, number> = new Map();

  generateIntervals(intervals);

  for (let i = 0; i < N; i++) {
    const number: number = +Math.random().toFixed(3);

    for (const interval of intervals.keys()) {
      if (interval[0] < number && number <= interval[1]) {
        const intervalCountNumber = intervals.get(interval);

        if (intervalCountNumber !== undefined) {
          intervals.set(interval, intervalCountNumber + 1);
        }
      }
    }
  }

  for (const [interval, count] of intervals.entries()) {
    map.set(interval, [count]);
  }
};

const calcPi = () => {
  for (const [interval, props] of map.entries()) {
    const pi = interval[1] - interval[0];
    props.push(pi);

    map.set(interval, props);
  }
};

const calcNih = () => {
  for (const [interval, props] of map.entries()) {
    const pi = props.at(-1);

    if (pi) {
      props.push(pi * N);
      map.set(interval, props);
    }
  }
};

const calcDiff = () => {
  for (const [interval, props] of map.entries()) {
    // const ni = intervals.get(interval);
    const ni = props.at(0);

    if (ni) {
      const ni_h = props.at(-1);

      if (ni_h) {
        const diff = ni - ni_h;
        props.push(diff);
        map.set(interval, props);
      }
    }
  }
};

const calcSqrt = () => {
  for (const [interval, props] of map.entries()) {
    const diff = props.at(-1);

    if (diff) {
      const diff2 = diff ** 2;
      props.push(diff2);

      map.set(interval, props);
    }
  }
};

const calcSqrtDivNih = () => {
  for (const [interval, props] of map.entries()) {
    const ni_h = props.at(-3);
    if (ni_h) {
      const s = props.at(-1);

      if (s) {
        const sqrtDivNiH = s / ni_h;

        props.push(sqrtDivNiH);
        map.set(interval, props);
      }
    }
  }
};

const calcHi = () => {
  let hiSqrt = 0;

  for (const props of map.values()) {
    const hi = props.at(-1);
    if (hi) hiSqrt += hi;
  }

  return hiSqrt;
};

const calcMathWait = () => {
  let mathWait = 0;
  for (const [interval, props] of map.entries()) {
    const ni = props[0];
    mathWait += ni;
  }

  return mathWait / Array.from(map.values()).length;
};

const calcDisp = (mathWait: number) => {
  let disp = 0;
  for (const [interval, props] of map.entries()) {
    disp += Math.pow(props[0] - mathWait, 2);
  }

  return disp / Array.from(map.values()).length;
};

const autocorrelation = () => {
  const t = 2;
  const mathWait = calcMathWait();
  const disp = calcDisp(mathWait);

  let correlation = 0;
  const nis = Array.from(map.values());
  for (let i = 0; i < nis.length - t; i++) {
    correlation +=
      ((nis[i][0] - mathWait) * (nis[i + t][0] - mathWait)) /
      (disp * (nis.length - t));
  }

  return correlation;
};

const hiSqrt = () => {
  calcHits();

  calcPi();
  calcNih();
  calcDiff();
  calcSqrt();
  calcSqrtDivNih();

  const hi = calcHi();

  return hi;
};

const bootstrap = () => {
  const hi = hiSqrt();
  const corr = autocorrelation();

  console.log(map);
  console.log("\nХи-квадрат:", hi, "\nАвтокорреляция: ", corr);
};

bootstrap();
