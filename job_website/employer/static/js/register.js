let first_name = document.querySelector('#first_name');
            let last_name = document.querySelector('#last_name');
            let company = document.querySelector('#company');
            let company_address = document.querySelector('#company_address');
            let email = document.querySelector('#email');
            let phone = document.querySelector('#phone');
            let validation_firstName = document.querySelector('#validation_firstName');
            let validation_lastName = document.querySelector('#validation_lastName');
            let validation_company = document.querySelector('#validation_company');
            let validation_companyAddress = document.querySelector('#validation_companyAddress');
            let validation_email = document.querySelector('#validation_email');
            let validation_phone = document.querySelector('#validation_phone');

            function validateInput() {
                if (first_name.value === '') {
                    first_name.classList.add('is-invalid');
                    validation_firstName.classList.add('invalid-feedback');
                    validation_firstName.innerHTML = 'First name is required';
                } else if (first_name.value.length < 2) {
                    first_name.classList.add('is-invalid');
                    validation_firstName.classList.add('invalid-feedback');
                    validation_firstName.innerHTML = 'First name must be at least 2 characters';
                } else if (first_name.value.length > 50) {
                    first_name.classList.add('is-invalid');
                    validation_firstName.classList.add('invalid-feedback');
                    validation_firstName.innerHTML = 'First name must be less than 50 characters';
                } else if (!first_name.value.match(/^[a-zA-Z\s]+$/)) {
                    first_name.classList.add('is-invalid');
                    validation_firstName.classList.add('invalid-feedback');
                    validation_firstName.innerHTML = 'First name must only contain letters';
                } else {
                    first_name.classList.remove('is-invalid');
                    first_name.classList.add('is-valid');
                    validation_firstName.classList.remove('invalid-feedback');
                    validation_firstName.innerHTML = '';
                }

                if (last_name.value === '') {
                    last_name.classList.add('is-invalid');
                    validation_lastName.classList.add('invalid-feedback');
                    validation_lastName.innerHTML = 'Last name is required';
                } else if (last_name.value.length < 2) {
                    last_name.classList.add('is-invalid');
                    validation_lastName.classList.add('invalid-feedback');
                    validation_lastName.innerHTML = 'Last name must be at least 2 characters';
                } else if (last_name.value.length > 50) {
                    last_name.classList.add('is-invalid');
                    validation_lastName.classList.add('invalid-feedback');
                    validation_lastName.innerHTML = 'Last name must be less than 50 characters';
                } else if (!last_name.value.match(/^[a-zA-Z\s]+$/)) {
                    last_name.classList.add('is-invalid');
                    validation_lastName.classList.add('invalid-feedback');
                    validation_lastName.innerHTML = 'Last name must only contain letters';
                } else {
                    last_name.classList.remove('is-invalid');
                    last_name.classList.add('is-valid');
                    validation_lastName.classList.remove('invalid-feedback');
                    validation_lastName.innerHTML = '';
                }

                if (company.value === '') {
                    company.classList.add('is-invalid');
                    validation_company.classList.add('invalid-feedback');
                    validation_company.innerHTML = 'Company name is required';
                }  else {
                    company.classList.remove('is-invalid');
                    company.classList.add('is-valid');
                    validation_company.classList.remove('invalid-feedback');
                    validation_company.innerHTML = '';
                }

                if (company_address.value === '') {
                    company_address.classList.add('is-invalid');
                    validation_companyAddress.classList.add('invalid-feedback');
                    validation_companyAddress.innerHTML = 'Company address is required';
                }  else {
                    company_address.classList.remove('is-invalid');
                    company_address.classList.add('is-valid');
                    validation_companyAddress.classList.remove('invalid-feedback');
                    validation_companyAddress.innerHTML = '';
                }

                if (email.value === '') {
                    email.classList.add('is-invalid');
                    validation_email.classList.add('invalid-feedback');
                    validation_email.innerHTML = 'Email address is required';
                } else if (!email.value.match(/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/)) {
                    email.classList.add('is-invalid');
                    validation_email.classList.add('invalid-feedback');
                    validation_email.innerHTML = 'Email address is invalid';
                } else {
                    email.classList.remove('is-invalid');
                    email.classList.add('is-valid');
                    validation_email.classList.remove('invalid-feedback');
                    validation_email.innerHTML = '';
                }

                if (phone.value === '') {
                    phone.setCustomValidity('Phone number is required');
                } else {
                    phone.setCustomValidity('');
                }
            }


            first_name.addEventListener('keyup', validateInput);
            last_name.addEventListener('keyup', validateInput);
            company.addEventListener('keyup', validateInput);
            company_address.addEventListener('keyup', validateInput);
            email.addEventListener('keyup', validateInput);
            phone.addEventListener('keyup', validateInput);


            document.addEventListener('DOMContentLoaded', function () {
                    const form = document.querySelector('.needs-validation');

                    function validatePassword() {
                        const password = document.querySelector('#password');
                        const confirmPassword = document.querySelector('#confirm-password');
                        if (password.value !== confirmPassword.value) {
                            confirmPassword.setCustomValidity('Password does not match');
                        } else {
                            confirmPassword.setCustomValidity('');
                        }
                    }

                    password.addEventListener('change', validatePassword);
                    confirmPassword.addEventListener('keyup', validatePassword);

                    
                });