function deleteNote(noteId) {
  fetch(`/note/${noteId}`, {
      method: "DELETE",
  }).then((response) => {
      if (response.ok) {
          window.location.href = "/";
      } else {
          console.error('Error deleting note');
      }
  }).catch((error) => {
      console.error(error);
  });
}
