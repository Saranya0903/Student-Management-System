// Delete confirmation
function confirmDelete() {
    return confirm("Are you sure you want to delete this record?");
}

// Student search filter
document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById("searchInput");

    if (input) {
        input.addEventListener("keyup", function() {
            let filter = input.value.toLowerCase();
            let rows = document.querySelectorAll("#studentTable tr");

            rows.forEach(function(row) {
                let text = row.textContent.toLowerCase();
                row.style.display = text.includes(filter) ? "" : "none";
            });
        });
    }
});
