import React from "react";

const UserItem = ({userapp}) => {
    return (
        <tr>
            <td>{userapp.first_name}</td>
            <td>{userapp.last_name}</td>
            <td>{userapp.username}</td>
        </tr>
    )
}

const UserList = ({userapp}) => {
    return (
        <table>
            <thead>
            <tr>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Username</th>
            </tr>
            </thead>
            <tbody>
            {userapp.map((userapp) => <UserItem key={userapp.id} userapp={userapp}/>)}
            </tbody>
        </table>
    )
}

export default UserList;