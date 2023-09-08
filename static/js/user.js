document.addEventListener("DOMContentLoaded", function() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const skills = document.querySelectorAll('.row.mb-12');
    
    skills.forEach((skill) => {
        const skillId = skill.getAttribute('data-id');
        const submitButton = skill.querySelector(`#submitButton-${skillId}`);
        const minutesInput = skill.querySelector(`#minutes_spent-${skillId}`);
        const confirmModal = skill.querySelector(`#confirmModal-${skillId}`);
        const modalContent = confirmModal.querySelector('.modal-content');
        const myModal = new bootstrap.Modal(confirmModal, {});
        let allowClose = true;
        
        submitButton.addEventListener("click", function() {
            myModal.show();
        });
        
        confirmModal.addEventListener('show.bs.modal', function () {
            const minutes = minutesInput.value;
            confirmModal.querySelector(`#minutes_spent`).value = minutes;
        });
        
        confirmModal.addEventListener('hidden.bs.modal', function () {
            if (allowClose) return;
            const minutes = minutesInput.value;
            if (!Number.isInteger(Number(minutes)) || minutes === "") {
                modalContent.classList.add('shake');
                setTimeout(() => modalContent.classList.remove('shake'), 1000);
                myModal.show();
            }
        });

        const form = confirmModal.querySelector('form');
        form.addEventListener('submit', function(e) {
            const minutes = minutesInput.value;
            if (!Number.isInteger(Number(minutes)) || minutes === "") {
                e.preventDefault();
                allowClose = false;
                modalContent.classList.add('shake');
                setTimeout(() => modalContent.classList.remove('shake'), 1000);
                myModal.show();
            } else {
                allowClose = true;
            }
        });

        const closeModalButtons = confirmModal.querySelectorAll('.btn-close, .btn-secondary');
        closeModalButtons.forEach(button => {
            button.addEventListener('click', () => {
                allowClose = true;
            });
        });
    });
});