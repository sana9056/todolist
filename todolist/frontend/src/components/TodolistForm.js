import React from 'react'

class TodolistForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {User: '', Description: '', Active: '', Project: ''}
    }
    
    handleChange(event)
    {
        this.setState(
            {
                [event.target.User]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        console.log(this.state.User)
        console.log(this.state.Description)
        console.log(this.state.Active)
        console.log(this.state.Project)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">User</label>
                    <input type="text" className="form-control" name="User" value={this.state.User} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="Description">author</label>
                    <input type="number" className="form-control" name="Description" value={this.state.Description} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="Active">author</label>
                    <input type="number" className="form-control" name="Active" value={this.state.Active} onChange={(event)=>this.handleChange(event)} />
                </div>

                <div className="form-group">
                    <label for="author">Project</label>
                    <input type="number" className="form-control" name="Project" value={this.state.Project} onChange={(event)=>this.handleChange(event)} />
                </div>

                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }

}

export default TodolistForm