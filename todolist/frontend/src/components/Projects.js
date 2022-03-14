import React from "react";
import {Link} from "react-router-dom";

const ProjectItem = ({todoapp}) => {
    return (
        <tr>
            <td>
                <Link to={`/todoapp/${todoapp.id}`}>{todoapp.name}</Link>
            </td>
            <td>{todoapp.repository}</td>
            <td>{todoapp.users}</td>

        </tr>
    )
}

const ProjectList = ({todoapp}) => {
    return (
        <table>
            <thead>
            <tr>
                <th>Project</th>
                <th>URL</th>
                <th>Users</th>
            </tr>
            </thead>
            <tbody>
            {todoapp.map((project) => <ProjectItem key={todoapp.id} todoapp={todoapp}/>)}
            </tbody>
        </table>
    )
}

export default ProjectList;