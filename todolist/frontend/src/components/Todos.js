import React from 'react'
import {Link} from 'react-router-dom'


const TodoItem = ({todolist}) => {
    return (
        <tr>
            <td>{todolist.user}</td>
            <td>{todolist.description}</td>
            <td>{todolist.active}</td>
            <td>{todolist.project}</td>
            <td><button onClick={()=>deleteTODO(item.id)} type='button'>Delete</button></td>

        </tr>
    )
}

const TodoList = ({todolist}) => {
    return (
        <table>
            <thead>
            <tr>
                <th>User</th>
                <th>Description</th>
                <th>Active</th>
                <th>Project</th>
            </tr>
            </thead>
            <tbody>
            {todolist.map((todolist) => <TodoItem key={todolist.id} todolist={todolist}/>)}
            </tbody>
            {items.map((todolist) => <TodoItem todolist={todolist} deleteTODO={deleteTODO}/>)}
            <Link to='/books/create'>Create</Link>
        </table>
    )
}
//изменение


export default TodoList
