import React from "react";

const TodoItem = ({todolist}) => {
    return (
        <tr>
            <td>{todolist.user}</td>
            <td>{todolist.description}</td>
            <td>{todolist.active}</td>
            <td>{todolist.project}</td>
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
        </table>
    )
}

export default TodoList;