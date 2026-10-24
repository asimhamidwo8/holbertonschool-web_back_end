import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      reject(err);
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const fields = {};
    lines.slice(1).forEach((line) => {
      const parts = line.split(',');
      const firstname = parts[0].trim();
      const field = parts[parts.length - 1].trim();
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });
    resolve(fields);
  });
});

export default readDatabase;
