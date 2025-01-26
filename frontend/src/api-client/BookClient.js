export async function getBooks() {
  const response = await fetch("http://localhost:5000/books", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  const result = await response.json();
  console.log("Success:", result);
  return result;
}

export async function getBookById(bookId) {
  const response = await fetch(`http://localhost:5000/book/${bookId}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  const result = await response.json();
  console.log("Success:", result);
  return result;
}

export async function addBook(book) {
  const response = await fetch("http://localhost:5000/book", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(book),
  });

  const result = await response.text();
  console.log("Success:", result);
}

export async function updateBook(bookId, update) {
  const response = await fetch(`http://localhost:5000/book/${bookId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(update),
  });

  const result = await response.text();
  console.log("Success:", result);
}

export async function deleteBook(bookId) {
  const response = await fetch(`http://localhost:5000/book/${bookId}`, {
    method: "DELETE",
  });

  const result = await response.text();
  console.log("Success:", result);
}
