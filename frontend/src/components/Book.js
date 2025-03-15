import { Container, Table, Form, Button } from "react-bootstrap";
import { useState, useEffect } from "react";
import {
  getBooks,
  updateBook,
  deleteBook,
  addBook,
  getBookById,
} from "../api-client/BookClient";

export default function Book() {
  const [booksDisplay, setBooksDisplay] = useState([]);
  const [bookDisplay, setBookDisplay] = useState(renderBookByIdDisplay());
  const createBookDisplay = renderCreateBookDisplay();
  const updateBookDisplay = renderUpdateBookDisplay();
  const deleteBookDisplay = renderDeleteBookDisplay();

  const fetchBooks = async () => {
    const books = await getBooks();
    setBooksDisplay(renderCreateBooksDisplay(books));
  };

  const fetchBook = async (bookId) => {
    const book = await getBookById(bookId);
    setBookDisplay(renderBookByIdDisplay(book));
  };

  const createNewBook = async (book) => {
    await addBook(book);
    fetchBooks();
  };

  const updateExistingBook = async (bookId, update) => {
    await updateBook(bookId, update);
    fetchBooks();
  };

  const deleteExistingBook = async (bookId) => {
    await deleteBook(bookId);
    fetchBooks();
  };

  function renderCreateBooksDisplay(books) {
    const tableBody = books.map((book, index) => {
      let readableDate = null;
      if (book.date_published) {
        readableDate = new Date(book.date_published).toLocaleDateString(
          "en-US",
        );
      }
      return (
        <tr key={`book${book.id}:${index}`}>
          <td>{book.id}</td>
          <td>{book.title}</td>
          <td>{book.author}</td>
          <td>{book.genre}</td>
          <td>{book.description}</td>
          <td>{book.rating}</td>
          <td>{readableDate}</td>
        </tr>
      );
    });
    return (
      <div>
        <h1>Books</h1>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>ID</th>
              <th>Title</th>
              <th>Author</th>
              <th>Genre</th>
              <th>Description</th>
              <th>Rating</th>
              <th>Date Published</th>
            </tr>
          </thead>
          <tbody>{tableBody}</tbody>
        </Table>
      </div>
    );
  }

  useEffect(() => {
    fetchBooks();
  }, []);

  const handleBookByIdSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target),
      formDataObj = Object.fromEntries(formData.entries());
    fetchBook(formDataObj.id);
  };

  const handleCreateBookSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target),
      formDataObj = Object.fromEntries(
        formData.entries().filter(([_, v]) => v != null && v != ""),
      );
    if (formDataObj.rating) {
      formDataObj.rating = parseFloat(formDataObj.rating);
    }
    createNewBook(formDataObj);
  };

  const handleUpdateBookSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target),
      formDataObj = Object.fromEntries(
        formData.entries().filter(([_, v]) => v != null && v != ""),
      );
    const { id, ...update } = formDataObj;
    if (update.rating) {
      update.rating = parseFloat(update.rating);
    }
    updateExistingBook(id, update);
  };

  const handleDeleteBookSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target),
      formDataObj = Object.fromEntries(formData.entries());
    deleteExistingBook(formDataObj.id);
  };

  function renderBookByIdDisplay(book) {
    let tableBody = null;
    if (book != null) {
      let readableDate = null
      if (book.date_published){
        readableDate = new Date(book.date_published).toLocaleDateString(
          "en-US",
        );
      }
      tableBody = (
        <tbody>
          <tr>
            <td>{book.title}</td>
            <td>{book.author}</td>
            <td>{book.genre}</td>
            <td>{book.description}</td>
            <td>{book.rating}</td>
            <td>{readableDate}</td>
          </tr>
        </tbody>
      );
    }
    return (
      <div>
        <h1>Get Book By Id</h1>
        <div>
          <Form onSubmit={(e) => handleBookByIdSubmit(e)}>
            <Form.Group>
              <Form.Label>Book Id</Form.Label>
              <Form.Control type="text" name="id" />
            </Form.Group>
            <Button type="submit">Submit</Button>
          </Form>
        </div>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Title</th>
              <th>Author</th>
              <th>Genre</th>
              <th>Description</th>
              <th>Rating</th>
              <th>Date Published</th>
            </tr>
          </thead>
          {tableBody}
        </Table>
      </div>
    );
  }
  function renderCreateBookDisplay() {
    return (
      <div>
        <h1>Create Book</h1>
        <Form onSubmit={(e) => handleCreateBookSubmit(e)}>
          <Form.Group>
            <Form.Label>Title</Form.Label>
            <Form.Control type="text" name="title" />
            <Form.Label>Author</Form.Label>
            <Form.Control type="text" name="author" />
            <Form.Label>Genre</Form.Label>
            <Form.Control type="text" name="genre" />
            <Form.Label>Description</Form.Label>
            <Form.Control type="text" name="description" />
            <Form.Label>Rating</Form.Label>
            <Form.Control type="text" name="rating" />
            <Form.Label>Date Published</Form.Label>
            <Form.Control type="text" name="date_published" />
          </Form.Group>
          <Button type="submit">Submit</Button>
        </Form>
      </div>
    );
  }

  function renderUpdateBookDisplay() {
    return (
      <div>
        <h1>Update Book</h1>
        <Form onSubmit={(e) => handleUpdateBookSubmit(e)}>
          <Form.Group>
            <Form.Label>Id</Form.Label>
            <Form.Control type="text" name="id" />
            <Form.Label>Title</Form.Label>
            <Form.Control type="text" name="title" />
            <Form.Label>Author</Form.Label>
            <Form.Control type="text" name="author" />
            <Form.Label>Genre</Form.Label>
            <Form.Control type="text" name="genre" />
            <Form.Label>Description</Form.Label>
            <Form.Control type="text" name="description" />
            <Form.Label>Rating</Form.Label>
            <Form.Control type="text" name="rating" />
            <Form.Label>Date Published</Form.Label>
            <Form.Control type="text" name="date_published" />
          </Form.Group>
          <Button type="submit">Submit</Button>
        </Form>
      </div>
    );
  }

  function renderDeleteBookDisplay() {
    return (
      <div>
        <h1>Delete Book</h1>
        <div>
          <Form onSubmit={(e) => handleDeleteBookSubmit(e)}>
            <Form.Group>
              <Form.Label>Book Id</Form.Label>
              <Form.Control type="text" name="id" />
            </Form.Group>
            <Button type="submit">Submit</Button>
          </Form>
        </div>
      </div>
    );
  }
  return (
    <Container>
      {booksDisplay}
      {bookDisplay}
      {createBookDisplay}
      {updateBookDisplay}
      {deleteBookDisplay}
    </Container>
  );
}
