import React from "react";
import { Navbar, Nav, Container, NavDropdown } from "react-bootstrap";

const CustomNavbar = (props) => {
  return (
    <Navbar expand="lg" sticky="top" className="bg-body-tertiary">
      <Container>
        <Navbar.Brand>Shopping Store</Navbar.Brand>

        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse>
          <Nav className="me-auto"></Nav>
          <Nav>
            <Nav.Item>
              <Nav.Link href="/">Customer</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link href="admin">Admin</Nav.Link>
            </Nav.Item>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default CustomNavbar;
