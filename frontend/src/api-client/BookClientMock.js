import uuid4 from "uuid4";

let books = [
  {
    author: "JK Rowling",
    date_published: "2004-10-19T08:23:54+00:00",
    description: "Kid goes to magic school",
    genre: "fantasy",
    id: "75d78c06-f134-4d9c-b1ae-c3e28d312faa",
    rating: "9.2",
    title: "Harry Potter",
  },
  {
    author: "Rick Riordan",
    date_published: "2010-10-19T09:23:54+00:00",
    description: "Kid goes to magic camp",
    genre: "fantasy",
    id: "1561d744-0124-4dbd-b43a-e37bca283c55",
    rating: "9.0",
    title: "Percy Jackson",
  },
  {
    author: "Stephanie Meyer",
    date_published: "2004-10-19T08:23:54+00:00",
    description: "Girls falls in love with vampire",
    genre: "fantasy",
    id: "12e78d1b-f003-4d9f-a71c-1e66b3ed660a",
    rating: "6.0",
    title: "Twilight",
  },
  {
    author: "George Lucas",
    date_published: "2004-10-19T08:23:54+00:00",
    description: "Kid goes on space adventure",
    genre: "sci-fi",
    id: "027be1fa-eaaf-4a25-aa45-dc37a7fd9079",
    rating: "8",
    title: "Star Wars",
  },
];

export async function getBooks() {
  return books;
}

export async function getBookById(bookId) {
  for (let book of books) {
    if (book.id === bookId) {
      return book;
    }
  }
  return null;
}

export async function addBook(book) {
  const newBook = { ...book, id: uuid4() };
  books.push(newBook);
}

export async function updateBook(bookId, update) {
  for (let i = 0; i < books.length; i++) {
    let existing = books[i];

    if (existing.id === bookId) {
      books[i] = { ...existing, ...update };
    }
  }
  return update;
}

export async function deleteBook(bookId) {
  const newArr = [];
  for (let book of books) {
    if (book.id != bookId) {
      newArr.push(book);
    }
  }
  books = newArr;
}
