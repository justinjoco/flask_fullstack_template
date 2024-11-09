/*
Items table - Rendered on admin page render
- Row: id, Name, price, count, dateCreated, dateUpdated
- Update or delete from current table (Use button)

Add item
- Admin specified item (name, price, count); submit button

Orders table for all users -> updated after shopping cart has finished or on customer page render
- Row: Order id, item name, amount, date created, total price
<h1>Items</h1>
<Table striped bordered hover>
  <thead>
    <tr>
      <th>#</th>
      <th>First Name</th>
      <th>Last Name</th>
      <th>Username</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <td>3</td>
      <td colSpan={2}>Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</Table>
*/

import { Table, Container, Form, Button, Modal } from "react-bootstrap";
import { useState, useEffect, useRef } from "react";
import { getItems, getItemsMock } from "../api-client/CommonClient";
import {
  getOrders,
  getOrdersMock,
  addItem,
  updateItem,
  deleteItem,
} from "../api-client/AdminClient";

export default function Admin() {
  const [itemDisplay, setItemDisplay] = useState([]);
  const [orderDisplay, setOrderDisplay] = useState([]);
  const itemToUpdateRef = useRef("");
  const [show, setShow] = useState(false);

  const fetchItems = async () => {
    const items = await getItems();

    setItemDisplay(createItemDisplay(items));
  };

  const fetchOrders = async () => {
    const orders = await getOrders();
    setOrderDisplay(createOrderDisplay(orders));
  };

  const createNewItem = async (item) => {
    await addItem(item);
    await fetchItems();
    await fetchOrders();
  };

  const updateSpecificItem = async (itemId, update) => {
    await updateItem(itemId, update);
    await fetchItems();
    await fetchOrders();
  };

  const deleteSpecificItem = async (itemId) => {
    await deleteItem(itemId);
    await fetchItems();
    await fetchOrders();
  };
  useEffect(() => {
    fetchItems();
    fetchOrders();
  }, []);

  const handleUpdateButton = (e) => {
    itemToUpdateRef.current = e.target.value;
    setShow(true);
  };

  const handleUpdateItemSubmit = (e) => {
    const itemId = itemToUpdateRef.current;
    const formData = new FormData(e.target),
      formDataObj = Object.fromEntries(formData.entries());
    const requestBody = {};
    for (let key in formDataObj) {
      if (formDataObj[key]) {
        requestBody[key] = formDataObj[key];
      }
    }
    updateSpecificItem(itemId, requestBody);
    setShow(false);
  };

  const handleDeleteButton = (e) => {
    const itemId = e.target.value;
    deleteSpecificItem(itemId);
  };

  const handleAddItemSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target),
      formDataObj = Object.fromEntries(formData.entries());
    createNewItem(formDataObj);
  };

  const handleClose = () => setShow(false);

  function createItemDisplay(items) {
    const tableBody = items.map((item) => {
      const updateButton = (
        <Button
          variant="secondary"
          value={item.id}
          onClick={(e) => handleUpdateButton(e)}
        >
          Update item
        </Button>
      );
      const deleteButton = (
        <Button
          variant="danger"
          value={item.id}
          onClick={(e) => handleDeleteButton(e)}
        >
          Delete item
        </Button>
      );
      return (
        <tr key={`item${item.id}`}>
          <td>{item.name}</td>
          <td>{item.price}</td>
          <td>{item.count}</td>
          <td>{updateButton}</td>
          <td>{deleteButton}</td>
        </tr>
      );
    });
    return (
      <div>
        <h1>Items</h1>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>Item Name</th>
              <th>Price</th>
              <th>Available count</th>
              <th>Update?</th>
              <th>Delete?</th>
            </tr>
          </thead>
          <tbody>{tableBody}</tbody>
        </Table>
        {modal}
      </div>
    );
  }

  function createAddItemForm() {
    return (
      <div>
        <Form onSubmit={(e) => handleAddItemSubmit(e)}>
          <h1>Add Item Form</h1>
          <Form.Group>
            <Form.Label>Item name</Form.Label>
            <Form.Control type="text" name="name" />
          </Form.Group>
          <br />
          <Form.Group>
            <Form.Label>Item price</Form.Label>
            <Form.Control type="text" name="price" />
          </Form.Group>
          <br />
          <Form.Group>
            <Form.Label>Item count</Form.Label>
            <Form.Control type="text" name="count" />
          </Form.Group>
          <br />
          <Button type="submit">Submit</Button>
        </Form>
      </div>
    );
  }
  const modal = (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Update Item</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form onSubmit={(e) => handleUpdateItemSubmit(e)}>
          <Form.Group className="mb-3">
            <Form.Label>Name</Form.Label>
            <Form.Control type="textarea" name="name" />
          </Form.Group>
          <Form.Group className="mb-3">
            <Form.Label>Price</Form.Label>
            <Form.Control type="textarea" name="price" />
          </Form.Group>
          <Form.Group className="mb-3">
            <Form.Label>Count</Form.Label>
            <Form.Control type="textarea" name="count" />
          </Form.Group>

          <Button type="submit" variant="primary">
            Update item
          </Button>
        </Form>
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>
          Close
        </Button>
      </Modal.Footer>
    </Modal>
  );
  const addItemForm = createAddItemForm();
  return (
    <Container>
      {itemDisplay}
      {addItemForm}
      {orderDisplay}
      {modal}
    </Container>
  );
}

function createOrderDisplay(orders) {
  const tableBody = orders.map((order) => {
    const itemOrders = order["item_orders"];
    const rowSpanSize = itemOrders.length;

    const itemOrderBody = itemOrders.map((itemOrder, index) => {
      let orderRow = null;
      if (index === 0) {
        orderRow = (
          <>
            <td rowSpan={rowSpanSize}>{order.id}</td>
            <td rowSpan={rowSpanSize}>{order.order_price}</td>
            <td rowSpan={rowSpanSize}>{order.date_created}</td>
            <td rowSpan={rowSpanSize}>{order.user_id}</td>
          </>
        );
      }
      return (
        <tr key={`${order.id}:${itemOrder.item}`}>
          {orderRow}
          <td>{itemOrder.item}</td>
          <td>{itemOrder.amount_bought}</td>
          <td>{itemOrder.total_price}</td>
        </tr>
      );
    });
    return itemOrderBody;
  });
  return (
    <div>
      <h1>Orders</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Order Price</th>
            <th>Order Created </th>
            <th>User ID</th>
            <th>Item Name</th>
            <th>Amount Bought</th>
            <th>Item Price</th>
          </tr>
        </thead>
        <tbody>{tableBody}</tbody>
      </Table>
    </div>
  );
}
