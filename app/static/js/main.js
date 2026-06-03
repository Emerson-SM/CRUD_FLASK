const userForm = document.querySelector('#userForm')

let users = []
let editing = false
let userId = null

window.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("/api/users");
    const data = await response.json();
    users = data
    renderUser()
})

userForm.addEventListener('submit', async event => {
    event.preventDefault()

    const username = userForm['username'].value
    const password = userForm['password'].value
    const email = userForm['email'].value

    if (!editing) {
        const response = await fetch('/api/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username, 
                password: password, 
                email: email
            })
        })
        const new_user = await response.json()
        users.unshift(new_user)
    } else {
        const response = await fetch(`/api/users/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username, 
                password: password, 
                email: email
            })
        });
        const updatedUser = await response.json() 
        users = users.map(user => user.id === updatedUser.User.id ? updatedUser.User : user)
        editing = false
        userId = null
    }
    renderUser()
    userForm.reset();
});

function renderUser() {
    const userItem = document.querySelector('#userList')
    userList.innerHTML = ''

    users.forEach(user => {
        const userItem = document.createElement('li')
        userItem.classList = 'list-group-item list-group-item-dark my-2 p-3 shadow-sm'
        userItem.innerHTML = `
            <header class = "d-flex justify-content-between align-items-center">
                <h3>${user.username}</h3>
                <div>
                    <button class="btn-delete btn btn-danger btn-sm">Delete</button>
                    <button class="btn-edit btn btn-secondary btn-sm">Edit</button>
                </div>
            </header>
            <p>${user.email}</p>
        `
        const btnDelete = userItem.querySelector('.btn-delete')
        btnDelete.addEventListener('click', async () => {
            const response = await fetch(`/api/users/${user.id}`, {
                method: 'DELETE'
            })
            const data = await response.json()
            
            if (response.ok) {
                alert(`User ${user.username} deleted`)
                
                users = users.filter(user => user.id !== data.deleted_data.id)
                renderUser()
            } else {
                alert('Error al borrar: ' + (data.Error || 'Desconocido'))
            }
        }) 
        
        const btnEdit = userItem.querySelector('.btn-edit')
        btnEdit.addEventListener('click', async () => {
            const response = await fetch(`/api/users/${user.id}`)
            const data = await response.json()

            userForm['username'].value = data.username
            userForm['email'].value = data.email

            editing = true
            userId = data.id
        })
        userList.append(userItem)
    });
}