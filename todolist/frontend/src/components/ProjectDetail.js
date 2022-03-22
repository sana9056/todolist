import React from "react";
import {useParams} from "react-router-dom";


const ProjectItem = ({todoapp}) => {
    return (
        <tr>
            <td>HELLO DETAIL PROJECT</td>
            <td>{todoapp.id}</td>
            <td>{todoapp.name}</td>
            <td>{todoapp.repository}</td>
        </tr>
    )
}

const ProjectDetail = ({todoapp}) => {
    let {id} = useParams();
    let filtertodoapp = todoapp.filter((todoapp) => todoapp.id === +id);
    return (
        <table>
            <thead>
            <tr>
                <th>DETAIL</th>
                <th>ID</th>
                <th>Project</th>
                <th>URL</th>
            </tr>
            </thead>
            <tbody>
            {filtertodoapp.map((todoapp) => <ProjectItem key={todoapp.id} todoapp={todoapp}/>)}
            </tbody>
        </table>
    )
}
export default ProjectDetail;