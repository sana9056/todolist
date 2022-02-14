import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import axios from 'axios'
import Footer from './components/Footer.js'
import Navbar from './components/Menu.js'

const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'user': []
       }
   }

   componentDidMount() {
   axios.get('http://127.0.0.1:8000/api/users/')
       .then(response => {
           const user = response.data
               this.setState(
               {
                   'user': user
               }
           )
       }).catch(error => console.log(error))
   }

   render () {
       return (
           <div>
               <UserList user={this.state.user} />
           </div>
       )
   }
}


export default App;