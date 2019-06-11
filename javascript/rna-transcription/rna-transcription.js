function toRna(dnaStrand) {
  const rnaToDna = {
    G: 'C', C: 'G', T: 'A', A: 'U',
  };
  return dnaStrand.split('').map((x) => {
    if (rnaToDna[x] !== undefined) {
      return rnaToDna[x];
    }
    throw new Error('Invalid input DNA.');
  }).join('');
}

export { toRna };
