        var dataTable;

        $(document).ready(function () {
            if ($('#applicant_table').length) {
                dataTable = $('#applicant_table').DataTable({
                    
                });

                // Function to handle approval
                $('.approve-button').on('click', function () {
                    var applicantId = $(this).data('applicant-id');
                    handleApproval(applicantId);
                });
    
                // Function to handle rejection button click and open modal
                $('.reject-button').on('click', function () {
                    var applicantId = $(this).data('applicant-id');
                    $('#confirmRejection').data('applicant-id', applicantId);
                    $('#rejectionModal').modal('show');
                    return false;
                });
    
                // Function to handle confirm rejection button click
                $('#confirmRejection').on('click', function () {
                    var applicantId = $(this).data('applicant-id');
                    var rejectionReason = $('#rejectionReason').val();
                    handleRejection(applicantId, rejectionReason);
                    $('#rejectionModal').modal('hide');
                    return false; // Prevent default form submission
                });
            } else {
                console.error('#applicant_table not found.');
            }
    
            function handleApproval(applicantId) {
                var csrf_token = $("[name=csrfmiddlewaretoken]").val();
    
                $.ajax({
                    type: 'POST',
                    url: '/approve_applicant/' + applicantId + '/',
                    data: {
                        csrfmiddlewaretoken: csrf_token,
                    },
                    success: function (data) {
                        console.log('Approval success:', data);
                        if (data.status === 'success' && dataTable) {
                            console.log('Reloading DataTable...');
                            dataTable.ajax.reload();
                        } else {
                            console.error('Error approving applicant.');
                        }
                    },
                    error: function () {
                        console.error('Error approving applicant. Please try again.');
                    }
                });
            }
    
            function handleRejection(applicantId, rejectionReason) {
                var csrf_token = $("[name=csrfmiddlewaretoken]").val();
    
                if (rejectionReason) {
                    $.ajax({
                        type: 'POST',
                        url: '/reject_applicant/' + applicantId + '/',
                        data: {
                            csrfmiddlewaretoken: csrf_token,
                            'rejection_reason': rejectionReason
                        },
                        success: function (data) {
                            console.log('Rejection success:', data);
                            if (data.status === 'success' && dataTable) {
                                console.log('Reloading DataTable...');
                                dataTable.ajax.reload();
                            } else {
                                console.error('Error: Unexpected response');
                                alert('Error: Unexpected response');
                            }
                        },
                        error: function (xhr) {
                            console.error('Error rejecting applicant:', xhr.responseText);
                            alert('Error rejecting applicant. Please try again.');
                        }
                    });
                } else {
                    alert('Rejection reason cannot be empty.');
                }
            }
        });