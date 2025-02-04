const deleteButtons = document.getElementsByClassName("btn-danger");
const editButtons = document.getElementsByClassName("btn-secondary-update");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("data-booking-id");
    deleteModal.show();

    deleteConfirm.addEventListener("click", () => {
      if (bookingId) {
        window.location.href = `delete_booking/${bookingId}`;
      }
    });
  });
}

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let bookingId = e.target.getAttribute("data-booking-id");
        window.location.href=`update_booking/${bookingId}`;     
        
    });

}