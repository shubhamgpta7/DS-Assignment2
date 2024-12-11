import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import AddUserPage from './components/AddUser';
import UserListPage from './components/UserList';
import HomePage from './components/HomePage'; // Import the HomePage
import { AppBar, Toolbar, Button, Container } from '@mui/material';

function App() {
  return (
    <Router>
      <AppBar position="static">
        <Toolbar>
          <Button color="inherit" component={Link} to="/">Home</Button>
          <Button color="inherit" component={Link} to="/add-user">Add User</Button>
          <Button color="inherit" component={Link} to="/user-list">User List</Button>
        </Toolbar>
      </AppBar>
      <Container>
        <Routes>
          <Route path="/" element={<HomePage />} />  {/* Set HomePage as default route */}
          <Route path="/add-user" element={<AddUserPage />} />
          <Route path="/user-list" element={<UserListPage />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
