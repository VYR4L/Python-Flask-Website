function deleteUser(userId) {
    fetch(`/user/${userId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json" 
        },
    }).then((response) => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error deleting user');
        }
    }).then((data) => {
        window.location.reload();
    }).catch((error) => {
        console.error(error);
    });
}
