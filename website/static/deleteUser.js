function deleteUser(userId) {
    fetch("/delete-user", {
        method: "POST",
        headers: {
            "Content-Type": "application/json" 
        },
        body: JSON.stringify({ userId: userId }),
    }).then((response) => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Erro ao excluir o usuário');
        }
    }).then((data) => {
        window.location.reload();
    }).catch((error) => {
        console.error(error);
    });
}
