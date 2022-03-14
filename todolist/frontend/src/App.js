import React from "react";
import './App.css';
import UserList from "./components/Users";
import ProjectList from "./components/Projects";
import TodoList from "./components/Todos";
import axios from "axios";
import {BrowserRouter, Route, Link} from 'react-router-dom';
import ProjectDetail from "./components/ProjectDetail";
import Cookies from "universal-cookie/lib";
import LoginForm from "./components/Auth";




class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'userapp': [],
            'todoapp': [],
            'todolist': [],
        }
    }

    logout() {
        this.setToken('');
    }

    getToken(username, password) {
        console.log(this);
        console.log(username, password);
        axios.post(
            'http://127.0.0.1:8000/api-auth-token/',
            {username: username, password: password}
        ).then(response => {
            this.setToken(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    getTokenFromStorage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        console.log("token", token);
        this.setState({'token': token}, () => this.loadData())
    }

    setToken(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.loadData())
    }

    loadData() {
        if (!this.isAuthenticated()) {
            return;
        }
        const headers = this.getHeaders()
        axios.get('http://127.0.0.1:8000/api/userapp', {headers}).then(
            response => {
                const userapp = response.data.results
                this.setState(
                    {'userapp': userapp}
                )
            }
        ).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/todoapp', {headers}).then(
            response => {
                const todoapp = response.data.results
                this.setState(
                    {'todoapp': todoapp}
                )
            }
        ).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/todolist', {headers}).then(
            response => {
                const todolist = response.data.results
                this.setState(
                    {'todolist': todolist}
                )
            }
        ).catch(error => console.log(error))

    }

    getHeaders() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.isAuthenticated()) {
            headers['Authorization'] = `Token ${this.state.token}`;
        }
        return headers
    }

    isAuthenticated() {
        return this.state.token !== '';
    }

    componentDidMount() {
        this.getTokenFromStorage();
    }


    render() {
        return (
            <div className={'App'}>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to={'/'}>Userapp</Link>
                            </li>
                            <li>
                                <Link to={'/todoapp'}>todoapp</Link>
                            </li>
                            <li>
                                <Link to={'/todolist'}>todoapp</Link>
                            </li>
                            <li>
                                {this.isAuthenticated() ?
                                    <button onClick={() => this.logout()}>
                                        Logout
                                    </button> :
                                    <Link to={'/login'}>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Route exact path='/' component={() => <UserList userapp={this.state.users}/>}/>
                    <Route exact path='/todoapp' component={() => <ProjectList todoapp={this.state.projects}/>}/>
                    <Route exact path='/todolist' component={() => <TodoList todolist={this.state.todos}/>}/>
                    <Route exact path='/todoapp/:id/'
                           component={() => <ProjectDetail todoapp={this.state.projects}/>}/>
                    <Route exact path={'/login'}>
                        <LoginForm getToken={(username, password) => this.getToken(username, password)}/>
                    </Route>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;