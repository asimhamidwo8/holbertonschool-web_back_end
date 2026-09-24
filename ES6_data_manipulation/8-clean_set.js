function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  const values = [];

  set.forEach((value) => {
    if (typeof value === 'string' && value.startsWith(startString)) {
      values.push(value.slice(startString.length));
    }
  });

  return values.join('-');
}

export default cleanSet;

