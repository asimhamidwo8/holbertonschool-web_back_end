function uploadPhoto() {
  return Promise.resolve({
    body: 'photo-profile-1',
  });
}

function createUser() {
  return Promise.resolve({
    firstName: 'Guillaume',
    lastName: 'Salva',
  });
}

export { uploadPhoto, createUser };
