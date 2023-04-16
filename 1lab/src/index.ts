const bootstrap = () => {
  const f1 = (sigma: number) => 2 * Math.sin(sigma);
  const f2 = (sigma: number) => sigma;

  const coords: Array<Object> = [];
  for (let i = 0; i < 500; i++) {
    const sigma = Math.random();
    const x = Math.random() * 1.895;
    const y = f1(x) + (f2(x) - f1(x)) * sigma;
    coords.push({ x, y });
  }

  console.log(coords);
};

bootstrap();
