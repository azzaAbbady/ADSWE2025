// myapp/static/js/scripts.js
document.addEventListener('DOMContentLoaded', function () {
    // Add a confirmation dialog before deleting a post
    const deleteButtons = document.querySelectorAll('a[href*="delete"]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            if (!confirm('Are you sure you want to delete this post?')) {
                e.preventDefault(); // Cancel the action if the user clicks "No"
            }
        });
    });
});