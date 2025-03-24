document.addEventListener('DOMContentLoaded', function () {
    console.log('HR Management System is ready!');
});

document.addEventListener('DOMContentLoaded', function () {
    // Add confirmation for delete actions
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
});